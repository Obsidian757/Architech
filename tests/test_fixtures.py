"""Sanity tests for the shared fixtures in `tests/conftest.py`.

Without these, broken fixtures could silently make every downstream test pass.
"""

from __future__ import annotations

import json


def test_mock_openai_client_chat_completion(mock_openai_client):
    response = mock_openai_client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": "hi"}]
    )
    assert response.choices[0].message.content
    assert response.choices[0].finish_reason == "stop"
    payload = json.loads(response.choices[0].message.content)
    assert "script" in payload


def test_mock_openai_client_embeddings(mock_openai_client):
    response = mock_openai_client.embeddings.create(
        input="hello", model="text-embedding-3-small"
    )
    assert len(response.data[0].embedding) == 1536


def test_mock_openai_factory_custom_content(mock_openai_factory):
    client = mock_openai_factory(chat_content="custom!", embedding=[0.5, 0.5])
    chat = client.chat.completions.create(model="x", messages=[])
    emb = client.embeddings.create(input="x", model="x")
    assert chat.choices[0].message.content == "custom!"
    assert emb.data[0].embedding == [0.5, 0.5]


def test_mock_anthropic_client(mock_anthropic_client):
    msg = mock_anthropic_client.messages.create(
        model="claude-sonnet-4-6", max_tokens=10, messages=[{"role": "user", "content": "hi"}]
    )
    assert msg.content[0].text == "ok"
    assert msg.stop_reason == "end_turn"


def test_mock_gemini_model(mock_gemini_model):
    response = mock_gemini_model.generate_content("hello")
    assert response.text == "ok"


def test_seeded_sqlite_db(seeded_sqlite_db):
    import sqlite3

    with sqlite3.connect(seeded_sqlite_db) as conn:
        rows = conn.execute("SELECT name FROM widgets ORDER BY id").fetchall()
    assert [r[0] for r in rows] == ["alpha", "beta", "gamma"]


def test_isolated_cwd_changes_directory(isolated_cwd):
    from pathlib import Path

    assert Path.cwd() == isolated_cwd


def test_stub_env_sets_variables(stub_env, monkeypatch):
    import os

    stub_env({"FOO": "1", "BAR": "two"})
    assert os.environ["FOO"] == "1"
    assert os.environ["BAR"] == "two"
