"""Local conftest for beifong — adds the project root to sys.path so tests can
`from db.connection import ...` the same way the app does, and seeds the
tracking-db schema for tests that need it."""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

import pytest

BEIFONG_ROOT = Path(__file__).resolve().parent.parent
if str(BEIFONG_ROOT) not in sys.path:
    sys.path.insert(0, str(BEIFONG_ROOT))


def _apply_tracking_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS feed_tracking (
            feed_id INTEGER PRIMARY KEY,
            source_id INTEGER,
            feed_url TEXT,
            last_processed TIMESTAMP,
            last_etag TEXT,
            last_modified TEXT,
            entry_hash TEXT
        );
        CREATE TABLE IF NOT EXISTS feed_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feed_id INTEGER,
            source_id INTEGER,
            entry_id TEXT,
            title TEXT,
            link TEXT UNIQUE,
            published_date TIMESTAMP,
            content TEXT,
            summary TEXT,
            crawl_status TEXT DEFAULT 'pending',
            crawl_attempts INTEGER DEFAULT 0,
            processed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(feed_id, entry_id)
        );
        CREATE TABLE IF NOT EXISTS crawled_articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_id INTEGER,
            source_id INTEGER,
            feed_id INTEGER,
            title TEXT,
            url TEXT UNIQUE,
            published_date TIMESTAMP,
            raw_content TEXT,
            content TEXT,
            summary TEXT,
            metadata TEXT,
            ai_status TEXT DEFAULT 'pending',
            ai_error TEXT DEFAULT NULL,
            ai_attempts INTEGER DEFAULT 0,
            crawled_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            processed BOOLEAN DEFAULT 0,
            embedding_status TEXT DEFAULT NULL
        );
        CREATE TABLE IF NOT EXISTS article_categories (
            article_id INTEGER,
            category_name TEXT NOT NULL,
            PRIMARY KEY (article_id, category_name)
        );
        """
    )
    conn.commit()


@pytest.fixture
def tracking_db(tmp_path) -> str:
    """Path to a fresh tracking DB with the production schema applied."""
    path = tmp_path / "tracking.db"
    with sqlite3.connect(path) as conn:
        _apply_tracking_schema(conn)
    return str(path)


@pytest.fixture
def empty_db(tmp_path) -> str:
    """Path to an empty SQLite DB — caller applies its own schema."""
    path = tmp_path / "empty.db"
    path.touch()
    return str(path)
