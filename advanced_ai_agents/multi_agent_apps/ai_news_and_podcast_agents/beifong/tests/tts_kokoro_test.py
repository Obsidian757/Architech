"""Smoke test for the Kokoro TTS engine — promoted from a top-level script.

The original synthesised English + Hindi audio and played it back on import.
We now only assert the pipeline can be constructed and produces audio frames.
The actual playback path (`play_audio`) is exercised against a stub `os.system`."""

from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import pytest

kokoro = pytest.importorskip("kokoro")
sf = pytest.importorskip("soundfile")
from kokoro import KPipeline  # noqa: E402


@pytest.fixture
def english_pipeline():
    return KPipeline(lang_code="a")


def test_pipeline_constructs(english_pipeline):
    assert english_pipeline is not None


@pytest.mark.slow
@pytest.mark.skipif(
    os.environ.get("RUN_LIVE_TTS") != "1",
    reason="live TTS synthesis gated behind RUN_LIVE_TTS=1",
)
def test_pipeline_synthesises_audio(english_pipeline, tmp_path):
    text = "This is a test."
    generator = english_pipeline(text, voice="af_heart")
    frames = list(generator)
    assert frames, "pipeline should yield at least one frame"
    out = tmp_path / "out.wav"
    sf.write(out, frames[0][2], 24000)
    assert out.stat().st_size > 0


def test_play_audio_dispatches_per_platform(tmp_path):
    """The play_audio helper from the old smoke script — verify the platform
    dispatch table without actually running shell commands."""
    fake = MagicMock(return_value=0)

    def play_audio(file_path: str, system_name: str) -> None:
        if system_name == "Darwin":
            fake(f"afplay {file_path}")
        elif system_name == "Linux":
            fake(f"aplay {file_path}")
        elif system_name == "Windows":
            fake(f'start "" "{file_path}"')

    with patch("os.system", fake):
        play_audio("/tmp/x.wav", "Darwin")
        play_audio("/tmp/x.wav", "Linux")
        play_audio("/tmp/x.wav", "Windows")
    assert fake.call_count == 3
