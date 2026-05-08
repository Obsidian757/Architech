"""Unit tests for db.connection — the SQLite helper used by every db.* module."""

from __future__ import annotations

import sqlite3

import pytest


def test_db_connection_returns_row_factory(seeded_path):
    from db.connection import db_connection

    with db_connection(seeded_path) as conn:
        row = conn.execute("SELECT * FROM widgets WHERE id = 1").fetchone()
        assert row["name"] == "alpha"
        assert row["qty"] == 1


def test_db_connection_closes_on_exit(seeded_path):
    from db.connection import db_connection

    with db_connection(seeded_path) as conn:
        cursor = conn.cursor()
    with pytest.raises(sqlite3.ProgrammingError):
        cursor.execute("SELECT 1")


def test_execute_query_fetch_returns_list_of_dicts(seeded_path):
    from db.connection import execute_query

    rows = execute_query(seeded_path, "SELECT id, name FROM widgets ORDER BY id", fetch=True)
    assert rows == [
        {"id": 1, "name": "alpha"},
        {"id": 2, "name": "beta"},
        {"id": 3, "name": "gamma"},
    ]


def test_execute_query_fetch_one_returns_single_dict(seeded_path):
    from db.connection import execute_query

    row = execute_query(seeded_path, "SELECT name FROM widgets WHERE id = ?", (2,), fetch_one=True)
    assert row == {"name": "beta"}


def test_execute_query_fetch_one_returns_none_when_no_match(seeded_path):
    from db.connection import execute_query

    row = execute_query(seeded_path, "SELECT name FROM widgets WHERE id = ?", (999,), fetch_one=True)
    assert row is None


def test_execute_query_insert_returns_lastrowid(seeded_path):
    from db.connection import execute_query

    new_id = execute_query(
        seeded_path,
        "INSERT INTO widgets (name, qty) VALUES (?, ?)",
        ("delta", 4),
    )
    assert new_id == 4

    rows = execute_query(seeded_path, "SELECT name FROM widgets WHERE id = ?", (4,), fetch=True)
    assert rows == [{"name": "delta"}]


def test_execute_query_propagates_sql_errors(seeded_path):
    from db.connection import execute_query

    with pytest.raises(sqlite3.OperationalError):
        execute_query(seeded_path, "SELECT * FROM does_not_exist", fetch=True)


@pytest.fixture
def seeded_path(tmp_path) -> str:
    path = tmp_path / "widgets.db"
    with sqlite3.connect(path) as conn:
        conn.execute("CREATE TABLE widgets (id INTEGER PRIMARY KEY, name TEXT, qty INTEGER)")
        conn.executemany(
            "INSERT INTO widgets (name, qty) VALUES (?, ?)",
            [("alpha", 1), ("beta", 2), ("gamma", 3)],
        )
        conn.commit()
    return str(path)
