# CLAUDE.md - AI Assistant Guide for Awesome LLM Apps

## Project Overview

**Awesome LLM Apps** is a curated monorepo of 100+ production-ready LLM application examples built with RAG, AI Agents, Multi-agent Teams, MCP (Model Context Protocol), Voice Agents, and more. Each sub-project is a standalone application demonstrating a specific LLM pattern or use case.

- **Repository:** [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- **License:** Apache 2.0
- **Primary Language:** Python (with TypeScript/Next.js for select frontends)

## Repository Structure

```
├── starter_ai_agents/              # Beginner-friendly single agents (~18 projects)
├── advanced_ai_agents/
│   ├── single_agent_apps/          # Complex single-agent apps (~17 projects)
│   ├── autonomous_game_playing_agent_apps/  # Game-playing agents (3 projects)
│   └── multi_agent_apps/
│       └── agent_teams/            # Multi-agent team orchestrations (~13 projects)
├── rag_tutorials/                  # RAG implementations (~20 projects)
├── advanced_llm_apps/
│   ├── chat_with_X_tutorials/      # Chat interfaces for data sources (7 projects)
│   ├── llm_apps_with_memory_tutorials/  # Stateful conversations (6 projects)
│   └── llm_finetuning_tutorials/   # Model fine-tuning (2 projects)
├── mcp_ai_agents/                  # Model Context Protocol agents (6 projects)
├── voice_ai_agents/                # Voice-based AI agents (3 projects)
├── ai_agent_framework_crash_course/
│   ├── google_adk_crash_course/    # Google Agent Development Kit tutorials
│   └── openai_sdk_crash_course/    # OpenAI Agents SDK tutorials
├── docs/                           # Banner images and documentation assets
├── .github/workflows/claude.yml    # Claude PR Assistant CI workflow
└── README.md                       # Main project index
```

## Tech Stack

### Python (primary)
- **Agent Frameworks:** Agno, OpenAI Agents SDK, Google ADK, CrewAI, Agency-Swarm
- **LLM Providers:** OpenAI, Anthropic Claude, Google Gemini, xAI Grok, Ollama (local), Cohere, Deepseek
- **Web UI:** Streamlit (most projects)
- **API Framework:** FastAPI + Uvicorn (complex projects)
- **Vector DBs:** Qdrant (for RAG projects)
- **Memory:** mem0ai
- **Data:** pandas, numpy, DuckDB
- **Package Management:** pip with `requirements.txt` per project; `pyproject.toml` for complex projects

### JavaScript/TypeScript (select frontends)
- **Framework:** Next.js 15 with React 19
- **Styling:** Tailwind CSS v4
- **Package Manager:** pnpm 9.x
- **UI Components:** Radix UI, react-hook-form, zod

## Development Workflow

### Running a Python project
```bash
cd <project_directory>
pip install -r requirements.txt
# Most projects use Streamlit:
streamlit run <main_file>.py
# FastAPI projects:
uvicorn main:app --reload
# Google ADK projects:
adk web
```

### Running a Next.js frontend
```bash
cd <project_directory>
pnpm install
pnpm dev
```

### Environment Variables
- Most projects require API keys (OpenAI, Anthropic, Google, etc.)
- Look for `.env.example` files in individual project directories
- Never commit `.env` files or API keys

## Key Conventions

### Project Structure Pattern
Each sub-project is self-contained and follows this pattern:
1. **README.md** - Description, features, setup instructions, API key requirements
2. **requirements.txt** - Python dependencies
3. **Main application file** - Usually a single `.py` file for simple projects
4. **.env.example** - Template for required environment variables (when applicable)

### Naming Conventions
- Directory names: `snake_case` prefixed with `ai_` (e.g., `ai_travel_agent/`, `ai_deep_research_agent/`)
- Python files: `snake_case.py`
- Agent team directories include `_agent_team` suffix
- Local variants include `local_` prefix (e.g., `local_ai_legal_agent_team/`)

### Code Style
- Python projects do not enforce a centralized linter or formatter
- Individual projects follow standard Python conventions
- Next.js projects use ESLint with Next.js defaults

### Adding a New Project
1. Create a directory under the appropriate category folder
2. Follow the `ai_<descriptive_name>_agent/` naming convention
3. Include a `README.md` with description, features, prerequisites, and setup steps
4. Include a `requirements.txt` listing all Python dependencies
5. Add `.env.example` if the project needs API keys
6. Update the root `README.md` to list the new project

## CI/CD

The repository uses a GitHub Actions workflow (`.github/workflows/claude.yml`) for a Claude PR Assistant that responds to `@claude` mentions in issues and PR comments. It does not run tests or builds automatically since each sub-project is independent.

## Important Notes for AI Assistants

- **Independent projects:** Each sub-directory is a standalone app. Changes to one project should not affect others.
- **No global test suite:** There is no repo-wide test runner. Testing is manual per project.
- **No monorepo tooling:** No workspace manager (nx, turborepo, etc.) ties projects together.
- **Dependency isolation:** Each project manages its own `requirements.txt`. Do not create shared dependency files.
- **Minimal .gitignore:** Only `.DS_Store` is ignored globally. Individual projects may have their own ignores.
- **README is the index:** The root `README.md` serves as the master catalog of all projects. Keep it updated when adding/removing projects.
- **API keys are required:** Nearly every project needs at least one LLM provider API key. Never hardcode secrets.
- **Python version:** Newer projects target Python 3.12+; older ones work with Python 3.8+.
