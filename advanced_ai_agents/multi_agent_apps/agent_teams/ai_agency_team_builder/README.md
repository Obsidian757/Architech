# AI Agency Team Builder

Compose custom multi-agent teams from 160+ specialized AI agent personalities and coordinate them on any task through a chat interface.

## What it does

This Streamlit app loads every personality profile from `agency-agents/` (engineering, design, marketing, sales, product, testing, etc.) and lets you:

1. **Browse** agents by division with searchable cards
2. **Select** 2-6 agents to compose a custom team
3. **Chat** with the assembled team — an Agno `Team` in coordinate mode delegates to specialists and synthesizes their responses

## How it works

- `agent_parser.py` — Parses each markdown personality file (YAML frontmatter + structured body) into an `AgentConfig` dataclass. Cached per session via `@st.cache_data`.
- `ai_agency_team_builder.py` — Streamlit UI with two phases (browse → chat). Each selected personality becomes an Agno `Agent` with the full markdown body as its system instructions. The team uses `mode="coordinate"` with `enable_agentic_context` and `share_member_interactions` so members see each other's work.

## Run it

```bash
pip install -r requirements.txt
streamlit run ai_agency_team_builder.py
```

Enter your OpenAI API key in the sidebar, pick a division, add 2-6 agents to your team, and click **Start Chat**.

## Example teams

- **Ship an MVP**: Rapid Prototyper + Backend Architect + Frontend Developer + Code Reviewer
- **Launch a product**: Product Manager + Growth Hacker + Content Creator + PPC Strategist
- **Audit a codebase**: Code Reviewer + Security Engineer + Database Optimizer + Testing API Tester
