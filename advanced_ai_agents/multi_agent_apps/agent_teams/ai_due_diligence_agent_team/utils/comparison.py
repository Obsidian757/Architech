"""
Company Comparison Dashboard

Enables side-by-side comparison of multiple companies
for portfolio decision-making.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List
import numpy as np

from models.schemas import DueDiligenceReport, ComparisonMetrics


class ComparisonDashboard:
    """Generate comparison views for multiple companies"""

    @staticmethod
    def extract_comparison_metrics(report: DueDiligenceReport) -> ComparisonMetrics:
        """Extract key metrics for comparison"""
        critical_risks = sum(1 for r in report.key_risks if r.severity == "Critical")
        high_risks = sum(1 for r in report.key_risks if r.severity == "High")

        return ComparisonMetrics(
            company_name=report.company_profile.company_name,
            overall_score=report.investment_scores.overall_score,
            recommendation=report.recommendation,
            tam_millions=report.market_analysis.tam,
            revenue_millions=report.financial_metrics.revenue_current,
            revenue_growth=report.financial_metrics.revenue_growth_yoy,
            runway_months=report.financial_metrics.runway_months,
            market_score=report.investment_scores.market_score,
            team_score=report.investment_scores.team_score,
            product_score=report.investment_scores.product_score,
            critical_risks_count=critical_risks,
            high_risks_count=high_risks
        )

    @staticmethod
    def create_comparison_dataframe(reports: List[DueDiligenceReport]) -> pd.DataFrame:
        """
        Create comparison DataFrame from multiple reports.

        Args:
            reports: List of due diligence reports

        Returns:
            DataFrame with key comparison metrics
        """
        comparison_data = []

        for report in reports:
            metrics = ComparisonDashboard.extract_comparison_metrics(report)
            comparison_data.append({
                'Company': metrics.company_name,
                'Recommendation': metrics.recommendation,
                'Overall Score': metrics.overall_score,
                'Team': metrics.team_score,
                'Market': metrics.market_score,
                'Product': metrics.product_score,
                'TAM ($M)': f"${metrics.tam_millions:.0f}M" if metrics.tam_millions else "N/A",
                'Revenue ($M)': f"${metrics.revenue_millions:.1f}M" if metrics.revenue_millions else "N/A",
                'Growth (%)': f"{metrics.revenue_growth:.0f}%" if metrics.revenue_growth else "N/A",
                'Runway (mo)': metrics.runway_months if metrics.runway_months else "N/A",
                'Critical Risks': metrics.critical_risks_count,
                'High Risks': metrics.high_risks_count,
            })

        return pd.DataFrame(comparison_data)

    @staticmethod
    def create_score_comparison_chart(reports: List[DueDiligenceReport]) -> plt.Figure:
        """
        Create bar chart comparing overall scores.

        Args:
            reports: List of due diligence reports

        Returns:
            Matplotlib figure
        """
        companies = [r.company_profile.company_name for r in reports]
        scores = [r.investment_scores.overall_score for r in reports]
        recommendations = [r.recommendation for r in reports]

        # Color code by recommendation
        color_map = {
            "Strong Buy": '#2e7d32',
            "Buy": '#558b2f',
            "Hold": '#f57c00',
            "Pass": '#c62828'
        }
        colors = [color_map.get(rec, '#757575') for rec in recommendations]

        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(companies, scores, color=colors, alpha=0.8)

        ax.set_xlabel('Overall Investment Score', fontsize=12, weight='bold')
        ax.set_title('Company Comparison - Investment Scores', fontsize=14, weight='bold', pad=20)
        ax.set_xlim(0, 100)
        ax.grid(axis='x', alpha=0.3)

        # Add score labels
        for i, (bar, score, rec) in enumerate(zip(bars, scores, recommendations)):
            ax.text(score + 2, i, f'{score} ({rec})', va='center', fontsize=10)

        plt.tight_layout()
        return fig

    @staticmethod
    def create_dimension_comparison_chart(reports: List[DueDiligenceReport]) -> plt.Figure:
        """
        Create grouped bar chart comparing score dimensions.

        Args:
            reports: List of due diligence reports

        Returns:
            Matplotlib figure
        """
        companies = [r.company_profile.company_name[:20] for r in reports]

        # Extract dimension scores
        team_scores = [r.investment_scores.team_score for r in reports]
        market_scores = [r.investment_scores.market_score for r in reports]
        product_scores = [r.investment_scores.product_score for r in reports]
        financial_scores = [r.investment_scores.financial_score for r in reports]
        execution_scores = [r.investment_scores.execution_score for r in reports]

        x = np.arange(len(companies))
        width = 0.15

        fig, ax = plt.subplots(figsize=(12, 6))

        ax.bar(x - 2*width, team_scores, width, label='Team', color='#1976d2', alpha=0.8)
        ax.bar(x - width, market_scores, width, label='Market', color='#388e3c', alpha=0.8)
        ax.bar(x, product_scores, width, label='Product', color='#f57c00', alpha=0.8)
        ax.bar(x + width, financial_scores, width, label='Financial', color='#7b1fa2', alpha=0.8)
        ax.bar(x + 2*width, execution_scores, width, label='Execution', color='#c62828', alpha=0.8)

        ax.set_ylabel('Score', fontsize=12, weight='bold')
        ax.set_title('Multi-Dimensional Score Comparison', fontsize=14, weight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(companies, rotation=45, ha='right')
        ax.legend(loc='upper left', framealpha=0.9)
        ax.set_ylim(0, 100)
        ax.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        return fig

    @staticmethod
    def create_risk_comparison_chart(reports: List[DueDiligenceReport]) -> plt.Figure:
        """
        Create stacked bar chart comparing risk profiles.

        Args:
            reports: List of due diligence reports

        Returns:
            Matplotlib figure
        """
        companies = [r.company_profile.company_name[:20] for r in reports]

        critical = []
        high = []
        medium = []
        low = []

        for report in reports:
            critical.append(sum(1 for r in report.key_risks if r.severity == "Critical"))
            high.append(sum(1 for r in report.key_risks if r.severity == "High"))
            medium.append(sum(1 for r in report.key_risks if r.severity == "Medium"))
            low.append(sum(1 for r in report.key_risks if r.severity == "Low"))

        fig, ax = plt.subplots(figsize=(10, 6))

        x = np.arange(len(companies))
        width = 0.6

        p1 = ax.bar(x, critical, width, label='Critical', color='#c62828')
        p2 = ax.bar(x, high, width, bottom=critical, label='High', color='#f57c00')
        p3 = ax.bar(x, medium, width, bottom=np.array(critical)+np.array(high),
                    label='Medium', color='#fbc02d')
        p4 = ax.bar(x, low, width,
                    bottom=np.array(critical)+np.array(high)+np.array(medium),
                    label='Low', color='#388e3c')

        ax.set_ylabel('Number of Risks', fontsize=12, weight='bold')
        ax.set_title('Risk Profile Comparison', fontsize=14, weight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(companies, rotation=45, ha='right')
        ax.legend(loc='upper left', framealpha=0.9)
        ax.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        return fig

    @staticmethod
    def create_financial_comparison_chart(reports: List[DueDiligenceReport]) -> plt.Figure:
        """
        Create comparison chart for key financial metrics.

        Args:
            reports: List of due diligence reports

        Returns:
            Matplotlib figure
        """
        companies = [r.company_profile.company_name[:20] for r in reports]

        # Extract financial metrics
        revenues = [r.financial_metrics.revenue_current or 0 for r in reports]
        growth_rates = [r.financial_metrics.revenue_growth_yoy or 0 for r in reports]
        runways = [r.financial_metrics.runway_months or 0 for r in reports]

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

        # Revenue chart
        ax1.bar(companies, revenues, color='#1976d2', alpha=0.7)
        ax1.set_ylabel('Revenue ($M)', fontsize=11, weight='bold')
        ax1.set_title('Current Revenue', fontsize=12, weight='bold')
        ax1.tick_params(axis='x', rotation=45)
        ax1.grid(axis='y', alpha=0.3)

        # Growth rate chart
        colors_growth = ['#2e7d32' if g > 100 else '#f57c00' if g > 50 else '#c62828'
                         for g in growth_rates]
        ax2.bar(companies, growth_rates, color=colors_growth, alpha=0.7)
        ax2.set_ylabel('Growth Rate (%)', fontsize=11, weight='bold')
        ax2.set_title('YoY Revenue Growth', fontsize=12, weight='bold')
        ax2.tick_params(axis='x', rotation=45)
        ax2.axhline(y=100, color='green', linestyle='--', alpha=0.5, label='100% growth')
        ax2.grid(axis='y', alpha=0.3)

        # Runway chart
        colors_runway = ['#2e7d32' if r >= 18 else '#f57c00' if r >= 12 else '#c62828'
                         for r in runways]
        ax3.bar(companies, runways, color=colors_runway, alpha=0.7)
        ax3.set_ylabel('Runway (months)', fontsize=11, weight='bold')
        ax3.set_title('Cash Runway', fontsize=12, weight='bold')
        ax3.tick_params(axis='x', rotation=45)
        ax3.axhline(y=18, color='green', linestyle='--', alpha=0.5, label='18 mo target')
        ax3.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        return fig

    @staticmethod
    def rank_companies(reports: List[DueDiligenceReport]) -> pd.DataFrame:
        """
        Rank companies by overall score and recommendation.

        Args:
            reports: List of due diligence reports

        Returns:
            Ranked DataFrame
        """
        ranking_data = []

        for i, report in enumerate(reports, 1):
            critical_risks = sum(1 for r in report.key_risks if r.severity == "Critical")

            ranking_data.append({
                'Rank': i,
                'Company': report.company_profile.company_name,
                'Overall Score': report.investment_scores.overall_score,
                'Recommendation': report.recommendation,
                'Stage': report.company_profile.stage,
                'Critical Risks': critical_risks,
                'TAM ($M)': report.market_analysis.tam,
                'Investment Thesis': report.investment_thesis[:100] + '...'
            })

        df = pd.DataFrame(ranking_data)
        # Sort by overall score descending
        df = df.sort_values('Overall Score', ascending=False).reset_index(drop=True)
        df['Rank'] = range(1, len(df) + 1)

        return df
