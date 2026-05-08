"""Real tests for the FAISS-backed article search.

Replaces the earlier file (a CLI script with no asserts that required a live
OpenAI key + a populated FAISS index on disk).

These tests target the production `tools/embedding_search.py` helpers. The
top-level module imports `agno`, `faiss`, `openai` and `numpy`; we
`importorskip` so the file is skipped (not failed) in environments that don't
have those dependencies installed."""

from __future__ import annotations

import sqlite3
import sys
import types
from unittest.mock import MagicMock

import pytest

np = pytest.importorskip("numpy")
faiss = pytest.importorskip("faiss")

# `agno` is heavy and only used as a type annotation in the module. Stub it
# before import so we don't require the real dependency in CI.
if "agno" not in sys.modules:
    agno_module = types.ModuleType("agno")
    agno_agent_module = types.ModuleType("agno.agent")
    agno_agent_module.Agent = type("Agent", (), {})
    agno_module.agent = agno_agent_module
    sys.modules["agno"] = agno_module
    sys.modules["agno.agent"] = agno_agent_module

# Same for openai — only the OpenAI symbol is used and we'll monkeypatch it.
if "openai" not in sys.modules:
    openai_module = types.ModuleType("openai")
    openai_module.OpenAI = MagicMock()
    sys.modules["openai"] = openai_module


def _seed_articles(db_path: str, count: int = 5) -> None:
    conn = sqlite3.connect(db_path)
    for i in range(1, count + 1):
        conn.execute(
            "INSERT INTO crawled_articles (id, title, url, published_date, summary, content, source_id, feed_id) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (i, f"Article {i}", f"https://example.com/{i}", f"2024-01-0{i}",
             f"Summary {i}", f"Content {i}", 1, 1),
        )
    conn.commit()
    conn.close()


def test_get_article_details_handles_empty_id_list(tracking_db):
    from tools.embedding_search import get_article_details
    assert get_article_details(tracking_db, []) == []


def test_get_article_details_returns_seeded_rows(tracking_db):
    _seed_articles(tracking_db, count=3)
    from tools.embedding_search import get_article_details
    rows = get_article_details(tracking_db, [1, 2])
    assert len(rows) == 2
    titles = sorted(r["title"] for r in rows)
    assert titles == ["Article 1", "Article 2"]


def test_load_faiss_index_returns_error_when_missing(tmp_path):
    from tools.embedding_search import load_faiss_index
    index, err = load_faiss_index(str(tmp_path / "nope.faiss"))
    assert index is None
    assert err and "not found" in err


def test_load_id_mapping_returns_error_when_missing(tmp_path):
    from tools.embedding_search import load_id_mapping
    mapping, err = load_id_mapping(str(tmp_path / "nope.npy"))
    assert mapping is None
    assert err and "not found" in err


def test_load_faiss_index_round_trip(tmp_path):
    from tools.embedding_search import load_faiss_index
    index = faiss.IndexFlatL2(8)
    index.add(np.zeros((3, 8), dtype="float32"))
    index_path = tmp_path / "round.faiss"
    faiss.write_index(index, str(index_path))
    loaded, err = load_faiss_index(str(index_path))
    assert err is None
    assert loaded.ntotal == 3


def test_load_id_mapping_round_trip(tmp_path):
    from tools.embedding_search import load_id_mapping
    mapping_path = tmp_path / "ids.npy"
    np.save(mapping_path, np.array([10, 20, 30], dtype=np.int64))
    loaded, err = load_id_mapping(str(mapping_path))
    assert err is None
    assert loaded == [10, 20, 30]


def test_generate_query_embedding_returns_error_without_api_key(monkeypatch):
    from tools import embedding_search
    monkeypatch.setattr(embedding_search, "load_api_key", lambda *_: None)
    vector, err = embedding_search.generate_query_embedding("hello")
    assert vector is None
    assert "API key" in err


def test_generate_query_embedding_uses_client(monkeypatch):
    from tools import embedding_search
    monkeypatch.setattr(embedding_search, "load_api_key", lambda *_: "sk-test")

    fake_response = MagicMock()
    fake_response.data = [MagicMock(embedding=[0.1, 0.2, 0.3])]
    fake_client = MagicMock()
    fake_client.embeddings.create.return_value = fake_response

    monkeypatch.setattr(embedding_search, "OpenAI", lambda api_key=None: fake_client)
    vector, err = embedding_search.generate_query_embedding("hello")
    assert err is None
    assert vector == [0.1, 0.2, 0.3]
    fake_client.embeddings.create.assert_called_once()


def test_generate_query_embedding_swallows_provider_error(monkeypatch):
    from tools import embedding_search
    monkeypatch.setattr(embedding_search, "load_api_key", lambda *_: "sk-test")

    failing_client = MagicMock()
    failing_client.embeddings.create.side_effect = RuntimeError("api down")
    monkeypatch.setattr(embedding_search, "OpenAI", lambda api_key=None: failing_client)

    vector, err = embedding_search.generate_query_embedding("hello")
    assert vector is None
    assert "api down" in err
