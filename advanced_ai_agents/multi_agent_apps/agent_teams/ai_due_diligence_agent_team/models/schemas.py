from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime


class FinancialMetrics(BaseModel):
    """Financial health and performance metrics"""
    revenue_current: Optional[float] = Field(None, description="Current annual revenue in millions USD")
    revenue_growth_yoy: Optional[float] = Field(None, description="Year-over-year revenue growth percentage")
    burn_rate_monthly: Optional[float] = Field(None, description="Monthly burn rate in thousands USD")
    runway_months: Optional[int] = Field(None, description="Months of runway remaining")
    cac_to_ltv_ratio: Optional[float] = Field(None, description="Customer Acquisition Cost to Lifetime Value ratio")
    gross_margin: Optional[float] = Field(None, description="Gross margin percentage")
    arr_mrr: Optional[float] = Field(None, description="Annual Recurring Revenue or Monthly Recurring Revenue")
    profitability_status: Optional[str] = Field(None, description="Current profitability status (Profitable, Break-even, Burning cash)")
    funding_raised_total: Optional[float] = Field(None, description="Total funding raised in millions USD")
    last_valuation: Optional[float] = Field(None, description="Last known valuation in millions USD")


class InvestmentScore(BaseModel):
    """Quantitative investment scoring framework (0-100 scale)"""
    team_score: int = Field(ge=0, le=100, description="Team quality and experience score")
    market_score: int = Field(ge=0, le=100, description="Market opportunity and timing score")
    product_score: int = Field(ge=0, le=100, description="Product differentiation and technical moat score")
    financial_score: int = Field(ge=0, le=100, description="Financial health and unit economics score")
    execution_score: int = Field(ge=0, le=100, description="Execution capability and traction score")
    overall_score: int = Field(ge=0, le=100, description="Weighted overall investment score")

    team_rationale: str = Field(description="Explanation for team score")
    market_rationale: str = Field(description="Explanation for market score")
    product_rationale: str = Field(description="Explanation for product score")
    financial_rationale: str = Field(description="Explanation for financial score")
    execution_rationale: str = Field(description="Explanation for execution score")


class RiskAssessment(BaseModel):
    """Individual risk identification and assessment"""
    risk_category: Literal["Market", "Technology", "Team", "Financial", "Regulatory", "Operational"] = Field(
        description="Category of risk"
    )
    severity: Literal["Critical", "High", "Medium", "Low"] = Field(
        description="Severity level of the risk"
    )
    risk_name: str = Field(description="Short name/title of the risk")
    description: str = Field(description="Detailed description of the risk")
    impact: Literal["High", "Medium", "Low"] = Field(
        description="Potential impact if risk materializes"
    )
    probability: Literal["High", "Medium", "Low"] = Field(
        description="Likelihood of risk occurring"
    )
    mitigation_strategy: str = Field(description="Recommended mitigation approach")


class TeamAssessment(BaseModel):
    """Founding team and leadership evaluation"""
    founder_names: List[str] = Field(description="Names of key founders")
    relevant_experience: str = Field(description="Relevant industry and startup experience")
    technical_capabilities: str = Field(description="Technical expertise and capabilities")
    previous_exits: Optional[str] = Field(None, description="Previous successful exits or notable achievements")
    team_completeness: str = Field(description="Assessment of team gaps and completeness")
    key_hires_needed: List[str] = Field(description="Critical roles that need to be filled")


class MarketAnalysis(BaseModel):
    """Market opportunity and competitive landscape"""
    tam: Optional[float] = Field(None, description="Total Addressable Market in millions USD")
    sam: Optional[float] = Field(None, description="Serviceable Addressable Market in millions USD")
    som: Optional[float] = Field(None, description="Serviceable Obtainable Market in millions USD")
    market_growth_rate: Optional[float] = Field(None, description="Annual market growth rate percentage")
    target_customer_segment: str = Field(description="Primary target customer segment")
    key_competitors: List[str] = Field(description="Main competitors in the space")
    competitive_advantages: List[str] = Field(description="Key competitive advantages and differentiators")
    market_timing: str = Field(description="Assessment of market timing and readiness")
    barriers_to_entry: str = Field(description="Barriers protecting the business")


class CompanyProfile(BaseModel):
    """Core company information and background"""
    company_name: str = Field(description="Official company name")
    founded_year: Optional[int] = Field(None, description="Year company was founded")
    headquarters: Optional[str] = Field(None, description="Location of headquarters")
    website: Optional[str] = Field(None, description="Company website URL")
    industry: str = Field(description="Primary industry/sector")
    business_model: str = Field(description="Core business model (B2B SaaS, Marketplace, etc.)")
    elevator_pitch: str = Field(description="One sentence description of what the company does")
    value_proposition: str = Field(description="Core value proposition and problem being solved")
    stage: Literal["Pre-seed", "Seed", "Series A", "Series B", "Series C+", "Growth", "Unknown"] = Field(
        description="Current funding stage"
    )
    key_products: List[str] = Field(description="Main products or services offered")
    traction_metrics: str = Field(description="Key traction metrics and milestones achieved")


class DueDiligenceReport(BaseModel):
    """Comprehensive due diligence analysis report"""
    report_id: str = Field(description="Unique identifier for this report")
    analysis_date: str = Field(description="Date analysis was performed (YYYY-MM-DD)")

    # Core sections
    company_profile: CompanyProfile
    team_assessment: TeamAssessment
    market_analysis: MarketAnalysis
    financial_metrics: FinancialMetrics
    investment_scores: InvestmentScore

    # Risk analysis
    key_risks: List[RiskAssessment] = Field(description="Top identified risks")

    # Executive summary
    executive_summary: str = Field(description="High-level summary of key findings")
    investment_thesis: str = Field(description="Core investment thesis and rationale")

    # Recommendation
    recommendation: Literal["Strong Buy", "Buy", "Hold", "Pass"] = Field(
        description="Final investment recommendation"
    )
    recommended_investment_amount: Optional[float] = Field(
        None, description="Recommended investment amount in millions USD"
    )
    target_ownership: Optional[float] = Field(
        None, description="Target ownership percentage"
    )
    deal_terms_considerations: str = Field(
        description="Key considerations for deal terms and structure"
    )

    # Next steps
    next_steps: List[str] = Field(description="Recommended next steps for due diligence")
    additional_diligence_needed: List[str] = Field(
        description="Areas requiring additional investigation"
    )

    # Metadata
    analyzed_documents: List[str] = Field(
        default_factory=list,
        description="List of documents analyzed (pitch decks, financials, etc.)"
    )
    data_sources: List[str] = Field(
        default_factory=list,
        description="Data sources used in the analysis"
    )
    analyst_notes: Optional[str] = Field(
        None,
        description="Additional notes or commentary from the analysis"
    )


class ComparisonMetrics(BaseModel):
    """Simplified metrics for side-by-side company comparison"""
    company_name: str
    overall_score: int
    recommendation: str
    tam_millions: Optional[float]
    revenue_millions: Optional[float]
    revenue_growth: Optional[float]
    runway_months: Optional[int]
    market_score: int
    team_score: int
    product_score: int
    critical_risks_count: int
    high_risks_count: int
