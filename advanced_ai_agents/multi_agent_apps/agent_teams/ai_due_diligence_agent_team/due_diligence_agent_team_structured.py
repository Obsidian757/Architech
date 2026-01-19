"""
Structured AI Due Diligence Agent Team

Enhanced version with structured output using Pydantic schemas.
Returns comprehensive DueDiligenceReport objects with quantitative scoring.
"""

import json
import uuid
from datetime import datetime
from typing import Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

from models.schemas import (
    DueDiligenceReport,
    CompanyProfile,
    FinancialMetrics,
    InvestmentScore,
    MarketAnalysis,
    RiskAssessment,
    TeamAssessment
)
from utils.scoring import InvestmentScoringFramework


class DueDiligenceTeamStructured:
    """
    Structured due diligence agent team with quantitative scoring.

    Coordinates specialized agents to produce comprehensive,
    structured investment analysis reports.
    """

    def __init__(self, api_key: str, model: str = "gpt-4o"):
        """
        Initialize the due diligence agent team.

        Args:
            api_key: OpenAI API key
            model: Model to use for agents
        """
        self.api_key = api_key
        self.model = model
        self.scoring_framework = InvestmentScoringFramework()

        # Initialize specialist agents
        self._init_agents()

    def _init_agents(self):
        """Initialize all specialist agents"""

        # Company Research Agent
        self.company_research_agent = Agent(
            name="Company Research Agent",
            role="Research startup companies and gather comprehensive background information",
            model=OpenAIChat(id=self.model, api_key=self.api_key),
            tools=[DuckDuckGoTools()],
            instructions=[
                "Research company history, founding team, and mission",
                "Identify key products, services, and value propositions",
                "Find information about funding rounds, investors, and valuation",
                "Gather details about company culture and organizational structure",
                "Search for recent news, press releases, and media coverage",
                "Provide factual, well-sourced information with specific data points",
                "Focus on quantitative traction metrics: users, revenue, growth rates"
            ],
            storage=SqliteAgentStorage(table_name="company_research_agent", db_file="due_diligence_agents.db"),
            add_history_to_messages=True,
            markdown=True,
        )

        # Financial Analysis Agent
        self.financial_analysis_agent = Agent(
            name="Financial Analysis Agent",
            role="Analyze financial health, metrics, and create financial projections",
            model=OpenAIChat(id=self.model, api_key=self.api_key),
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
                "Extract specific numerical metrics: revenue, growth rates, burn rate, runway",
                "Analyze unit economics: CAC, LTV, payback period, churn",
                "Compare financial metrics with industry benchmarks",
                "Assess financial sustainability and path to profitability",
                "Identify financial strengths and weaknesses with specific examples",
                "Provide data-driven insights on capital efficiency"
            ],
            storage=SqliteAgentStorage(table_name="financial_analysis_agent", db_file="due_diligence_agents.db"),
            add_history_to_messages=True,
            markdown=True,
        )

        # Market Analysis Agent
        self.market_analysis_agent = Agent(
            name="Market Analysis Agent",
            role="Analyze market opportunities, competition, and industry trends",
            model=OpenAIChat(id=self.model, api_key=self.api_key),
            tools=[DuckDuckGoTools()],
            instructions=[
                "Size the market: provide specific TAM, SAM, and SOM values in millions/billions",
                "Research key competitors with market share data",
                "Analyze industry trends with growth rate percentages",
                "Identify barriers to entry and competitive moats with concrete examples",
                "Evaluate market timing and adoption curves",
                "Research customer segments with specific demographics/firmographics",
                "Assess regulatory environment and compliance requirements",
                "Present findings with supporting data sources and citations"
            ],
            storage=SqliteAgentStorage(table_name="market_analysis_agent", db_file="due_diligence_agents.db"),
            add_history_to_messages=True,
            markdown=True,
        )

        # Risk Assessment Agent
        self.risk_assessment_agent = Agent(
            name="Risk Assessment Agent",
            role="Identify and evaluate all potential risks associated with the investment",
            model=OpenAIChat(id=self.model, api_key=self.api_key),
            tools=[DuckDuckGoTools()],
            instructions=[
                "Identify specific, concrete risks (not generic statements)",
                "Categorize each risk: Market, Technology, Team, Financial, Regulatory, Operational",
                "Assess severity: Critical, High, Medium, Low",
                "Evaluate impact and probability for each risk",
                "Provide specific, actionable mitigation strategies",
                "Focus on material risks that could affect investment returns",
                "Consider both immediate and long-term risks",
                "Identify red flags that would disqualify the investment"
            ],
            storage=SqliteAgentStorage(table_name="risk_assessment_agent", db_file="due_diligence_agents.db"),
            add_history_to_messages=True,
            markdown=True,
        )

        # Scoring Agent
        self.scoring_agent = Agent(
            name="Investment Scoring Agent",
            role="Score the investment opportunity across multiple dimensions",
            model=OpenAIChat(id=self.model, api_key=self.api_key),
            instructions=[
                "Score on 0-100 scale for each dimension",
                "Team: Evaluate experience, track record, execution capability",
                "Market: Assess size, growth, timing, competition",
                "Product: Evaluate differentiation, technical moat, scalability",
                "Financial: Analyze unit economics, growth, capital efficiency",
                "Execution: Assess traction, momentum, milestone achievement",
                "Provide detailed rationale for each score",
                "Be objective and critical - high scores require exceptional performance"
            ],
            markdown=True,
        )

    def run_analysis(self, query: str) -> Optional[DueDiligenceReport]:
        """
        Run complete due diligence analysis and return structured report.

        Args:
            query: Analysis query (e.g., "Analyze Company X for investment")

        Returns:
            DueDiligenceReport object with structured data
        """
        try:
            # Generate unique report ID
            report_id = str(uuid.uuid4())[:8]
            analysis_date = datetime.now().strftime("%Y-%m-%d")

            print(f"\n🔬 Starting analysis (Report ID: {report_id})...\n")

            # Step 1: Company Research
            print("📋 Step 1/5: Researching company background...")
            company_query = f"""{query}

            Provide detailed company information including:
            - Company name, founding year, headquarters location
            - Industry and business model
            - Elevator pitch and value proposition
            - Key products/services
            - Founding team names and backgrounds
            - Funding history (total raised, last valuation, stage)
            - Traction metrics (users, revenue, growth rates)
            - Recent news and developments

            Format the response with clear sections and specific data points.
            """
            company_response = self.company_research_agent.run(company_query, stream=False)
            company_text = company_response.content

            # Step 2: Financial Analysis
            print("💰 Step 2/5: Analyzing financials...")
            financial_query = f"""{query}

            Extract and analyze financial metrics:
            - Current annual revenue (in millions)
            - Revenue growth rate (YoY percentage)
            - Monthly burn rate (in thousands)
            - Cash runway (in months)
            - CAC/LTV ratio
            - Gross margin percentage
            - ARR or MRR
            - Profitability status
            - Total funding raised
            - Last valuation

            Provide specific numbers with units. If data not available, state that explicitly.
            """
            financial_response = self.financial_analysis_agent.run(financial_query, stream=False)
            financial_text = financial_response.content

            # Step 3: Market Analysis
            print("📈 Step 3/5: Analyzing market opportunity...")
            market_query = f"""{query}

            Analyze the market:
            - TAM (Total Addressable Market in millions/billions)
            - SAM (Serviceable Addressable Market)
            - SOM (Serviceable Obtainable Market)
            - Market growth rate (annual percentage)
            - Target customer segment (be specific)
            - Key competitors (list top 5 with brief descriptions)
            - Competitive advantages (3-5 specific differentiators)
            - Market timing assessment
            - Barriers to entry

            Provide concrete numbers and specific examples.
            """
            market_response = self.market_analysis_agent.run(market_query, stream=False)
            market_text = market_response.content

            # Step 4: Risk Assessment
            print("⚠️  Step 4/5: Assessing risks...")
            risk_query = f"""{query}

            Identify specific investment risks:
            - List 5-10 concrete risks (not generic statements)
            - Categorize each: Market/Technology/Team/Financial/Regulatory/Operational
            - Assess severity: Critical/High/Medium/Low
            - Rate impact and probability: High/Medium/Low
            - Provide specific mitigation strategy for each

            Focus on material risks that could significantly affect returns.
            """
            risk_response = self.risk_assessment_agent.run(risk_query, stream=False)
            risk_text = risk_response.content

            # Step 5: Investment Scoring
            print("🎯 Step 5/5: Calculating investment scores...")
            scoring_query = f"""Based on the following due diligence research, score this investment opportunity:

            COMPANY RESEARCH:
            {company_text}

            FINANCIAL ANALYSIS:
            {financial_text}

            MARKET ANALYSIS:
            {market_text}

            RISK ASSESSMENT:
            {risk_text}

            Provide investment scores (0-100) for:
            1. Team Score - Evaluate founder experience, execution capability, team completeness
            2. Market Score - Assess market size, growth, timing, competition
            3. Product Score - Evaluate differentiation, technical moat, scalability
            4. Financial Score - Analyze unit economics, growth efficiency, sustainability
            5. Execution Score - Assess traction, momentum, milestones achieved

            For each score, provide a detailed rationale (2-3 sentences) explaining the score.
            Be critical and objective - scores above 80 should be rare and well-justified.
            """
            scoring_response = self.scoring_agent.run(scoring_query, stream=False)
            scoring_text = scoring_response.content

            # Now parse and structure the results
            print("\n📊 Structuring analysis results...")
            structured_report = self._parse_to_structured_report(
                report_id=report_id,
                analysis_date=analysis_date,
                company_text=company_text,
                financial_text=financial_text,
                market_text=market_text,
                risk_text=risk_text,
                scoring_text=scoring_text,
                query=query
            )

            print(f"\n✅ Analysis complete! Report ID: {report_id}\n")
            return structured_report

        except Exception as e:
            print(f"\n❌ Error during analysis: {str(e)}\n")
            raise

    def _parse_to_structured_report(
        self,
        report_id: str,
        analysis_date: str,
        company_text: str,
        financial_text: str,
        market_text: str,
        risk_text: str,
        scoring_text: str,
        query: str
    ) -> DueDiligenceReport:
        """
        Parse agent outputs into structured Pydantic models.

        Uses GPT-4o to extract structured data from markdown text.
        """
        # Create a synthesis agent to structure the output
        synthesis_agent = Agent(
            name="Synthesis Agent",
            role="Structure due diligence findings into JSON format",
            model=OpenAIChat(id=self.model, api_key=self.api_key),
            response_model=DueDiligenceReport,
            markdown=False,
        )

        synthesis_query = f"""
        Structure the following due diligence analysis into a complete JSON report.

        Report ID: {report_id}
        Analysis Date: {analysis_date}

        COMPANY RESEARCH:
        {company_text}

        FINANCIAL ANALYSIS:
        {financial_text}

        MARKET ANALYSIS:
        {market_text}

        RISK ASSESSMENT:
        {risk_text}

        INVESTMENT SCORING:
        {scoring_text}

        Extract ALL information into the structured format. Be thorough and include:
        - All company details (name, industry, stage, value proposition, products, traction)
        - All financial metrics with specific numbers
        - Complete market analysis with TAM/SAM/SOM
        - Team assessment with founder names and experience
        - Investment scores with detailed rationales
        - All identified risks with severity, impact, probability, and mitigation
        - Executive summary and investment thesis (write compelling narratives)
        - Final recommendation (Strong Buy/Buy/Hold/Pass) based on scores and risks
        - Recommended investment amount and target ownership (make reasonable estimates)
        - Next steps and additional diligence needed (3-5 items each)

        If specific data is not available, use null for optional fields.
        Be comprehensive and extract every relevant detail from the analysis.
        """

        result = synthesis_agent.run(synthesis_query, stream=False)

        # The response_model will automatically structure it
        if isinstance(result.content, DueDiligenceReport):
            report = result.content
        else:
            # Fallback: parse JSON
            report = DueDiligenceReport.model_validate_json(result.content)

        # Calculate overall score using our framework
        overall_score = self.scoring_framework.calculate_overall_score(
            team_score=report.investment_scores.team_score,
            market_score=report.investment_scores.market_score,
            product_score=report.investment_scores.product_score,
            financial_score=report.investment_scores.financial_score,
            execution_score=report.investment_scores.execution_score,
            risks=report.key_risks
        )
        report.investment_scores.overall_score = overall_score

        # Update recommendation based on scoring framework
        critical_risks = sum(1 for r in report.key_risks if r.severity == "Critical")
        recommendation = self.scoring_framework.get_recommendation(overall_score, critical_risks)
        report.recommendation = recommendation

        return report
