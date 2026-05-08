"""Smoke test for the Agno agent — promoted from a top-level script.

The original file ran a real LLM call against `gpt-4o-mini` whenever the file
was imported. That made it impossible to use as a pytest module. We now gate
the live call behind `--run-live` and `OPENAI_API_KEY`, and add a
construction-only test that validates the Agent wiring without making any
network calls."""

from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import pytest

agno = pytest.importorskip("agno")
from agno.agent import Agent  # noqa: E402
from agno.models.openai import OpenAIChat  # noqa: E402


def test_agent_constructs_with_openai_chat_model():
    agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))
    assert agent.model is not None
    assert agent.model.id == "gpt-4o-mini"


def test_agent_run_invokes_model(monkeypatch):
    """Agent.run should delegate to its model — verified with a mock."""
    agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))
    fake_response = MagicMock()
    fake_response.content = "mock story"
    with patch.object(agent, "run", return_value=fake_response) as mocked:
        result = agent.run("Tell me a 5 second short story about a robot")
    mocked.assert_called_once()
    assert result.content == "mock story"


@pytest.mark.requires_api_key
@pytest.mark.skipif(
    not os.environ.get("OPENAI_API_KEY")
    or os.environ.get("OPENAI_API_KEY", "").startswith("sk-test"),
    reason="needs a real OPENAI_API_KEY",
)
def test_agent_live_short_story():
    agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))
    response = agent.run("Reply with exactly the word: pong")
    assert response is not None
    assert response.content
