"""Round-trip tests for db.articles against a temp tracking DB."""

from __future__ import annotations

import json

from db.articles import (
    get_article_by_id,
    get_article_categories,
    get_article_stats,
    get_articles_by_category,
    get_articles_by_date_range,
    get_categories_with_counts,
    get_unprocessed_articles,
    mark_articles_as_processing,
    save_article_categories,
    store_crawled_article,
    update_article_status,
    update_entry_status,
)


def _entry(entry_id: str = "e1", **overrides) -> dict:
    base = {
        "id": entry_id,
        "source_id": 1,
        "feed_id": 1,
        "title": "T",
        "link": f"https://example.com/{entry_id}",
        "published_date": "2024-01-01T00:00:00",
    }
    base.update(overrides)
    return base


def test_store_crawled_article_returns_true_on_success(tracking_db):
    assert store_crawled_article(tracking_db, _entry("e1"), "raw", {"k": "v"}) is True


def test_store_crawled_article_returns_false_on_duplicate_url(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    # url has UNIQUE constraint — second insert with same link should fail.
    duplicate = _entry("e2")
    duplicate["link"] = "https://example.com/e1"  # force the URL collision
    assert store_crawled_article(tracking_db, duplicate, "raw", {}) is False


def test_get_article_by_id_parses_metadata_json(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {"author": "alice"})
    row = get_article_by_id(tracking_db, 1)
    assert row is not None
    assert row["metadata"] == {"author": "alice"}
    assert row["categories"] == []


def test_get_article_by_id_handles_invalid_metadata(tracking_db):
    # Insert a row with non-JSON metadata directly.
    import sqlite3

    with sqlite3.connect(tracking_db) as conn:
        conn.execute(
            "INSERT INTO crawled_articles (entry_id, title, url, metadata) VALUES (?,?,?,?)",
            ("e1", "T", "https://example.com/x", "not-json"),
        )
        conn.commit()
    row = get_article_by_id(tracking_db, 1)
    assert row["metadata"] == {}


def test_save_and_get_article_categories(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    inserted = save_article_categories(tracking_db, 1, ["AI", " ML ", "ai"])
    # 3 rows attempted; "ai" duplicates "AI" after lower/strip → second insert fails silently
    assert inserted >= 2
    cats = get_article_categories(tracking_db, 1)
    assert "ai" in cats
    assert "ml" in cats


def test_save_article_categories_replaces_existing(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    save_article_categories(tracking_db, 1, ["one", "two"])
    save_article_categories(tracking_db, 1, ["three"])
    assert get_article_categories(tracking_db, 1) == ["three"]


def test_save_article_categories_empty_returns_zero(tracking_db):
    assert save_article_categories(tracking_db, 1, []) == 0


def test_update_article_status_success_marks_processed(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    update_article_status(
        tracking_db,
        1,
        results={"summary": "S", "content": "C", "categories": ["news"]},
        success=True,
    )
    row = get_article_by_id(tracking_db, 1)
    assert row["processed"] == 1
    assert row["ai_status"] == "success"
    assert row["summary"] == "S"
    assert row["content"] == "C"
    assert row["categories"] == ["news"]


def test_update_article_status_failure_sets_error(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    update_article_status(tracking_db, 1, success=False, error_message="boom")
    row = get_article_by_id(tracking_db, 1)
    assert row["ai_status"] == "error"
    assert row["ai_error"] == "boom"
    assert row["ai_attempts"] == 1


def test_update_article_status_categories_string_with_json(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    update_article_status(
        tracking_db,
        1,
        results={"summary": "", "content": "", "categories": json.dumps(["a", "b"])},
        success=True,
    )
    assert sorted(get_article_categories(tracking_db, 1)) == ["a", "b"]


def test_update_article_status_categories_string_csv_fallback(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    update_article_status(
        tracking_db,
        1,
        results={"summary": "", "content": "", "categories": "x, y , z"},
        success=True,
    )
    assert sorted(get_article_categories(tracking_db, 1)) == ["x", "y", "z"]


def test_get_unprocessed_articles_marks_returned_rows_as_processing(tracking_db):
    for i in range(1, 4):
        store_crawled_article(tracking_db, _entry(f"e{i}"), "raw", {})
    rows = get_unprocessed_articles(tracking_db, limit=10)
    assert len(rows) == 3
    # After fetch, they should all be in 'processing' state.
    import sqlite3

    with sqlite3.connect(tracking_db) as conn:
        statuses = [r[0] for r in conn.execute("SELECT ai_status FROM crawled_articles")]
    assert all(s == "processing" for s in statuses)


def test_get_unprocessed_articles_resets_stuck_rows_first(tracking_db):
    """Rows already in 'processing' should be reset to 'pending' and re-returned."""
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    mark_articles_as_processing(tracking_db, [1])
    rows = get_unprocessed_articles(tracking_db, limit=10)
    assert len(rows) == 1


def test_mark_articles_as_processing_empty_list(tracking_db):
    assert mark_articles_as_processing(tracking_db, []) == 0


def test_get_articles_by_date_range_filters(tracking_db):
    for i, day in enumerate(["2024-01-01", "2024-02-01", "2024-03-01"], start=1):
        store_crawled_article(
            tracking_db,
            _entry(f"e{i}", published_date=day),
            "raw",
            {},
        )
        # Mark them as success so the WHERE filter passes.
        update_article_status(
            tracking_db, i, results={"summary": "", "content": ""}, success=True
        )
    rows = get_articles_by_date_range(tracking_db, start_date="2024-02-01", end_date="2024-02-28")
    assert len(rows) == 1
    assert rows[0]["published_date"].startswith("2024-02-01")


def test_get_articles_by_category(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    update_article_status(
        tracking_db,
        1,
        results={"summary": "S", "content": "C", "categories": ["foo"]},
        success=True,
    )
    rows = get_articles_by_category(tracking_db, "foo")
    assert len(rows) == 1
    assert rows[0]["title"] == "T"


def test_get_article_stats_counts_states(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    store_crawled_article(tracking_db, _entry("e2"), "raw", {})
    update_article_status(
        tracking_db, 1, results={"summary": "", "content": ""}, success=True
    )
    stats = get_article_stats(tracking_db)
    assert stats["total_articles"] == 2
    assert stats["success_articles"] == 1
    assert stats["pending_articles"] == 1


def test_get_categories_with_counts(tracking_db):
    store_crawled_article(tracking_db, _entry("e1"), "raw", {})
    save_article_categories(tracking_db, 1, ["a", "b", "a"])  # last "a" deduped via lower
    counts = get_categories_with_counts(tracking_db)
    names = {c["category_name"] for c in counts}
    assert "a" in names and "b" in names


def test_update_entry_status_increments_attempts(tracking_db):
    import sqlite3

    with sqlite3.connect(tracking_db) as conn:
        conn.execute(
            "INSERT INTO feed_entries (id, feed_id, source_id, entry_id, link) VALUES (1, 1, 1, 'e1', 'https://x')"
        )
        conn.commit()
    update_entry_status(tracking_db, 1, "failed")
    with sqlite3.connect(tracking_db) as conn:
        row = conn.execute("SELECT crawl_attempts, crawl_status FROM feed_entries WHERE id = 1").fetchone()
    assert row == (1, "failed")
