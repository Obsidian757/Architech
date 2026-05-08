"""Lightweight repo-wide smoke tests.

Catches the cheapest, highest-value regressions for a tutorial repo:
1. Every demo subproject still has a single canonical entrypoint .py file.
2. Every requirements.txt parses (no broken syntax) and pins or floats sanely.
3. .env / credentials are not committed.

These tests are intentionally tolerant — they run without installing any
demo's dependencies. Demo-specific behaviour belongs in per-subproject tests."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
DEMO_SECTIONS = [
    "advanced_llm_apps",
    "ai_agent_framework_crash_course",
    "mcp_ai_agents",
    "rag_tutorials",
    "starter_ai_agents",
    "voice_ai_agents",
]


def _iter_subprojects():
    """Yield (section, subproject_dir) for each leaf demo project."""
    for section in DEMO_SECTIONS:
        section_dir = REPO_ROOT / section
        if not section_dir.is_dir():
            continue
        for child in sorted(section_dir.iterdir()):
            if not child.is_dir() or child.name.startswith("."):
                continue
            yield section, child


def _all_requirements_files():
    return sorted(REPO_ROOT.rglob("requirements*.txt"))


JS_DEMO_MARKERS = {"package.json", "index.html"}


@pytest.mark.parametrize(
    "section,subproject",
    list(_iter_subprojects()),
    ids=lambda v: v.name if isinstance(v, Path) else v,
)
def test_subproject_has_an_entrypoint(section, subproject):
    """Each demo dir should ship at least one runnable file (Python or JS)."""
    has_py = any(subproject.rglob("*.py"))
    has_js = any((subproject / m).exists() for m in JS_DEMO_MARKERS)
    assert has_py or has_js, f"{section}/{subproject.name} has no entrypoint"


REQ_LINE = re.compile(
    r"^\s*(?:#.*)?$"                                # comment / blank
    r"|^\s*-r\s+\S+.*$"                             # -r other.txt
    r"|^\s*--?[a-z-]+(?:\s+\S+)?\s*$"               # CLI flags
    r"|^\s*[\"']?[A-Za-z0-9_.\-]+(?:\[[^\]]+\])?"   # [optionally-quoted] package[extra]
    r"(?:\s*[=<>!~]+\s*[^\s;#\"']+(?:\s*,\s*[=<>!~]+\s*[^\s;#\"']+)*)?"  # version specs
    r"[\"']?(?:\s*;\s*.+)?\s*(?:#.*)?$"             # closing quote / marker / comment
    r"|^\s*git\+\S+\s*(?:#.*)?$"                    # git+https://...
    r"|^\s*\S+@(?:git\+)?\S+\s*(?:#.*)?$"           # name @ git+url
)


@pytest.mark.parametrize("req_file", _all_requirements_files(), ids=lambda p: str(p.relative_to(REPO_ROOT)))
def test_requirements_files_parse(req_file):
    """Every requirements.txt should be syntactically reasonable."""
    text = req_file.read_text(encoding="utf-8", errors="replace")
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        assert REQ_LINE.match(raw), (
            f"{req_file.relative_to(REPO_ROOT)}:{lineno} unparseable line: {raw!r}"
        )


def _env_file_has_real_secret(path: Path) -> bool:
    """A `.env` is a template if every value is empty / quoted-empty / placeholder."""
    placeholder_re = re.compile(r"^\s*[A-Z_][A-Z0-9_]*\s*=\s*([\"']?\s*[\"']?|<.*>|your[_-]?.*|xxx+|changeme)?\s*$", re.IGNORECASE)
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if not placeholder_re.match(line):
            return True
    return False


def test_no_env_files_with_real_secrets():
    """`.env` files holding real values should never be committed.

    Empty templates (`OPENAI_API_KEY=""`) are allowed but still discouraged —
    keep them out of the repo when possible."""
    leaked = [
        p for p in REPO_ROOT.rglob(".env")
        if ".git" not in p.parts and _env_file_has_real_secret(p)
    ]
    assert leaked == [], f".env files with non-empty values: {leaked}"


def test_no_obvious_secret_patterns_in_requirements():
    """Sanity check: a requirements file should not contain a key-looking token."""
    secret_re = re.compile(r"(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})")
    for req in _all_requirements_files():
        text = req.read_text(encoding="utf-8", errors="replace")
        match = secret_re.search(text)
        assert not match, f"possible secret in {req.relative_to(REPO_ROOT)}: {match.group(0)[:8]}…"
