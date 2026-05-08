"""Unit tests for utils.translate_podcast.translate_script.

Validates: language passthrough, list-vs-dict response unwrapping, length
mismatch raising, missing-key raising, and the OpenAI client wiring."""

from __future__ import annotations

import json
import sys
import types
from unittest.mock import MagicMock

import pytest

# `openai` is optional in CI; stub the symbol the module imports.
if "openai" not in sys.modules:
    openai_module = types.ModuleType("openai")
    openai_module.OpenAI = MagicMock()
    sys.modules["openai"] = openai_module

from utils import translate_podcast  # noqa: E402


SCRIPT = [
    {"text": "Hello", "speaker": "host"},
    {"text": "World", "speaker": "guest"},
]


def _mock_openai_returning(content: str) -> MagicMock:
    response = MagicMock()
    response.choices = [MagicMock()]
    response.choices[0].message = MagicMock(content=content)
    client = MagicMock()
    client.chat.completions.create.return_value = response
    return client


def test_returns_input_unchanged_when_lang_code_is_passthrough():
    """lang_code='b' maps to None in LANG_CODE_TO_NAME → no translation."""
    out = translate_podcast.translate_script(SCRIPT.copy(), lang_code="b")
    assert out == SCRIPT


def test_unknown_lang_code_returns_input():
    out = translate_podcast.translate_script(SCRIPT.copy(), lang_code="zz")
    assert out == SCRIPT


def test_raises_when_api_key_missing(monkeypatch):
    monkeypatch.setattr(translate_podcast, "load_api_key", lambda *_: None)
    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        translate_podcast.translate_script(SCRIPT.copy(), lang_code="es")


def test_unwraps_script_key_in_response(monkeypatch):
    monkeypatch.setattr(translate_podcast, "load_api_key", lambda *_: "sk-test")
    payload = {"script": [
        {"text": "Hola", "speaker": "host"},
        {"text": "Mundo", "speaker": "guest"},
    ]}
    monkeypatch.setattr(
        translate_podcast, "OpenAI", lambda api_key=None: _mock_openai_returning(json.dumps(payload))
    )
    out = translate_podcast.translate_script(SCRIPT.copy(), lang_code="es")
    assert out == payload["script"]


def test_accepts_bare_list_response(monkeypatch):
    monkeypatch.setattr(translate_podcast, "load_api_key", lambda *_: "sk-test")
    bare = [
        {"text": "Hola", "speaker": "host"},
        {"text": "Mundo", "speaker": "guest"},
    ]
    monkeypatch.setattr(
        translate_podcast, "OpenAI", lambda api_key=None: _mock_openai_returning(json.dumps(bare))
    )
    out = translate_podcast.translate_script(SCRIPT.copy(), lang_code="es")
    assert out == bare


def test_raises_on_length_mismatch(monkeypatch):
    monkeypatch.setattr(translate_podcast, "load_api_key", lambda *_: "sk-test")
    payload = {"script": [{"text": "Hola", "speaker": "host"}]}  # only 1 entry, expected 2
    monkeypatch.setattr(
        translate_podcast, "OpenAI", lambda api_key=None: _mock_openai_returning(json.dumps(payload))
    )
    with pytest.raises(ValueError, match="expected 2"):
        translate_podcast.translate_script(SCRIPT.copy(), lang_code="es")


def test_raises_when_response_is_not_a_list(monkeypatch):
    monkeypatch.setattr(translate_podcast, "load_api_key", lambda *_: "sk-test")
    bad = {"unexpected": "shape"}
    monkeypatch.setattr(
        translate_podcast, "OpenAI", lambda api_key=None: _mock_openai_returning(json.dumps(bad))
    )
    with pytest.raises(ValueError, match="not a list"):
        translate_podcast.translate_script(SCRIPT.copy(), lang_code="es")


def test_target_language_name_appears_in_prompt(monkeypatch):
    monkeypatch.setattr(translate_podcast, "load_api_key", lambda *_: "sk-test")
    payload = {"script": [
        {"text": "x", "speaker": "host"},
        {"text": "y", "speaker": "guest"},
    ]}
    captured: dict = {}

    def fake_openai(api_key=None):
        client = MagicMock()
        def create(**kwargs):
            captured["kwargs"] = kwargs
            response = MagicMock()
            response.choices = [MagicMock(message=MagicMock(content=json.dumps(payload)))]
            return response
        client.chat.completions.create.side_effect = create
        return client

    monkeypatch.setattr(translate_podcast, "OpenAI", fake_openai)
    translate_podcast.translate_script(SCRIPT.copy(), lang_code="ja")
    user_prompt = captured["kwargs"]["messages"][1]["content"]
    assert "Japanese" in user_prompt
