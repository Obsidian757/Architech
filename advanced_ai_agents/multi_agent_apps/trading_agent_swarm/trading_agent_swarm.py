"""Trading agent swarm with a quantum portfolio-optimization node.

A small Agno team that, given a candidate ticker universe and a target
position count, picks names by formulating the selection as a QUBO and
solving with QAOA on a local Qiskit Aer simulator. The remaining agents
(research, signal, risk, paper-execution) are LLM-driven and coordinate
through a team root agent.

This is a demo. It is not financial advice and does not place real trades.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

from quantum_optimizer import quantum_portfolio_optimize

DB = "trading_swarm.db"
MODEL_ID = "gpt-4o"


research_agent = Agent(
    name="Research Agent",
    role="Surface recent news and fundamentals for each candidate ticker",
    model=OpenAIChat(id=MODEL_ID),
    tools=[
        DuckDuckGoTools(),
        YFinanceTools(company_info=True, company_news=True, analyst_recommendations=True),
    ],
    instructions=[
        "Summarize each ticker in 2-3 lines.",
        "Flag any ticker with material negative news in the last 30 days.",
    ],
    storage=SqliteAgentStorage(table_name="research_agent", db_file=DB),
    add_history_to_messages=True,
    markdown=True,
)

signal_agent = Agent(
    name="Signal Agent",
    role="Compute simple price-based signals (returns, vol, momentum) over a 1y lookback",
    model=OpenAIChat(id=MODEL_ID),
    tools=[YFinanceTools(stock_price=True, historical_prices=True)],
    instructions=[
        "Pull 1y daily closes for each ticker.",
        "Report annualized return, annualized vol, and 3-month momentum per ticker.",
        "Do not invent numbers. If yfinance returns nothing, say so.",
    ],
    storage=SqliteAgentStorage(table_name="signal_agent", db_file=DB),
    add_history_to_messages=True,
    markdown=True,
)

quantum_agent = Agent(
    name="Quantum Optimizer",
    role="Pick the final basket via QAOA on a local quantum simulator",
    model=OpenAIChat(id=MODEL_ID),
    tools=[quantum_portfolio_optimize],
    instructions=[
        "Call quantum_portfolio_optimize with the user's tickers and budget.",
        "Universe must be 8 tickers or fewer.",
        "Return the selected basket and the objective value verbatim.",
    ],
    storage=SqliteAgentStorage(table_name="quantum_agent", db_file=DB),
    add_history_to_messages=True,
    markdown=True,
)

risk_agent = Agent(
    name="Risk Agent",
    role="Sanity-check the proposed basket",
    model=OpenAIChat(id=MODEL_ID),
    tools=[YFinanceTools(historical_prices=True)],
    instructions=[
        "Confirm the basket size matches the requested budget.",
        "Compute the equal-weight basket's realized 1y vol and worst 1m drawdown.",
        "Return GO or NO-GO with a one-line justification.",
    ],
    storage=SqliteAgentStorage(table_name="risk_agent", db_file=DB),
    add_history_to_messages=True,
    markdown=True,
)

execution_agent = Agent(
    name="Paper Execution Agent",
    role="Replay last month at equal weight and report hypothetical PnL",
    model=OpenAIChat(id=MODEL_ID),
    tools=[YFinanceTools(historical_prices=True)],
    instructions=[
        "Pull the last ~21 trading days of daily closes for the approved basket.",
        "Assume equal weights, no rebalancing, no fees.",
        "Report total return and Sharpe (252d annualization). Label clearly as paper.",
    ],
    storage=SqliteAgentStorage(table_name="execution_agent", db_file=DB),
    add_history_to_messages=True,
    markdown=True,
)

trading_swarm = Agent(
    team=[research_agent, signal_agent, quantum_agent, risk_agent, execution_agent],
    name="Trading Agent Swarm",
    model=OpenAIChat(id=MODEL_ID),
    instructions=[
        "Coordinate the team in this order: Research -> Signal -> Quantum Optimizer -> Risk -> Paper Execution.",
        "Pass the selected basket from the Quantum Optimizer to Risk and Execution.",
        "Always end with a disclaimer: this is a demo, not financial advice.",
    ],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[trading_swarm]).get_app()


if __name__ == "__main__":
    serve_playground_app("trading_agent_swarm:app", reload=True)
