"""Round-trip tests for db.feeds against a temp tracking + sources DB."""

from __future__ import annotations

import sqlite3

import pytest

from db.feeds import (
    count_active_feeds,
    ensure_feed_tracking_exists,
    get_active_feeds,
    get_feed_stats,
    get_feed_tracking_info,
    get_uncrawled_entries,
    mark_entries_as_processing,
    store_feed_entries,
    update_feed_tracking,
    update_tracking_info,
)


@pytest.fixture
def sources_db(tmp_path) -> str:
    path = tmp_path / "sources.db"
    with sqlite3.connect(path) as conn:
        conn.executescript(
            """
            CREATE TABLE sources (
                id INTEGER PRIMARY KEY,
                name TEXT,
                is_active BOOLEAN DEFAULT 1
            );
            CREATE TABLE source_feeds (
                id INTEGER PRIMARY KEY,
                source_id INTEGER,
                feed_url TEXT UNIQUE,
                feed_type TEXT,
                is_active BOOLEAN DEFAULT 1,
                last_crawled TIMESTAMP
            );
            INSERT INTO sources (id, name, is_active) VALUES (1, 'Hacker News', 1), (2, 'Inactive', 0);
            INSERT INTO source_feeds (id, source_id, feed_url, feed_type, is_active) VALUES
                (10, 1, 'https://news.ycombinator.com/rss', 'rss', 1),
                (11, 1, 'https://example.com/feed', 'rss', 0),
                (12, 2, 'https://inactive.example/feed', 'rss', 1);
            """
        )
    return str(path)


def test_get_active_feeds_skips_inactive(sources_db):
    rows = get_active_feeds(sources_db)
    assert len(rows) == 1
    assert rows[0]["feed_url"] == "https://news.ycombinator.com/rss"
    assert rows[0]["source_name"] == "Hacker News"


def test_get_active_feeds_respects_limit(sources_db):
    rows = get_active_feeds(sources_db, limit=10, offset=0)
    assert len(rows) == 1


def test_count_active_feeds(sources_db):
    assert count_active_feeds(sources_db) == 1


def test_count_active_feeds_zero(tmp_path):
    path = tmp_path / "empty_sources.db"
    with sqlite3.connect(path) as conn:
        conn.executescript(
            """
            CREATE TABLE sources (id INTEGER PRIMARY KEY, name TEXT, is_active BOOLEAN DEFAULT 1);
            CREATE TABLE source_feeds (id INTEGER PRIMARY KEY, source_id INTEGER, is_active BOOLEAN DEFAULT 1);
            """
        )
    assert count_active_feeds(str(path)) == 0


def test_ensure_feed_tracking_exists_is_idempotent(tracking_db):
    ensure_feed_tracking_exists(tracking_db, 1, 1, "https://x/feed")
    ensure_feed_tracking_exists(tracking_db, 1, 1, "https://x/feed")
    info = get_feed_tracking_info(tracking_db, 1)
    assert info["feed_url"] == "https://x/feed"


def test_update_feed_tracking_writes_provided_values(tracking_db):
    ensure_feed_tracking_exists(tracking_db, 1, 1, "https://x/feed")
    update_feed_tracking(tracking_db, 1, etag="W/abc", modified="Mon", entry_hash="h1")
    info = get_feed_tracking_info(tracking_db, 1)
    assert info["last_etag"] == "W/abc"
    assert info["last_modified"] == "Mon"
    assert info["entry_hash"] == "h1"


def test_store_feed_entries_inserts_unique_links(tracking_db):
    entries = [
        {"entry_id": "1", "title": "A", "link": "https://x/1", "published_date": "2024-01-01", "content": "", "summary": ""},
        {"entry_id": "2", "title": "B", "link": "https://x/2", "published_date": "2024-01-02", "content": "", "summary": ""},
    ]
    inserted = store_feed_entries(tracking_db, feed_id=1, source_id=1, entries=entries)
    assert inserted == 2


def test_store_feed_entries_silently_skips_duplicates(tracking_db):
    e = {"entry_id": "1", "title": "A", "link": "https://x/1", "published_date": "2024-01-01", "content": "", "summary": ""}
    store_feed_entries(tracking_db, 1, 1, [e])
    inserted = store_feed_entries(tracking_db, 1, 1, [e, e])
    assert inserted == 0


def test_update_tracking_info_inserts_or_ignores(tracking_db):
    feeds = [
        {"id": 1, "source_id": 1, "feed_url": "https://x/1"},
        {"id": 2, "source_id": 1, "feed_url": "https://x/2"},
    ]
    update_tracking_info(tracking_db, feeds)
    update_tracking_info(tracking_db, feeds)  # second call is a no-op
    info1 = get_feed_tracking_info(tracking_db, 1)
    info2 = get_feed_tracking_info(tracking_db, 2)
    assert info1["feed_url"] == "https://x/1"
    assert info2["feed_url"] == "https://x/2"


def test_get_uncrawled_entries_marks_them_processing(tracking_db):
    store_feed_entries(
        tracking_db, 1, 1,
        [{"entry_id": "1", "title": "A", "link": "https://x/1", "published_date": "2024-01-01", "content": "", "summary": ""}],
    )
    rows = get_uncrawled_entries(tracking_db, limit=10)
    assert len(rows) == 1
    with sqlite3.connect(tracking_db) as conn:
        status = conn.execute("SELECT crawl_status FROM feed_entries WHERE id = 1").fetchone()
    assert status[0] == "processing"


def test_get_uncrawled_entries_skips_entries_with_existing_article(tracking_db):
    store_feed_entries(
        tracking_db, 1, 1,
        [{"entry_id": "1", "title": "A", "link": "https://x/1", "published_date": "2024-01-01", "content": "", "summary": ""}],
    )
    with sqlite3.connect(tracking_db) as conn:
        conn.execute(
            "INSERT INTO crawled_articles (entry_id, url, title) VALUES (?,?,?)",
            ("1", "https://x/1", "Article"),
        )
        conn.commit()
    rows = get_uncrawled_entries(tracking_db, limit=10)
    assert rows == []


def test_get_uncrawled_entries_respects_max_attempts(tracking_db):
    store_feed_entries(
        tracking_db, 1, 1,
        [{"entry_id": "1", "title": "A", "link": "https://x/1", "published_date": "2024-01-01", "content": "", "summary": ""}],
    )
    with sqlite3.connect(tracking_db) as conn:
        conn.execute("UPDATE feed_entries SET crawl_attempts = 5 WHERE id = 1")
        conn.commit()
    rows = get_uncrawled_entries(tracking_db, limit=10, max_attempts=3)
    assert rows == []


def test_mark_entries_as_processing_empty_returns_zero(tracking_db):
    assert mark_entries_as_processing(tracking_db, []) == 0


def test_get_feed_stats(tracking_db):
    store_feed_entries(
        tracking_db, 1, 1,
        [
            {"entry_id": "1", "title": "A", "link": "https://x/1", "published_date": "2024-01-01", "content": "", "summary": ""},
            {"entry_id": "2", "title": "B", "link": "https://x/2", "published_date": "2024-01-02", "content": "", "summary": ""},
        ],
    )
    stats = get_feed_stats(tracking_db)
    assert stats["total_entries"] == 2
    assert stats["pending_entries"] == 2
