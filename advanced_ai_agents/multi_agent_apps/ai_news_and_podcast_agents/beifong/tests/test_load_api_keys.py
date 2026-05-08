"""Unit tests for utils.load_api_keys.

The helper reads `.env` from the *current* working directory, then falls back
to process env. We validate both paths and confirm an unknown key returns None."""

from __future__ import annotations

import importlib

import pytest


def test_returns_value_from_env(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-from-env")
    from utils.load_api_keys import load_api_key
    assert load_api_key() == "sk-from-env"


def test_returns_none_for_unknown_key(monkeypatch):
    monkeypatch.delenv("DOES_NOT_EXIST", raising=False)
    from utils.load_api_keys import load_api_key
    assert load_api_key("DOES_NOT_EXIST") is None


def test_supports_custom_key_name(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-x")
    from utils.load_api_keys import load_api_key
    assert load_api_key("ANTHROPIC_API_KEY") == "sk-ant-x"


def test_loads_from_dotenv_in_cwd(tmp_path, monkeypatch):
    monkeypatch.delenv("MY_TOKEN", raising=False)
    (tmp_path / ".env").write_text("MY_TOKEN=from-dotenv\n")
    monkeypatch.chdir(tmp_path)

    # Reload to bypass the module-level dotenv cache state.
    import utils.load_api_keys as mod
    importlib.reload(mod)
    assert mod.load_api_key("MY_TOKEN") == "from-dotenv"
