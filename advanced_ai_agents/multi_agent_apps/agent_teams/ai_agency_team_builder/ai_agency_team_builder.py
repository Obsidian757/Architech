"""Multi-Agent Team Builder — compose custom teams from 160+ agent personalities."""

from __future__ import annotations

import os
from pathlib import Path

import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team

from agent_parser import AgentConfig, load_all_agents


AGENTS_DIR = Path(__file__).resolve().parents[4] / "agency-agents"
MIN_TEAM_SIZE = 2
MAX_TEAM_SIZE = 6

st.set_page_config(
    page_title="AI Agency Team Builder",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data(show_spinner=False)
def get_agents() -> dict[str, list[AgentConfig]]:
    return load_all_agents(AGENTS_DIR)


def init_state() -> None:
    defaults = {
        "selected_agents": [],
        "messages": [],
        "team": None,
        "phase": "browse",
        "team_name": "Custom Agency Team",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def build_team(configs: list[AgentConfig], api_key: str, model_id: str) -> Team:
    members = [
        Agent(
            name=cfg.name,
            role=cfg.description or cfg.vibe or cfg.name,
            model=OpenAIChat(id=model_id, api_key=api_key),
            instructions=[cfg.personality],
            markdown=True,
        )
        for cfg in configs
    ]
    return Team(
        name=st.session_state.team_name,
        mode="coordinate",
        model=OpenAIChat(id=model_id, api_key=api_key),
        members=members,
        instructions=[
            "You are coordinating a team of specialized agents.",
            "Delegate tasks to the most appropriate team member based on their role and expertise.",
            "If a task requires multiple perspectives, engage multiple members.",
            "Synthesize member responses into a coherent, well-structured final answer.",
        ],
        show_tool_calls=True,
        markdown=True,
        show_members_responses=True,
        enable_agentic_context=True,
        share_member_interactions=True,
    )


def render_sidebar() -> tuple[str, str]:
    st.sidebar.header("🔑 Configuration")
    api_key = st.sidebar.text_input(
        "OpenAI API Key",
        type="password",
        value=os.getenv("OPENAI_API_KEY", ""),
    )
    model_id = st.sidebar.selectbox("Model", ["gpt-4o", "gpt-4o-mini"], index=0)

    st.sidebar.divider()
    st.sidebar.subheader(f"👥 Team ({len(st.session_state.selected_agents)}/{MAX_TEAM_SIZE})")

    if not st.session_state.selected_agents:
        st.sidebar.caption("No agents selected yet. Browse and add from the main panel.")
    else:
        for idx, cfg in enumerate(st.session_state.selected_agents):
            cols = st.sidebar.columns([5, 1])
            cols[0].markdown(f"{cfg.emoji} **{cfg.name}**")
            if cols[1].button("✕", key=f"remove_{idx}", help="Remove from team"):
                st.session_state.selected_agents.pop(idx)
                st.session_state.team = None
                st.rerun()

    st.sidebar.divider()
    if st.sidebar.button("🗑️ Clear Team", use_container_width=True):
        st.session_state.selected_agents = []
        st.session_state.team = None
        st.session_state.messages = []
        st.session_state.phase = "browse"
        st.rerun()
    if st.sidebar.button("💬 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    return api_key, model_id


def render_browse(agents_by_division: dict[str, list[AgentConfig]]) -> None:
    st.title("🏢 AI Agency Team Builder")
    st.caption(
        f"Compose a custom team from {sum(len(v) for v in agents_by_division.values())} "
        f"specialized agent personalities across {len(agents_by_division)} divisions."
    )

    team_count = len(st.session_state.selected_agents)
    if team_count >= MIN_TEAM_SIZE:
        if st.button("🚀 Start Chat with Team", type="primary", use_container_width=True):
            st.session_state.phase = "chat"
            st.rerun()
    else:
        st.info(f"Select at least {MIN_TEAM_SIZE} agents to start a team chat.")

    selected_paths = {c.file_path for c in st.session_state.selected_agents}

    division_names = list(agents_by_division.keys())
    division_labels = [
        f"{name.replace('-', ' ').title()} ({len(agents_by_division[name])})"
        for name in division_names
    ]
    tabs = st.tabs(division_labels)

    for tab, division in zip(tabs, division_names):
        with tab:
            agents = agents_by_division[division]
            cols_per_row = 3
            for i in range(0, len(agents), cols_per_row):
                row = st.columns(cols_per_row)
                for col, cfg in zip(row, agents[i : i + cols_per_row]):
                    with col:
                        with st.container(border=True):
                            st.markdown(f"### {cfg.emoji} {cfg.name}")
                            if cfg.vibe:
                                st.caption(f"_{cfg.vibe}_")
                            if cfg.description:
                                with st.expander("Description"):
                                    st.write(cfg.description)
                            is_selected = cfg.file_path in selected_paths
                            at_max = team_count >= MAX_TEAM_SIZE and not is_selected
                            if is_selected:
                                st.success("✓ In team")
                            elif at_max:
                                st.warning("Team is full")
                            else:
                                if st.button(
                                    "➕ Add to Team",
                                    key=f"add_{cfg.file_path}",
                                    use_container_width=True,
                                ):
                                    st.session_state.selected_agents.append(cfg)
                                    st.session_state.team = None
                                    st.rerun()


def render_chat(api_key: str, model_id: str) -> None:
    col_title, col_back = st.columns([4, 1])
    col_title.title("💬 Team Chat")
    if col_back.button("← Back to Builder", use_container_width=True):
        st.session_state.phase = "browse"
        st.rerun()

    roster = " · ".join(
        f"{c.emoji} {c.name}" for c in st.session_state.selected_agents
    )
    st.caption(f"**Team:** {roster}")

    if not api_key:
        st.warning("⚠️ Enter your OpenAI API key in the sidebar to chat with the team.")
        return

    if st.session_state.team is None:
        with st.spinner("Assembling team..."):
            st.session_state.team = build_team(
                st.session_state.selected_agents, api_key, model_id
            )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Give your team a task...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Team is collaborating..."):
                try:
                    response = st.session_state.team.run(prompt, stream=False)
                    content = response.content if hasattr(response, "content") else str(response)
                except Exception as exc:  # noqa: BLE001
                    content = f"❌ Error: {exc}"
            st.markdown(content)
        st.session_state.messages.append({"role": "assistant", "content": content})


def main() -> None:
    init_state()
    api_key, model_id = render_sidebar()

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

    agents_by_division = get_agents()
    if not agents_by_division:
        st.error(
            f"No agents found at {AGENTS_DIR}. "
            "Ensure the agency-agents/ directory exists at the project root."
        )
        return

    if st.session_state.phase == "chat" and len(st.session_state.selected_agents) >= MIN_TEAM_SIZE:
        render_chat(api_key, model_id)
    else:
        st.session_state.phase = "browse"
        render_browse(agents_by_division)


if __name__ == "__main__":
    main()
