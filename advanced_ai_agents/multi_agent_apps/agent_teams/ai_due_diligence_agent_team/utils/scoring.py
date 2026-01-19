"""
Investment Scoring Framework

Calculates quantitative investment scores based on multiple factors.
Each dimension is scored 0-100, with weighted overall score.
"""

from typing import Dict, Tuple
from models.schemas import InvestmentScore, FinancialMetrics, RiskAssessment


class InvestmentScoringFramework:
    """
    Investment scoring system based on venture capital best practices.

    Scoring Dimensions:
    - Team (25% weight): Experience, execution capability, completeness
    - Market (25% weight): Size, growth, timing, competition
    - Product (20% weight): Differentiation, technical moat, scalability
    - Financial (20% weight): Unit economics, growth, capital efficiency
    - Execution (10% weight): Traction, milestones, momentum
    """

    WEIGHTS = {
        "team": 0.25,
        "market": 0.25,
        "product": 0.20,
        "financial": 0.20,
        "execution": 0.10
    }

    @staticmethod
    def calculate_financial_score(metrics: FinancialMetrics) -> Tuple[int, str]:
        """
        Calculate financial health score based on key metrics.

        Scoring factors:
        - Revenue growth rate (30 points)
        - Unit economics (CAC/LTV) (25 points)
        - Runway (20 points)
        - Gross margins (15 points)
        - Burn efficiency (10 points)
        """
        score = 0
        rationale_parts = []

        # Revenue growth (30 points max)
        if metrics.revenue_growth_yoy:
            if metrics.revenue_growth_yoy >= 200:
                score += 30
                rationale_parts.append(f"Exceptional {metrics.revenue_growth_yoy}% YoY growth")
            elif metrics.revenue_growth_yoy >= 100:
                score += 25
                rationale_parts.append(f"Strong {metrics.revenue_growth_yoy}% YoY growth")
            elif metrics.revenue_growth_yoy >= 50:
                score += 20
                rationale_parts.append(f"Solid {metrics.revenue_growth_yoy}% YoY growth")
            elif metrics.revenue_growth_yoy >= 20:
                score += 15
                rationale_parts.append(f"Moderate {metrics.revenue_growth_yoy}% YoY growth")
            else:
                score += 10
                rationale_parts.append(f"Limited {metrics.revenue_growth_yoy}% YoY growth")
        else:
            score += 15
            rationale_parts.append("Revenue growth data not available")

        # Unit economics - CAC/LTV ratio (25 points max)
        if metrics.cac_to_ltv_ratio:
            if metrics.cac_to_ltv_ratio <= 0.33:  # LTV > 3x CAC
                score += 25
                rationale_parts.append(f"Excellent unit economics (CAC/LTV: {metrics.cac_to_ltv_ratio:.2f})")
            elif metrics.cac_to_ltv_ratio <= 0.5:  # LTV > 2x CAC
                score += 20
                rationale_parts.append(f"Good unit economics (CAC/LTV: {metrics.cac_to_ltv_ratio:.2f})")
            elif metrics.cac_to_ltv_ratio <= 1.0:
                score += 10
                rationale_parts.append(f"Marginal unit economics (CAC/LTV: {metrics.cac_to_ltv_ratio:.2f})")
            else:
                score += 5
                rationale_parts.append(f"Concerning unit economics (CAC/LTV: {metrics.cac_to_ltv_ratio:.2f})")
        else:
            score += 12
            rationale_parts.append("Unit economics data not available")

        # Runway (20 points max)
        if metrics.runway_months:
            if metrics.runway_months >= 24:
                score += 20
                rationale_parts.append(f"Strong {metrics.runway_months} months runway")
            elif metrics.runway_months >= 18:
                score += 18
                rationale_parts.append(f"Good {metrics.runway_months} months runway")
            elif metrics.runway_months >= 12:
                score += 15
                rationale_parts.append(f"Adequate {metrics.runway_months} months runway")
            elif metrics.runway_months >= 6:
                score += 10
                rationale_parts.append(f"Limited {metrics.runway_months} months runway")
            else:
                score += 5
                rationale_parts.append(f"Critical runway concern: {metrics.runway_months} months")
        else:
            score += 10
            rationale_parts.append("Runway data not available")

        # Gross margins (15 points max)
        if metrics.gross_margin:
            if metrics.gross_margin >= 80:
                score += 15
                rationale_parts.append(f"Exceptional {metrics.gross_margin}% gross margins")
            elif metrics.gross_margin >= 70:
                score += 13
                rationale_parts.append(f"Strong {metrics.gross_margin}% gross margins")
            elif metrics.gross_margin >= 50:
                score += 10
                rationale_parts.append(f"Solid {metrics.gross_margin}% gross margins")
            else:
                score += 5
                rationale_parts.append(f"Low {metrics.gross_margin}% gross margins")
        else:
            score += 8
            rationale_parts.append("Gross margin data not available")

        # Burn efficiency (10 points max)
        # If revenue growing faster than burn, good. If profitable, excellent.
        if metrics.profitability_status:
            if "profitable" in metrics.profitability_status.lower():
                score += 10
                rationale_parts.append("Already profitable - excellent burn efficiency")
            elif "break-even" in metrics.profitability_status.lower():
                score += 8
                rationale_parts.append("At break-even - good capital efficiency")
            else:
                score += 5
                rationale_parts.append("Still burning cash")
        else:
            score += 5

        rationale = "; ".join(rationale_parts)
        return min(score, 100), rationale

    @staticmethod
    def calculate_risk_impact_score(risks: list[RiskAssessment]) -> int:
        """
        Calculate score reduction based on identified risks.
        Returns a value 0-30 representing risk penalty.
        """
        penalty = 0

        critical_count = sum(1 for r in risks if r.severity == "Critical")
        high_count = sum(1 for r in risks if r.severity == "High")
        medium_count = sum(1 for r in risks if r.severity == "Medium")

        # Each critical risk: -10 points (up to 3)
        penalty += min(critical_count * 10, 30)

        # Each high risk: -5 points (up to 3)
        penalty += min(high_count * 5, 15)

        # Each medium risk: -2 points (up to 5)
        penalty += min(medium_count * 2, 10)

        return min(penalty, 30)

    @staticmethod
    def calculate_overall_score(
        team_score: int,
        market_score: int,
        product_score: int,
        financial_score: int,
        execution_score: int,
        risks: list[RiskAssessment] = None
    ) -> int:
        """
        Calculate weighted overall investment score.
        """
        weighted = (
            team_score * InvestmentScoringFramework.WEIGHTS["team"] +
            market_score * InvestmentScoringFramework.WEIGHTS["market"] +
            product_score * InvestmentScoringFramework.WEIGHTS["product"] +
            financial_score * InvestmentScoringFramework.WEIGHTS["financial"] +
            execution_score * InvestmentScoringFramework.WEIGHTS["execution"]
        )

        # Apply risk penalty
        if risks:
            risk_penalty = InvestmentScoringFramework.calculate_risk_impact_score(risks)
            weighted = max(0, weighted - risk_penalty)

        return int(round(weighted))

    @staticmethod
    def get_recommendation(overall_score: int, critical_risks: int) -> str:
        """
        Determine investment recommendation based on score and risks.

        Score Ranges:
        - 80-100: Strong Buy (exceptional opportunity)
        - 65-79: Buy (good opportunity)
        - 50-64: Hold (needs more diligence)
        - 0-49: Pass (does not meet bar)

        Any critical risks automatically downgrade to Hold or Pass.
        """
        if critical_risks > 0:
            return "Pass" if overall_score < 70 else "Hold"

        if overall_score >= 80:
            return "Strong Buy"
        elif overall_score >= 65:
            return "Buy"
        elif overall_score >= 50:
            return "Hold"
        else:
            return "Pass"
