# CLAUDE.md - AI Assistant Guide for Awesome LLM Apps

This document provides comprehensive guidance for AI assistants (like Claude) working with the Awesome LLM Apps repository. It covers codebase structure, development patterns, conventions, and best practices.

## Table of Contents

1. [Repository Overview](#repository-overview)
2. [Directory Structure](#directory-structure)
3. [Development Workflows](#development-workflows)
4. [Agent Frameworks & Patterns](#agent-frameworks--patterns)
5. [File Structure Conventions](#file-structure-conventions)
6. [Code Style & Naming Conventions](#code-style--naming-conventions)
7. [API Key Management](#api-key-management)
8. [Documentation Standards](#documentation-standards)
9. [Dependencies & Package Management](#dependencies--package-management)
10. [Testing & Quality](#testing--quality)
11. [Git & GitHub Workflows](#git--github-workflows)
12. [Creating New Agents](#creating-new-agents)
13. [Common Pitfalls](#common-pitfalls)

---

## Repository Overview

**Awesome LLM Apps** is a curated collection of LLM-powered applications featuring:
- RAG (Retrieval Augmented Generation) systems
- AI Agents (single and multi-agent systems)
- Voice-enabled agents
- MCP (Model Context Protocol) integrations
- Framework tutorials and crash courses

**Key Principles:**
- **Simplicity First**: Focus on practical, runnable examples
- **Educational Value**: Well-documented, easy-to-understand code
- **Framework Diversity**: Support for multiple LLM providers and frameworks
- **Community-Driven**: Open-source contributions welcome

**Primary Maintainer**: Shubham Saboo (@Shubhamsaboo)

---

## Directory Structure

### Main Categories

```
awesome-llm-apps/
├── starter_ai_agents/              # Simple, single-file agents (16 projects)
├── advanced_ai_agents/             # Complex agent implementations
│   ├── single_agent_apps/          # Advanced single agents (15 projects)
│   ├── multi_agent_apps/           # Multi-agent systems (14+ projects)
│   │   └── agent_teams/            # Team-based multi-agent systems
│   └── autonomous_game_playing_agent_apps/  # Gaming agents (3 projects)
├── rag_tutorials/                  # RAG implementations (20+ tutorials)
├── mcp_ai_agents/                  # MCP protocol agents (5+ projects)
├── voice_ai_agents/                # Voice-enabled agents (3 projects)
├── ai_agent_framework_crash_course/ # Framework tutorials
│   ├── google_adk_crash_course/    # Google ADK tutorials
│   └── openai_sdk_crash_course/    # OpenAI SDK tutorials
├── advanced_llm_apps/              # Advanced LLM applications
│   ├── chat_with_X_tutorials/      # Chat with [PDF, GitHub, Gmail, etc.]
│   ├── llm_apps_with_memory_tutorials/  # Memory-enabled apps
│   └── llm_finetuning_tutorials/   # Fine-tuning examples
├── docs/                           # Documentation and assets
│   └── banner/                     # Banner images and sponsors
└── .github/                        # GitHub workflows
    └── workflows/
        └── claude.yml              # Claude PR Assistant workflow
```

### Project Complexity Levels

1. **Starter Agents** (`starter_ai_agents/`)
   - Single Python file (20-200 lines)
   - Basic agent functionality
   - Quick setup and running
   - Example: `xai_finance_agent/xai_finance_agent.py` (~23 lines)

2. **Advanced Single Agents** (`advanced_ai_agents/single_agent_apps/`)
   - Single file or simple multi-file structure
   - Complex logic and integrations
   - 200-500+ lines of code
   - Example: `ai_services_agency/agency.py` (~300+ lines)

3. **Multi-Agent Systems** (`advanced_ai_agents/multi_agent_apps/`)
   - Multiple agent coordination
   - Often includes subdirectories
   - Complex workflows
   - Example: `beifong/` (news and podcast agent with full package structure)

4. **Framework Tutorials** (`ai_agent_framework_crash_course/`)
   - Numbered directories (e.g., `1_starter_agent/`, `2_model_agnostic_agent/`)
   - Progressive learning structure
   - Each tutorial builds on previous concepts

---

## Development Workflows

### Standard Development Flow

1. **Choose the Right Directory**
   - Simple demos → `starter_ai_agents/`
   - Complex single agents → `advanced_ai_agents/single_agent_apps/`
   - Multi-agent systems → `advanced_ai_agents/multi_agent_apps/`
   - RAG systems → `rag_tutorials/`
   - MCP integrations → `mcp_ai_agents/`
   - Voice features → `voice_ai_agents/`

2. **Create Project Structure**
   - Create directory: `ai_{purpose}_agent/`
   - Add required files: `README.md`, `requirements.txt`, `{agent_name}.py`
   - Optional: `.env.example` for complex projects

3. **Implement Agent**
   - Use Agno/Phidata framework (most common)
   - Integrate Streamlit for UI
   - Follow naming conventions (see below)

4. **Document**
   - Write comprehensive README.md
   - Follow standard documentation template
   - Include emojis in titles (matching repo style)

5. **Test Manually**
   - Run via Streamlit: `streamlit run agent.py`
   - Verify API key handling
   - Test core functionality

6. **Commit & Push**
   - Use descriptive commit messages
   - Follow git patterns (see Git & GitHub section)

### Git Branch Patterns

- **Main branch**: `main` (or default branch)
- **Claude branches**: `claude/{feature-description}-{session-id}`
  - Example: `claude/add-claude-documentation-nzz1z`
  - Session ID is appended automatically
  - **CRITICAL**: Branch must start with `claude/` and end with matching session ID for push to succeed

### GitHub Integration

- **Claude PR Assistant**: Automated via `.github/workflows/claude.yml`
- Trigger: Comment `@claude` on issues or PRs
- Permissions: Read access to contents, PRs, and issues

---

## Agent Frameworks & Patterns

### Framework Preference Order

1. **Agno (formerly Phidata)** - **MOST COMMON** (80%+ of projects)
2. OpenAI Agents SDK
3. Google ADK
4. Agency Swarm
5. MCP Agent
6. CrewAI (used in some multi-agent teams)

### 1. Agno/Phidata Pattern (Primary Framework)

**When to Use**: Default choice for new agents unless specific requirements dictate otherwise.

**Basic Structure**:
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
import streamlit as st

# Get API key from user
openai_api_key = st.text_input("Enter OpenAI API Key", type="password")

if openai_api_key:
    # Initialize agent
    agent = Agent(
        name="Agent Name",
        role="Brief role description",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        tools=[DuckDuckGoTools()],
        instructions=[
            "Instruction 1",
            "Instruction 2"
        ],
        markdown=True,
        debug_mode=False,  # Set to True for debugging
        add_datetime_to_context=True,
        show_tool_calls=True
    )

    # Streamlit UI
    st.title("Agent Name")

    query = st.text_area("Enter your query:")

    if st.button("Submit"):
        with st.spinner("Processing..."):
            response = agent.run(query)
            st.markdown(response.content)
```

**AgentOS Pattern** (For multiple agents):
```python
from agno.os import AgentOS
from agno.agent import Agent

# Define multiple agents
agent1 = Agent(name="Agent 1", ...)
agent2 = Agent(name="Agent 2", ...)

# Create AgentOS
agent_os = AgentOS(
    agents=[agent1, agent2],
    name="Multi-Agent System"
)

# Get Streamlit app
app = agent_os.get_app()
```

**Common Agno Tools**:
```python
from agno.tools.duckduckgo import DuckDuckGoTools     # Web search
from agno.tools.yfinance import YFinanceTools         # Financial data
from agno.tools.file import FileTools                 # File operations
from agno.tools.browser import BrowserTools           # Browser automation
from agno.tools.serpapi import SerpApiTools           # Google search
from agno.tools.firecrawl import FirecrawlTools       # Web scraping
```

**Version Requirements**:
```
agno>=2.2.10  # Specify version for compatibility
```

### 2. OpenAI Agents SDK Pattern

**When to Use**: Projects specifically targeting OpenAI's agent framework, swarm patterns, or agent handoffs.

**Basic Structure**:
```python
from agents import Agent, Runner

# Define agent
agent = Agent(
    name="Agent Name",
    instructions="Detailed instructions for the agent",
    tools=[custom_tool],
    model="gpt-4o"
)

# Synchronous execution
result = Runner.run_sync(agent, message="User query")

# Asynchronous execution
result = await Runner.run(agent, message="User query")
```

**Swarm Pattern** (Multiple agents):
```python
from agents import Agent, Swarm

agent1 = Agent(name="Agent 1", ...)
agent2 = Agent(name="Agent 2", ...)

swarm = Swarm(agents=[agent1, agent2])
result = swarm.run("User query")
```

### 3. Google ADK Pattern

**When to Use**: Projects using Google's Gemini models exclusively or Google ADK tutorials.

**Basic Structure**:
```python
from google.adk.agents import LlmAgent

agent = LlmAgent(
    name="agent_name",
    model="gemini-2.5-flash",
    description="Agent description",
    instruction="Detailed instructions"
)

# Execute
response = agent.run("User query")
```

**Environment Setup**:
```bash
# .env.example
GOOGLE_GENAI_USE_VERTEXAI=False
GOOGLE_API_KEY="your-api-key"
```

### 4. Agency Swarm Pattern

**When to Use**: Complex multi-agent coordination, agency structures.

**Basic Structure**:
```python
from agency_swarm import Agent, Agency

# Define agents
agent1 = Agent(
    name="Agent 1",
    description="Agent 1 description",
    instructions="Instructions",
    tools=[ToolClass]
)

agent2 = Agent(
    name="Agent 2",
    description="Agent 2 description",
    instructions="Instructions",
    tools=[AnotherToolClass]
)

# Create agency with communication flows
agency = Agency(
    [
        agent1,           # Entry point
        agent2,
        [agent1, agent2]  # Communication channel: agent1 can talk to agent2
    ],
    async_mode='threading'
)

# Run
result = agency.run("User query")
```

### 5. MCP Agent Pattern

**When to Use**: Model Context Protocol integrations, browser automation, playwright.

**Basic Structure**:
```python
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent

# Create MCP app
app = MCPApp(name="app_name")

# Define agent with MCP servers
agent = Agent(
    name="agent_name",
    instruction="Agent instructions",
    server_names=["playwright"]  # MCP server names
)

app.add_agent(agent)
```

---

## File Structure Conventions

### Required Files for Every Project

1. **README.md** (MANDATORY)
   - Project description
   - Features list
   - Installation instructions
   - Usage guide
   - Requirements

2. **requirements.txt** (MANDATORY)
   - All Python dependencies
   - Version specifications where needed
   - Format: `package==version` or `package>=version`

3. **Main Python File** (MANDATORY)
   - Agent implementation
   - Naming: `{purpose}_agent.py` or `app.py`

### Optional Files

4. **.env.example**
   - Template for environment variables
   - Use for projects with multiple API keys
   - Never include actual API keys

5. **__init__.py**
   - For package-structured projects
   - Makes directory a Python package

6. **config.yaml / config.json**
   - Rare, only for complex configurations
   - Prefer environment variables

7. **Dockerfile**
   - Very rare (only 1 found in codebase)
   - Use only if containerization is essential

### Project Structure Templates

#### Starter Agent (Simple)
```
ai_travel_agent/
├── README.md
├── requirements.txt
└── travel_agent.py
```

#### Advanced Agent (Moderate Complexity)
```
ai_consultant_agent/
├── README.md
├── requirements.txt
├── .env.example
└── consultant_agent.py
```

#### Multi-Agent System (Complex)
```
ai_news_and_podcast_agent/
├── README.md
├── requirements.txt
├── .env.example
├── main.py
├── __init__.py
├── agents/
│   ├── __init__.py
│   ├── researcher_agent.py
│   └── writer_agent.py
├── tools/
│   ├── __init__.py
│   └── custom_tools.py
├── models/
│   ├── __init__.py
│   └── data_models.py
└── utils/
    ├── __init__.py
    └── helpers.py
```

---

## Code Style & Naming Conventions

### Directory Naming

- **Format**: `lowercase_with_underscores`
- **Pattern**: `ai_{purpose}_agent`
- **Examples**:
  - ✅ `ai_travel_agent`
  - ✅ `ai_financial_coach_agent`
  - ✅ `multi_agent_apps`
  - ❌ `AI-Travel-Agent` (no hyphens, no capitals)
  - ❌ `aiTravelAgent` (no camelCase)

- **Local Variants**: `local_{agent_name}`
  - Example: `local_travel_agent`

- **Numbered Tutorials**: `{number}_{description}`
  - Example: `1_starter_agent`, `2_model_agnostic_agent`

### File Naming

- **Agent Files**: `{purpose}_agent.py`
  - Examples: `travel_agent.py`, `finance_agent.py`

- **Main Application**: `app.py`, `main.py`, or `streamlit.py`

- **Local Variants**: `local_{agent_name}.py`
  - Example: `local_travel_agent.py`

- **Tests**: `test_{feature}.py` or `{feature}_test.py`
  - Examples: `test_agent.py`, `embedding_search_test.py`

- **Documentation**: Always `README.md` (uppercase)

- **Requirements**: Always `requirements.txt` (lowercase)

- **Environment Template**: Always `.env.example` (lowercase)

### Python Code Naming

#### Variables & Functions: `snake_case`
```python
# Good
openai_api_key = "..."
agent_team = [...]
user_query = st.text_input(...)

def setup_assistant():
    pass

def query_assistant(message):
    pass
```

#### Classes: `PascalCase`
```python
# Good
class Agent:
    pass

class OpenAIChat:
    pass

class CustomTool:
    pass
```

#### Constants: `UPPER_SNAKE_CASE`
```python
# Good
DB_URL = "..."
MAX_TOKENS = 4096
DEFAULT_MODEL = "gpt-4o"
```

#### Private Variables/Functions: Leading underscore
```python
# Good
def _internal_helper():
    pass

_cached_results = {}
```

### Code Organization

#### Import Order
```python
# 1. Standard library imports
import os
import sys
from typing import List, Dict

# 2. Third-party imports
import streamlit as st
from dotenv import load_dotenv

# 3. Agent framework imports
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# 4. Local imports
from .utils import helper_function
from .models import DataModel
```

#### Function Documentation
```python
def complex_function(param1: str, param2: int) -> Dict:
    """
    Brief description of what the function does.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value
    """
    # Implementation
    pass
```

**Note**: Simple, self-explanatory functions don't need docstrings. Use them for complex logic only.

---

## API Key Management

### Method 1: Streamlit Text Input (MOST COMMON - 80%+)

**Recommended for**: Starter agents, demos, educational projects.

```python
import streamlit as st

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    openai_api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Enter your OpenAI API key from https://platform.openai.com"
    )

# Main app
if openai_api_key:
    # Initialize agent with API key
    agent = Agent(
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        ...
    )

    # Rest of app logic
else:
    st.warning("⚠️ Please enter your OpenAI API key to continue.")
    st.stop()
```

**Alternative: Main Area Input**
```python
st.title("🤖 AI Agent")
openai_api_key = st.text_input("Enter OpenAI API Key", type="password")

if openai_api_key:
    # App logic
```

### Method 2: Environment Variables (.env)

**Recommended for**: Advanced projects, multi-agent systems, production-like setups.

**Step 1: Create .env.example**
```bash
# .env.example
OPENAI_API_KEY=your-openai-api-key-here
GOOGLE_API_KEY=your-google-api-key-here
ANTHROPIC_API_KEY=your-anthropic-api-key-here
DATABASE_URL=your-database-url-here

# Optional: Model configuration
MODEL_NAME=gpt-4o
MAX_TOKENS=4096
```

**Step 2: Load in Python**
```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access keys
openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

# With defaults
model_name = os.getenv("MODEL_NAME", "gpt-4o")
```

**Step 3: Add to .gitignore**
```bash
# .gitignore
.env
.DS_Store
```

### Method 3: Streamlit Session State

**Recommended for**: Persistent key storage during session.

```python
import streamlit as st

# Initialize session state
if "api_key" not in st.session_state:
    st.session_state.api_key = None

# Input
api_key = st.text_input("API Key", type="password", value=st.session_state.api_key or "")

# Store in session state
if api_key:
    st.session_state.api_key = api_key

    # Use stored key
    agent = Agent(
        model=OpenAIChat(api_key=st.session_state.api_key),
        ...
    )
```

### Security Best Practices

✅ **DO:**
- Use `type="password"` for Streamlit inputs
- Provide `.env.example` templates (without actual keys)
- Add `.env` to `.gitignore`
- Use environment variables for production
- Provide clear instructions in README for obtaining API keys

❌ **DON'T:**
- Commit API keys to repository
- Hardcode API keys in source code
- Share `.env` files
- Use `git add -A` or `git add .` (can accidentally stage sensitive files)
- Commit `.env`, credentials.json, or similar files

### Multiple API Keys Pattern

```python
import streamlit as st

st.sidebar.title("🔑 API Configuration")

# Multiple key inputs
openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
anthropic_key = st.sidebar.text_input("Anthropic API Key", type="password")
google_key = st.sidebar.text_input("Google API Key", type="password")

# Validation
keys_provided = {
    "OpenAI": bool(openai_key),
    "Anthropic": bool(anthropic_key),
    "Google": bool(google_key)
}

# Show status
for provider, provided in keys_provided.items():
    if provided:
        st.sidebar.success(f"✅ {provider} key provided")
    else:
        st.sidebar.warning(f"⚠️ {provider} key missing")
```

---

## Documentation Standards

### README.md Template

Every project **MUST** include a comprehensive README.md following this structure:

```markdown
# 🤖 Project Name with Emoji

Brief description (1-2 sentences) of what the agent does and its main capabilities.

## ✨ Features

- Feature 1: Description
- Feature 2: Description
- Feature 3: Description
- Feature 4: Description

## 📋 Requirements

- Python 3.8 or higher
- OpenAI API key
- [Additional API keys if needed]
- [Any special requirements]

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/[path/to/project]
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

## 💻 Usage

1. Run the Streamlit app:
   ```bash
   streamlit run [filename].py
   ```

2. Enter your API key(s) in the [sidebar/input field]

3. [Additional usage instructions specific to your agent]

## 🎯 Example Prompts

- "Example query 1"
- "Example query 2"
- "Example query 3"

## 🔧 Technical Details

[Optional section explaining architecture, how it works, etc.]

### How It Works

1. Step 1
2. Step 2
3. Step 3

### Tech Stack

- Framework: Agno/Phidata
- LLM: OpenAI GPT-4
- Tools: DuckDuckGo, YFinance, etc.
- UI: Streamlit

## 🤝 Contributing

[Optional: Contribution guidelines]

## 📝 License

[License information if applicable]
```

### Documentation Style Guidelines

#### 1. Use Emojis Consistently
- **ALWAYS** use emojis in section headers (matches repository style)
- Use relevant, recognizable emojis
- Common emojis:
  - 🤖 🧠 🤝 💬 - AI/Agents
  - ✨ 🚀 💡 🔥 - Features/Highlights
  - 📋 📝 📄 - Documentation
  - ⚙️ 🔧 🛠️ - Configuration/Setup
  - 💻 🖥️ - Usage/Code
  - 🎯 🎓 📚 - Examples/Learning
  - ⚠️ ❌ ✅ - Warnings/Status

#### 2. Keep It Concise
- Focus on practical information
- Avoid unnecessary fluff or marketing language
- Use bullet points for lists
- Keep paragraphs short (2-3 sentences max)

#### 3. Include Code Examples
- Always use proper syntax highlighting
- Show complete, runnable examples
- Include comments for clarity
- Format consistently:

```markdown
```python
# Good example with comments
from agno.agent import Agent

agent = Agent(name="Example")  # Clear variable names
```

#### 4. Provide Clear Setup Instructions
- Step-by-step numbered lists
- Include exact commands to run
- Mention prerequisites upfront
- Link to external resources for API keys

#### 5. Show Example Outputs/Prompts
- Help users understand what to expect
- Provide 3-5 example queries
- Show sample outputs when relevant

### README Examples by Complexity

#### Starter Agent (Minimal):
```markdown
# 🧳 AI Travel Agent

A simple AI agent that helps you plan your trips using GPT-4 and DuckDuckGo search.

## Features

- Destination recommendations
- Travel itinerary planning
- Budget estimation
- Weather information

## Requirements

- Python 3.8+
- OpenAI API key

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run travel_agent.py
```

Enter your OpenAI API key and start planning your trip!
```

#### Advanced Agent (Comprehensive):
- Include "How It Works" section
- Add technical architecture details
- Provide troubleshooting tips
- Include example screenshots or outputs
- Add contribution guidelines

---

## Dependencies & Package Management

### Core Dependencies by Category

#### 1. UI Framework (Nearly Universal)

```txt
streamlit>=1.30.0
```

**Why Streamlit?**
- Used in 90%+ of projects
- Quick prototyping
- Easy API key input
- Built-in chat interface
- Real-time updates

#### 2. Agent Frameworks (Choose One)

**Agno (Most Common - 80%+)**
```txt
agno>=2.2.10
```

**OpenAI Agents SDK**
```txt
openai-agents>=0.1.0
```

**Google ADK**
```txt
google-adk>=1.5.0
```

**Agency Swarm**
```txt
agency-swarm==0.4.1
```

**MCP Agent**
```txt
mcp-agent>=0.0.14
```

#### 3. LLM Provider SDKs

**OpenAI** (Most Common)
```txt
openai>=1.0.0
```

**Anthropic (Claude)**
```txt
anthropic>=0.8.0
```

**Google (Gemini)**
```txt
google-generativeai>=0.3.0
```

**xAI (Grok)**
```txt
openai>=1.0.0  # Uses OpenAI-compatible API
```

#### 4. Search Tools

```txt
# DuckDuckGo (Free)
duckduckgo-search>=3.9.0

# Google Search via SerpAPI
google-search-results>=2.4.2

# Tavily AI Search
tavily-python>=0.3.0
```

#### 5. Web Scraping & Crawling

```txt
# Firecrawl (Recommended)
firecrawl-py>=0.0.12

# Beautiful Soup
beautifulsoup4>=4.12.0
requests>=2.31.0

# Playwright (for MCP)
playwright>=1.40.0
```

#### 6. Financial Data

```txt
# Yahoo Finance
yfinance>=0.2.30

# Alpha Vantage
alpha-vantage>=2.3.1
```

#### 7. Database & Vector Stores

```txt
# PostgreSQL with vector support
psycopg-binary>=3.1.0
pgvector>=0.2.0
sqlalchemy>=2.0.0

# LanceDB (Local vector DB)
lancedb>=0.3.0

# ChromaDB
chromadb>=0.4.0

# Pinecone
pinecone-client>=2.2.0
```

#### 8. Document Processing

```txt
# PDF handling
pypdf>=3.17.0
pymupdf>=1.23.0

# Calendar/iCal
icalendar>=5.0.10

# Excel
openpyxl>=3.1.0
pandas>=2.0.0
```

#### 9. Audio & Speech

```txt
# Text-to-Speech
elevenlabs>=0.2.26

# Speech-to-Text
openai-whisper>=20230918
```

#### 10. Utilities

```txt
# Environment variables
python-dotenv>=1.0.0

# Async support
nest-asyncio>=1.5.8

# Data validation
pydantic>=2.0.0

# HTTP requests
httpx>=0.25.0

# Date/time utilities
python-dateutil>=2.8.2
```

### requirements.txt Best Practices

#### Version Pinning Strategies

**Loose Pinning (Recommended for Compatibility)**
```txt
# Allow minor version updates
streamlit>=1.30.0
agno>=2.2.10
openai>=1.0.0
```

**Strict Pinning (For Reproducibility)**
```txt
# Exact versions
streamlit==1.32.0
agno==2.2.10
openai==1.12.0
```

**Range Pinning (For Specific Compatibility)**
```txt
# Version range
streamlit>=1.30.0,<2.0.0
agno>=2.2.10,<3.0.0
```

#### Example requirements.txt (Starter Agent)

```txt
# UI
streamlit>=1.30.0

# Agent Framework
agno>=2.2.10

# LLM Provider
openai>=1.0.0

# Tools
duckduckgo-search>=3.9.0
yfinance>=0.2.30

# Utilities
python-dotenv>=1.0.0
```

#### Example requirements.txt (Advanced Agent)

```txt
# UI
streamlit>=1.32.0

# Agent Framework
agno>=2.2.10

# LLM Providers
openai>=1.12.0
anthropic>=0.8.0

# Search & Scraping
firecrawl-py>=0.0.12
duckduckgo-search>=3.9.0

# Vector Database
lancedb>=0.3.0
chromadb>=0.4.0

# Document Processing
pypdf>=3.17.0
pandas>=2.0.0

# Audio
elevenlabs>=0.2.26

# Utilities
python-dotenv>=1.0.0
pydantic>=2.0.0
httpx>=0.25.0
nest-asyncio>=1.5.8
```

### Installing Dependencies

```bash
# Standard installation
pip install -r requirements.txt

# With virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Upgrade all packages
pip install -r requirements.txt --upgrade
```

---

## Testing & Quality

### Current Testing Status

**Important Note**: Testing is minimal in this repository (only 5 test files found).

- **Philosophy**: Manual testing via Streamlit UI
- **Focus**: Runnable demos over test coverage
- **Approach**: Educational examples, not production code

### Existing Test Patterns

**Location**: Found primarily in complex projects:
```
advanced_ai_agents/multi_agent_apps/ai_news_and_podcast_agents/beifong/tests/
├── agent_agno_test.py
├── embedding_search_test.py
├── index_faiss_test.py
├── tool_browseruse_test.py
└── tts_kokoro_test.py
```

**Test Structure Example**:
```python
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Initialize agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[...],
    instructions=[...]
)

# Test execution
response: RunResponse = agent.run("Test query")
print(response.content)
```

### Manual Testing Checklist

When creating or modifying agents, verify:

- [ ] Agent runs without errors: `streamlit run agent.py`
- [ ] API key input works (if using Streamlit text input)
- [ ] Agent responds to queries appropriately
- [ ] Tools are called correctly (check with `debug_mode=True`)
- [ ] UI renders properly in browser
- [ ] Error messages are clear and helpful
- [ ] README instructions are accurate
- [ ] requirements.txt includes all dependencies

### Debugging Tips

**Enable Debug Mode**:
```python
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    debug_mode=True,  # Shows tool calls and reasoning
    show_tool_calls=True,  # Display in UI
    ...
)
```

**Streamlit Debugging**:
```python
import streamlit as st

# Show debug information
if st.checkbox("Show Debug Info"):
    st.write("Session State:", st.session_state)
    st.write("Agent Config:", agent.__dict__)
```

**Common Issues & Solutions**:

1. **Import Error**: Missing package in requirements.txt
   - Solution: Add package to requirements.txt, reinstall

2. **API Key Error**: Key not provided or invalid
   - Solution: Check key format, verify it's active

3. **Tool Error**: Tool not properly configured
   - Solution: Enable debug_mode, check tool parameters

4. **Streamlit Error**: Port already in use
   - Solution: Use `streamlit run app.py --server.port 8502`

---

## Git & GitHub Workflows

### Branch Naming Conventions

#### Claude Branches (Automated Development)
- **Pattern**: `claude/{feature-description}-{session-id}`
- **Example**: `claude/add-claude-documentation-nzz1z`
- **Critical Requirements**:
  - MUST start with `claude/`
  - MUST end with matching session ID
  - Push will fail with 403 error if pattern doesn't match
  - Session ID is automatically appended

#### Feature Branches
- **Pattern**: `feature/{description}`
- **Example**: `feature/add-voice-agent`

#### Bug Fix Branches
- **Pattern**: `fix/{description}`
- **Example**: `fix/api-key-validation`

### Git Commands & Best Practices

#### Cloning Repository
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps
```

#### Creating a New Branch
```bash
# For Claude-based development
git checkout -b claude/add-new-feature-abc123

# For regular development
git checkout -b feature/add-new-agent
```

#### Committing Changes
```bash
# Stage specific files (PREFERRED)
git add path/to/changed/file.py
git add path/to/new/README.md

# Check status
git status

# Commit with descriptive message
git commit -m "feat: Add AI travel recommendation agent

- Implement core agent logic with Agno
- Add Streamlit UI with API key input
- Include comprehensive README
- Add requirements.txt with dependencies"
```

**Commit Message Format**:
- Use conventional commit style: `type: description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Keep first line under 72 characters
- Add detailed description after blank line

#### Pushing Changes
```bash
# First push (set upstream)
git push -u origin claude/add-new-feature-abc123

# Subsequent pushes
git push

# IMPORTANT: Retry with exponential backoff if network errors occur
# Retry sequence: 2s, 4s, 8s, 16s (up to 4 retries)
```

#### Pulling Updates
```bash
# Fetch specific branch
git fetch origin main

# Pull updates
git pull origin main

# Rebase (if needed)
git pull --rebase origin main
```

### GitHub Workflows

#### Claude PR Assistant Workflow

**File**: `.github/workflows/claude.yml`

**Trigger**: Comment `@claude` on:
- Issue comments
- Pull request review comments
- New issues
- Pull request reviews

**Permissions**:
- `contents: read` - Read repository files
- `pull-requests: read` - Read PR details
- `issues: read` - Read issue details
- `id-token: write` - Authentication

**Usage**:
```markdown
@claude please review this PR and suggest improvements

@claude can you help implement the feature described in this issue?

@claude analyze this code and identify potential bugs
```

### Git Safety Practices

#### .gitignore Configuration

Current `.gitignore`:
```
.DS_Store
```

**Recommended additions** (if using env files):
```
.DS_Store
.env
*.pyc
__pycache__/
.vscode/
.idea/
*.log
venv/
env/
.pytest_cache/
```

#### Pre-commit Checks

Before committing, verify:
- [ ] No API keys in code
- [ ] No `.env` files included
- [ ] All files properly formatted
- [ ] README updated if needed
- [ ] requirements.txt updated if dependencies changed
- [ ] Removed any debug print statements
- [ ] Removed unused imports

#### Staging Files Safely

```bash
# ✅ GOOD: Stage specific files
git add starter_ai_agents/new_agent/agent.py
git add starter_ai_agents/new_agent/README.md
git add starter_ai_agents/new_agent/requirements.txt

# ❌ AVOID: Can accidentally include sensitive files
git add .
git add -A

# ✅ GOOD: Review before staging
git diff
git status
```

---

## Creating New Agents

### Step-by-Step Guide

#### Step 1: Choose the Right Category

Ask yourself:
- **Complexity**: Simple demo or complex system?
- **Agents**: Single or multiple agents?
- **Special Features**: RAG, voice, MCP, gaming?

**Decision Tree**:
```
Is it a simple, single-file demo?
  ├─ Yes → starter_ai_agents/
  └─ No → Is it a multi-agent system?
       ├─ Yes → advanced_ai_agents/multi_agent_apps/
       └─ No → Does it use RAG?
            ├─ Yes → rag_tutorials/
            └─ No → Does it use MCP?
                 ├─ Yes → mcp_ai_agents/
                 └─ No → Does it use voice?
                      ├─ Yes → voice_ai_agents/
                      └─ No → advanced_ai_agents/single_agent_apps/
```

#### Step 2: Create Directory Structure

**For Starter Agent**:
```bash
cd starter_ai_agents
mkdir ai_{purpose}_agent
cd ai_{purpose}_agent
touch README.md requirements.txt {purpose}_agent.py
```

**For Advanced Agent**:
```bash
cd advanced_ai_agents/single_agent_apps
mkdir ai_{purpose}_agent
cd ai_{purpose}_agent
touch README.md requirements.txt .env.example main.py
```

**For Multi-Agent System**:
```bash
cd advanced_ai_agents/multi_agent_apps
mkdir ai_{purpose}_agent_team
cd ai_{purpose}_agent_team
mkdir agents tools models utils
touch README.md requirements.txt .env.example main.py
touch agents/__init__.py tools/__init__.py models/__init__.py utils/__init__.py
```

#### Step 3: Implement the Agent

**Starter Agent Template** (`starter_ai_agents/ai_example_agent/example_agent.py`):

```python
"""
AI Example Agent - A simple agent that demonstrates core functionality.
"""
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Example Agent",
    page_icon="🤖",
    layout="wide"
)

# Title and description
st.title("🤖 AI Example Agent")
st.markdown("*A simple AI agent that helps you with [purpose]*")

# Sidebar for API key
with st.sidebar:
    st.header("⚙️ Configuration")
    openai_api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Get your API key from https://platform.openai.com/api-keys"
    )

    if openai_api_key:
        st.success("✅ API Key provided")
    else:
        st.warning("⚠️ Please enter your API key")

# Main application
if openai_api_key:
    # Initialize agent
    agent = Agent(
        name="Example Agent",
        role="A helpful AI assistant that [specific role]",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        tools=[DuckDuckGoTools()],
        instructions=[
            "You are a helpful assistant that [specific capability]",
            "Always provide clear and concise responses",
            "Use tools when necessary to get accurate information"
        ],
        markdown=True,
        show_tool_calls=True,
        add_datetime_to_context=True
    )

    # User input
    st.subheader("💬 Ask Me Anything")
    user_query = st.text_area(
        "Enter your query:",
        height=100,
        placeholder="Type your question here..."
    )

    # Submit button
    if st.button("🚀 Submit", type="primary"):
        if user_query:
            with st.spinner("🔄 Processing your query..."):
                try:
                    # Get agent response
                    response = agent.run(user_query)

                    # Display response
                    st.subheader("📝 Response")
                    st.markdown(response.content)

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a query")

    # Example prompts
    with st.expander("💡 Example Prompts"):
        st.markdown("""
        - Example query 1
        - Example query 2
        - Example query 3
        """)
else:
    st.info("👆 Please enter your OpenAI API key in the sidebar to get started")

# Footer
st.divider()
st.markdown("*Powered by Agno and OpenAI GPT-4*")
```

#### Step 4: Create requirements.txt

```txt
# UI
streamlit>=1.30.0

# Agent Framework
agno>=2.2.10

# LLM Provider
openai>=1.0.0

# Tools
duckduckgo-search>=3.9.0

# Utilities
python-dotenv>=1.0.0
```

#### Step 5: Write README.md

Use the [Documentation Standards](#documentation-standards) template above.

**Quick README Template**:
```markdown
# 🤖 AI [Purpose] Agent

A [simple/advanced] AI agent that helps you [main purpose].

## ✨ Features

- Feature 1
- Feature 2
- Feature 3

## 📋 Requirements

- Python 3.8+
- OpenAI API key

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/[category]/ai_[purpose]_agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. Run the app:
   ```bash
   streamlit run [filename].py
   ```

2. Enter your OpenAI API key in the sidebar

3. Start interacting with the agent!

## 🎯 Example Prompts

- "Example query 1"
- "Example query 2"
```

#### Step 6: Test Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the agent
streamlit run example_agent.py

# Test in browser (usually opens automatically at http://localhost:8501)
# Verify:
# - API key input works
# - Agent responds correctly
# - UI looks good
# - No errors in console
```

#### Step 7: Commit and Push

```bash
# Stage files
git add starter_ai_agents/ai_example_agent/

# Commit
git commit -m "feat: Add AI example agent

- Implement core agent logic with Agno
- Add Streamlit UI with API key input
- Include comprehensive README
- Add requirements.txt with dependencies"

# Push (if on Claude branch)
git push -u origin claude/add-example-agent-abc123
```

### Advanced Agent Patterns

#### Multi-Agent System Example

```python
"""
Multi-Agent Team Example
"""
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import streamlit as st

# Configure Streamlit
st.set_page_config(page_title="Multi-Agent Team", page_icon="👥", layout="wide")

# API Key
openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    # Researcher Agent
    researcher = Agent(
        name="Researcher",
        role="Research and gather information",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        tools=[DuckDuckGoTools()],
        instructions=["Conduct thorough research", "Provide accurate information"]
    )

    # Analyst Agent
    analyst = Agent(
        name="Analyst",
        role="Analyze data and provide insights",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        tools=[YFinanceTools()],
        instructions=["Analyze data carefully", "Provide actionable insights"]
    )

    # Coordinator Agent
    coordinator = Agent(
        name="Coordinator",
        role="Coordinate team and synthesize results",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        team=[researcher, analyst],
        instructions=["Coordinate the team", "Synthesize findings"]
    )

    # User Interface
    st.title("👥 Multi-Agent Team")
    query = st.text_area("Enter your query:")

    if st.button("Execute"):
        with st.spinner("Team is working..."):
            response = coordinator.run(query)
            st.markdown(response.content)
```

#### RAG Agent Example

```python
"""
RAG Agent Example with Vector Database
"""
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb import LanceDb
import streamlit as st

# API Key
openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    # Create knowledge base
    knowledge_base = PDFKnowledgeBase(
        path="path/to/documents",
        vector_db=LanceDb(
            table_name="documents",
            uri="tmp/lancedb"
        )
    )

    # Create RAG agent
    rag_agent = Agent(
        name="RAG Agent",
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
        knowledge_base=knowledge_base,
        instructions=["Use the knowledge base to answer questions accurately"],
        search_knowledge=True
    )

    # UI
    st.title("📚 RAG Agent")
    query = st.text_input("Ask a question about the documents:")

    if query:
        response = rag_agent.run(query)
        st.markdown(response.content)
```

---

## Common Pitfalls

### 1. Import Errors

**Problem**: `ModuleNotFoundError: No module named 'agno'`

**Solutions**:
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install/reinstall requirements
pip install -r requirements.txt

# Check if package is installed
pip list | grep agno

# Upgrade pip
pip install --upgrade pip
```

### 2. API Key Issues

**Problem**: Agent fails with authentication error

**Solutions**:
- Verify API key is correct (no extra spaces)
- Check API key is active in provider dashboard
- Ensure sufficient credits/quota
- Test with simple request first
```python
import openai
openai.api_key = "your-key"
openai.models.list()  # Test authentication
```

### 3. Streamlit Port Conflicts

**Problem**: `OSError: [Errno 48] Address already in use`

**Solutions**:
```bash
# Use different port
streamlit run app.py --server.port 8502

# Kill process using port 8501
lsof -ti:8501 | xargs kill -9  # On Mac/Linux
netstat -ano | findstr :8501  # On Windows (get PID, then taskkill)
```

### 4. Tool Not Working

**Problem**: Agent doesn't use tools or tools fail

**Solutions**:
- Enable debug mode: `debug_mode=True`
- Check tool configuration
```python
agent = Agent(
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,  # Show in UI
    debug_mode=True  # Show in console
)
```
- Verify tool-specific API keys (e.g., SerpAPI)
- Check tool instructions in agent configuration

### 5. Large Response Truncation

**Problem**: Agent response is cut off

**Solutions**:
```python
# Increase max tokens
model = OpenAIChat(
    id="gpt-4o",
    max_tokens=4096  # Increase limit
)

# Stream response
response = agent.run(query, stream=True)
for chunk in response:
    st.write(chunk)
```

### 6. Memory/Performance Issues

**Problem**: Application slow or crashes

**Solutions**:
- Use smaller model: `gpt-4o-mini` instead of `gpt-4o`
- Limit context: Don't load entire large documents
- Use streaming: Process responses in chunks
- Clear cache: `streamlit cache clear`

### 7. Dependency Conflicts

**Problem**: Conflicting package versions

**Solutions**:
```bash
# Create fresh virtual environment
python -m venv fresh_venv
source fresh_venv/bin/activate
pip install -r requirements.txt

# Check conflicts
pip check

# Update problematic packages
pip install --upgrade package-name
```

### 8. .gitignore Issues

**Problem**: Accidentally committed sensitive files

**Solutions**:
```bash
# Remove from Git but keep locally
git rm --cached .env

# Remove from history (if already committed)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (CAUTION: Coordinate with team)
git push origin --force --all
```

### 9. README Outdated

**Problem**: Instructions don't match current code

**Solution**: Always update README when changing:
- File names
- API requirements
- Installation steps
- Usage instructions
- Dependencies

### 10. requirements.txt Incomplete

**Problem**: Missing dependencies cause runtime errors

**Solutions**:
```bash
# Generate requirements from current environment
pip freeze > requirements.txt

# Or use pipreqs to scan imports
pip install pipreqs
pipreqs /path/to/project

# Verify all imports are covered
python -c "import pkg; print(pkg.__version__)" # Test each package
```

---

## Quick Reference

### Essential Commands

```bash
# Setup
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd awesome-llm-apps
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Development
streamlit run agent.py
streamlit run agent.py --server.port 8502

# Git
git checkout -b claude/feature-name-abc123
git add path/to/file.py
git commit -m "feat: description"
git push -u origin claude/feature-name-abc123

# Debugging
pip list  # Show installed packages
pip check  # Check for conflicts
streamlit cache clear  # Clear Streamlit cache
```

### Common Code Snippets

**Basic Agno Agent**:
```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
import streamlit as st

api_key = st.text_input("API Key", type="password")
if api_key:
    agent = Agent(
        model=OpenAIChat(id="gpt-4o", api_key=api_key),
        instructions=["Be helpful"]
    )
    response = agent.run(st.text_input("Query:"))
    st.write(response.content)
```

**With Tools**:
```python
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    tools=[DuckDuckGoTools()],
    show_tool_calls=True
)
```

**Multi-Agent**:
```python
agent1 = Agent(name="Agent 1", ...)
agent2 = Agent(name="Agent 2", team=[agent1], ...)
```

### File Structure Quick Copy

```bash
# Starter Agent
mkdir -p starter_ai_agents/ai_example_agent
cd starter_ai_agents/ai_example_agent
touch README.md requirements.txt example_agent.py

# Advanced Agent
mkdir -p advanced_ai_agents/single_agent_apps/ai_example_agent
cd advanced_ai_agents/single_agent_apps/ai_example_agent
touch README.md requirements.txt .env.example main.py
```

---

## Conclusion

This guide provides comprehensive information for AI assistants working with the Awesome LLM Apps repository. Key takeaways:

1. **Simplicity is paramount** - Focus on runnable, educational examples
2. **Follow established patterns** - Use Agno framework and Streamlit UI unless specified otherwise
3. **Document thoroughly** - Every project needs a comprehensive README
4. **Manage secrets safely** - Never commit API keys
5. **Test manually** - Verify everything works before committing
6. **Keep it practical** - Prioritize working code over complex architectures

### For Questions or Issues

- Review this guide first
- Check existing similar projects for patterns
- Consult project-specific READMEs
- Follow the repository's coding style

### Contributing Updates to This Guide

If you notice patterns or conventions not covered here:
1. Document the pattern with examples
2. Add to appropriate section
3. Update table of contents if adding new sections
4. Submit PR with clear description

---

**Last Updated**: 2026-02-04
**Guide Version**: 1.0.0
**Repository**: [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
**Maintainer**: Shubham Saboo (@Shubhamsaboo)
