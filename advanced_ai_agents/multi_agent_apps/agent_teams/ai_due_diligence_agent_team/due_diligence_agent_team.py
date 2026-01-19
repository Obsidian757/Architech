from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.playground import Playground, serve_playground_app

# Company Research Agent
# Specializes in gathering comprehensive company background information
company_research_agent = Agent(
    name="Company Research Agent",
    role="Research startup companies and gather comprehensive background information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Research company history, founding team, and mission",
        "Identify key products, services, and value propositions",
        "Find information about funding rounds, investors, and valuation",
        "Gather details about company culture and organizational structure",
        "Search for recent news, press releases, and media coverage",
        "Provide factual, well-sourced information in a structured format"
    ],
    storage=SqliteAgentStorage(table_name="company_research_agent", db_file="due_diligence_agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Financial Analysis Agent
# Analyzes financial health, metrics, and projections
financial_analysis_agent = Agent(
    name="Financial Analysis Agent",
    role="Analyze financial health, metrics, and create financial projections",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
            technical_indicators=True,
            stock_fundamentals=True
        ),
        DuckDuckGoTools()
    ],
    instructions=[
        "Always use tables to display financial data",
        "Analyze revenue, profit margins, and growth rates",
        "Evaluate burn rate, runway, and cash flow if applicable",
        "Compare financial metrics with industry benchmarks",
        "Assess unit economics and customer acquisition costs",
        "Identify financial strengths and weaknesses",
        "Provide data-driven insights on financial sustainability"
    ],
    storage=SqliteAgentStorage(table_name="financial_analysis_agent", db_file="due_diligence_agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Market Analysis Agent
# Researches market size, competition, and industry trends
market_analysis_agent = Agent(
    name="Market Analysis Agent",
    role="Analyze market opportunities, competition, and industry trends",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Identify and size the total addressable market (TAM), serviceable addressable market (SAM), and serviceable obtainable market (SOM)",
        "Research key competitors and their market positioning",
        "Analyze industry trends, growth drivers, and market dynamics",
        "Identify barriers to entry and competitive moats",
        "Evaluate market timing and adoption curves",
        "Research customer segments and target demographics",
        "Assess regulatory environment and industry challenges",
        "Present findings with supporting data and sources"
    ],
    storage=SqliteAgentStorage(table_name="market_analysis_agent", db_file="due_diligence_agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Risk Assessment Agent
# Identifies and evaluates potential risks
risk_assessment_agent = Agent(
    name="Risk Assessment Agent",
    role="Identify and evaluate all potential risks associated with the investment",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Identify market risks (competition, market size, timing)",
        "Evaluate technology risks (IP, technical feasibility, scalability)",
        "Assess team risks (experience, key person dependencies, culture)",
        "Analyze financial risks (burn rate, funding needs, unit economics)",
        "Identify regulatory and compliance risks",
        "Evaluate operational risks (execution, supply chain, dependencies)",
        "Consider reputational and ESG risks",
        "Categorize risks by severity (Critical, High, Medium, Low)",
        "Provide mitigation strategies for key risks",
        "Use structured format with clear risk categorization"
    ],
    storage=SqliteAgentStorage(table_name="risk_assessment_agent", db_file="due_diligence_agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Due Diligence Team Agent
# Orchestrates all specialist agents to provide comprehensive investment analysis
due_diligence_team = Agent(
    team=[
        company_research_agent,
        financial_analysis_agent,
        market_analysis_agent,
        risk_assessment_agent
    ],
    name="AI Due Diligence Team",
    role="Provide comprehensive due diligence analysis for startup investments",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Coordinate with all specialist agents to gather comprehensive information",
        "Synthesize findings from all agents into a cohesive analysis",
        "Structure the output as a professional due diligence report with clear sections:",
        "  1. Executive Summary - Key findings and recommendation",
        "  2. Company Overview - Background, team, product, and traction",
        "  3. Financial Analysis - Key metrics, projections, and sustainability",
        "  4. Market Analysis - Market size, competition, and positioning",
        "  5. Risk Assessment - Key risks and mitigation strategies",
        "  6. Investment Recommendation - Final assessment with rationale",
        "Ensure all claims are supported by data and sources",
        "Highlight both strengths and weaknesses objectively",
        "Provide actionable insights for investment decision-making",
        "Use tables, bullet points, and clear formatting for readability"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Create Playground app for interactive interface
app = Playground(agents=[due_diligence_team]).get_app()

if __name__ == "__main__":
    # Serve the playground app with hot reload for development
    serve_playground_app("due_diligence_agent_team:app", reload=True)
