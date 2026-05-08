"""Smoke test for the browser-use tool — promoted from a top-level script.

The original ran a real browser session against a live LLM whenever imported.
Tests now: (a) verify Agent construction, (b) gate the live browser run behind
explicit env opt-in. CI will skip the live test by default."""

from __future__ import annotations

import asyncio
import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

pytest.importorskip("browser_use")
pytest.importorskip("langchain_openai")
from browser_use import Agent  # noqa: E402
from langchain_openai import ChatOpenAI  # noqa: E402


def test_browseruse_agent_constructs():
    llm = ChatOpenAI(model="gpt-4o", api_key="sk-test")
    agent = Agent(task="Compare the price of gpt-4o and DeepSeek-V3", llm=llm)
    assert agent is not None


def test_browseruse_agent_run_is_awaitable():
    llm = ChatOpenAI(model="gpt-4o", api_key="sk-test")
    agent = Agent(task="noop", llm=llm)
    fake_result = MagicMock(final_result=lambda: "mocked")
    with patch.object(agent, "run", new=AsyncMock(return_value=fake_result)):
        result = asyncio.run(agent.run())
    assert result.final_result() == "mocked"


@pytest.mark.requires_api_key
@pytest.mark.skipif(
    os.environ.get("RUN_LIVE_BROWSER") != "1",
    reason="live browser test gated behind RUN_LIVE_BROWSER=1",
)
def test_browseruse_live_run():
    llm = ChatOpenAI(model="gpt-4o")
    agent = Agent(task="Compare the price of gpt-4o and DeepSeek-V3", llm=llm)
    result = asyncio.run(agent.run())
    assert result is not None
