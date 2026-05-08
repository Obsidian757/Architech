"""Unit tests for utils.rss_feed_parser — pure-logic, no network."""

from __future__ import annotations

import sys
import types

# `feedparser` is only used by get_feed_data; stub it so the pure-logic
# helpers can be imported without the full dependency installed.
if "feedparser" not in sys.modules:
    sys.modules["feedparser"] = types.ModuleType("feedparser")

from utils.rss_feed_parser import get_hash, parse_feed_entries  # noqa: E402


def test_get_hash_empty_input_is_deterministic():
    assert get_hash([]) == get_hash([])


def test_get_hash_changes_with_content():
    a = get_hash([{"id": "1", "title": "A", "published_date": "x"}])
    b = get_hash([{"id": "1", "title": "B", "published_date": "x"}])
    assert a != b


def test_get_hash_is_order_dependent():
    e1 = {"id": "1", "title": "A", "published_date": "x"}
    e2 = {"id": "2", "title": "B", "published_date": "y"}
    assert get_hash([e1, e2]) != get_hash([e2, e1])


def test_get_hash_handles_missing_keys():
    assert get_hash([{}]) == get_hash([{}])


def test_parse_feed_entries_uses_content_when_present():
    entries = [{"title": "T", "link": "L", "content": "BODY"}]
    parsed = parse_feed_entries(entries)
    assert parsed[0]["content"] == "BODY"


def test_parse_feed_entries_falls_back_to_description():
    entries = [{"title": "T", "link": "L", "description": "DESC"}]
    parsed = parse_feed_entries(entries)
    assert parsed[0]["content"] == "DESC"


def test_parse_feed_entries_published_date_priority():
    """published > updated > pubDate > created."""
    cases = [
        ({"published": "P", "updated": "U", "pubDate": "PD", "created": "C"}, "P"),
        ({"updated": "U", "pubDate": "PD", "created": "C"}, "U"),
        ({"pubDate": "PD", "created": "C"}, "PD"),
        ({"created": "C"}, "C"),
    ]
    for keys, expected in cases:
        parsed = parse_feed_entries([{"title": "T", "link": "L", **keys}])
        assert parsed[0]["published_date"] == expected


def test_parse_feed_entries_published_date_defaults_to_now_when_absent():
    parsed = parse_feed_entries([{"title": "T", "link": "L"}])
    assert parsed[0]["published_date"]  # non-empty (current ISO timestamp)


def test_parse_feed_entries_entry_id_falls_back_to_link():
    parsed = parse_feed_entries([{"title": "T", "link": "https://x/1"}])
    assert parsed[0]["entry_id"] == "https://x/1"


def test_parse_feed_entries_entry_id_uses_id_when_present():
    parsed = parse_feed_entries([{"id": "GUID-1", "title": "T", "link": "https://x/1"}])
    assert parsed[0]["entry_id"] == "GUID-1"


def test_parse_feed_entries_preserves_required_shape():
    parsed = parse_feed_entries([{}])
    assert set(parsed[0].keys()) == {
        "title", "link", "summary", "content", "published_date", "entry_id",
    }


def test_parse_feed_entries_handles_empty_list():
    assert parse_feed_entries([]) == []
