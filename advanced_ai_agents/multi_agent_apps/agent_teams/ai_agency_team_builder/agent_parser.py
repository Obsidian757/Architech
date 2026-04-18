"""Parse agency-agents markdown personality files into structured configs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


SKIP_FILES = {
    "README.md",
    "CONTRIBUTING.md",
    "CONTRIBUTING_zh-CN.md",
    "LICENSE",
    "EXECUTIVE-BRIEF.md",
    "QUICKSTART.md",
}

SKIP_DIVISIONS = {
    "examples",
    "scripts",
    "integrations",
    "coordination",
    "playbooks",
    "runbooks",
}


@dataclass(frozen=True)
class AgentConfig:
    name: str
    description: str
    color: str
    emoji: str
    vibe: str
    division: str
    file_path: str
    personality: str

    @property
    def display_division(self) -> str:
        return self.division.replace("-", " ").title()


def _split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        data = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}, text
    if not isinstance(data, dict):
        return {}, text
    return data, parts[2].lstrip("\n")


def parse_agent_file(file_path: Path) -> AgentConfig | None:
    try:
        text = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    frontmatter, body = _split_frontmatter(text)
    name = frontmatter.get("name")
    if not name:
        return None

    division = file_path.parent.name
    if division in SKIP_DIVISIONS:
        return None

    return AgentConfig(
        name=str(name),
        description=str(frontmatter.get("description", "")),
        color=str(frontmatter.get("color", "gray")),
        emoji=str(frontmatter.get("emoji", "🤖")),
        vibe=str(frontmatter.get("vibe", "")),
        division=division,
        file_path=str(file_path),
        personality=body.strip(),
    )


def load_all_agents(agents_dir: Path) -> dict[str, list[AgentConfig]]:
    """Walk agents_dir and return {division: [AgentConfig, ...]} sorted by name."""
    agents_by_division: dict[str, list[AgentConfig]] = {}

    for md_path in sorted(agents_dir.rglob("*.md")):
        if md_path.name in SKIP_FILES:
            continue
        if any(part in SKIP_DIVISIONS for part in md_path.relative_to(agents_dir).parts[:-1]):
            continue

        config = parse_agent_file(md_path)
        if config is None:
            continue
        agents_by_division.setdefault(config.division, []).append(config)

    for division in agents_by_division:
        agents_by_division[division].sort(key=lambda c: c.name.lower())

    return dict(sorted(agents_by_division.items()))
