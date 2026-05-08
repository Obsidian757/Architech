"""Shared pytest fixtures for the awesome-llm-apps test suite.

Fixtures here are intentionally provider-agnostic so subproject tests can opt in
without pulling the SDK they're mocking. Each mock returns a `MagicMock` shaped
like the SDK's response object — tests assert on what the *caller* does with
the response, not on the canned content itself.
"""

from __future__ import annotations

import json
import sqlite3
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def tmp_sqlite_db(tmp_path: Path) -> Path:
    """An empty SQLite file that callers seed with their own schema."""
    db_path = tmp_path / "test.db"
    db_path.touch()
    return db_path


@pytest.fixture
def sqlite_factory(tmp_path: Path) -> Callable[[str], Path]:
    """Returns a factory for creating named temp SQLite files."""

    def _make(name: str = "test.db") -> Path:
        path = tmp_path / name
        path.touch()
        return path

    return _make


@pytest.fixture
def seeded_sqlite_db(tmp_sqlite_db: Path) -> Path:
    """A SQLite DB pre-seeded with a tiny `widgets` table for connection tests."""
    with sqlite3.connect(tmp_sqlite_db) as conn:
        conn.execute("CREATE TABLE widgets (id INTEGER PRIMARY KEY, name TEXT, qty INTEGER)")
        conn.executemany(
            "INSERT INTO widgets (name, qty) VALUES (?, ?)",
            [("alpha", 1), ("beta", 2), ("gamma", 3)],
        )
        conn.commit()
    return tmp_sqlite_db


def _make_chat_completion(content: str = "ok") -> MagicMock:
    completion = MagicMock()
    completion.choices = [MagicMock()]
    completion.choices[0].message = MagicMock()
    completion.choices[0].message.content = content
    completion.choices[0].finish_reason = "stop"
    completion.model = "mock-model"
    completion.usage = MagicMock(prompt_tokens=1, completion_tokens=1, total_tokens=2)
    return completion


def _make_embedding_response(vector: list[float] | None = None) -> MagicMock:
    response = MagicMock()
    response.data = [MagicMock()]
    response.data[0].embedding = vector if vector is not None else [0.1] * 1536
    response.model = "text-embedding-3-small"
    response.usage = MagicMock(prompt_tokens=1, total_tokens=1)
    return response


@pytest.fixture
def mock_openai_client() -> MagicMock:
    """A MagicMock shaped like `openai.OpenAI()` — chat + embeddings preconfigured."""
    client = MagicMock()
    client.chat.completions.create.return_value = _make_chat_completion(
        content=json.dumps({"script": []})
    )
    client.embeddings.create.return_value = _make_embedding_response()
    return client


@pytest.fixture
def mock_openai_factory() -> Callable[..., MagicMock]:
    """Build an OpenAI client mock with a specific chat content / embedding vector."""

    def _build(chat_content: str = "ok", embedding: list[float] | None = None) -> MagicMock:
        client = MagicMock()
        client.chat.completions.create.return_value = _make_chat_completion(chat_content)
        client.embeddings.create.return_value = _make_embedding_response(embedding)
        return client

    return _build


@pytest.fixture
def mock_anthropic_client() -> MagicMock:
    """Mock shaped like `anthropic.Anthropic()`."""
    client = MagicMock()
    message = MagicMock()
    message.content = [MagicMock(text="ok", type="text")]
    message.stop_reason = "end_turn"
    message.usage = MagicMock(input_tokens=1, output_tokens=1)
    client.messages.create.return_value = message
    return client


@pytest.fixture
def mock_gemini_model() -> MagicMock:
    """Mock shaped like `google.generativeai.GenerativeModel()`."""
    model = MagicMock()
    response = MagicMock()
    response.text = "ok"
    response.candidates = [MagicMock(finish_reason="STOP")]
    model.generate_content.return_value = response
    return model


@pytest.fixture
def stub_env(monkeypatch: pytest.MonkeyPatch) -> Callable[[dict[str, str]], None]:
    """Set a batch of environment variables for the duration of the test."""

    def _apply(values: dict[str, str]) -> None:
        for key, val in values.items():
            monkeypatch.setenv(key, val)

    return _apply


@pytest.fixture
def isolated_cwd(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Run the test inside an empty tmp dir so .env / relative paths don't leak."""
    monkeypatch.chdir(tmp_path)
    return tmp_path


@pytest.fixture
def captured_calls() -> dict[str, list[Any]]:
    """A simple dict-of-lists for tests to record side-effects from injected fakes."""
    return {}


def patch_module_attr(monkeypatch: pytest.MonkeyPatch, dotted: str, value: Any) -> None:
    """Helper used by subproject tests; kept here so it stays consistent."""
    module_path, _, attr = dotted.rpartition(".")
    import importlib

    module = importlib.import_module(module_path)
    monkeypatch.setattr(module, attr, value)


@pytest.fixture
def patch_attr(monkeypatch: pytest.MonkeyPatch) -> Callable[[str, Any], None]:
    def _apply(dotted: str, value: Any) -> Iterator[None]:
        patch_module_attr(monkeypatch, dotted, value)

    return _apply
