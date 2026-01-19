"""
Professional PDF Report Generator

Generates comprehensive due diligence reports with:
- Executive summary
- Investment score visualizations
- Financial metrics tables
- Risk heat maps
- Market analysis charts
"""

import io
from typing import List
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
import pandas as pd
import numpy as np

from models.schemas import DueDiligenceReport, RiskAssessment


class PDFReportGenerator:
    """Generate professional investment due diligence PDF reports"""

    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()

    def _create_custom_styles(self):
        """Create custom paragraph styles for the report"""
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1a237e'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#283593'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='Recommendation',
            parent=self.styles['Normal'],
            fontSize=18,
            textColor=colors.white,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            spaceAfter=20
        ))

    def _get_recommendation_color(self, recommendation: str) -> colors.Color:
        """Get color based on recommendation"""
        color_map = {
            "Strong Buy": colors.HexColor('#2e7d32'),  # Green
            "Buy": colors.HexColor('#558b2f'),  # Light green
            "Hold": colors.HexColor('#f57c00'),  # Orange
            "Pass": colors.HexColor('#c62828')  # Red
        }
        return color_map.get(recommendation, colors.grey)

    def _create_score_chart(self, report: DueDiligenceReport) -> str:
        """Create radar chart for investment scores"""
        scores = report.investment_scores

        categories = ['Team', 'Market', 'Product', 'Financial', 'Execution']
        values = [
            scores.team_score,
            scores.market_score,
            scores.product_score,
            scores.financial_score,
            scores.execution_score
        ]

        # Create radar chart
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        values += values[:1]  # Complete the circle
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
        ax.plot(angles, values, 'o-', linewidth=2, color='#1976d2')
        ax.fill(angles, values, alpha=0.25, color='#1976d2')
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, size=10)
        ax.set_ylim(0, 100)
        ax.set_yticks([25, 50, 75, 100])
        ax.set_yticklabels(['25', '50', '75', '100'], size=8)
        ax.grid(True)
        ax.set_title(f'Investment Score: {scores.overall_score}/100',
                     size=14, weight='bold', pad=20)

        # Save to bytes
        img_buffer = io.BytesIO()
        plt.tight_layout()
        plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight')
        plt.close()
        img_buffer.seek(0)

        # Save to temp file for ReportLab
        temp_path = f'/tmp/score_chart_{report.report_id}.png'
        with open(temp_path, 'wb') as f:
            f.write(img_buffer.getvalue())

        return temp_path

    def _create_risk_heatmap(self, risks: List[RiskAssessment]) -> str:
        """Create risk heat map visualization"""
        if not risks:
            return None

        # Create matrix data
        impact_map = {'High': 3, 'Medium': 2, 'Low': 1}
        prob_map = {'High': 3, 'Medium': 2, 'Low': 1}

        matrix = np.zeros((3, 3))
        risk_labels = {}

        for risk in risks:
            i = 3 - impact_map[risk.impact]  # Flip for correct orientation
            j = prob_map[risk.probability] - 1
            matrix[i, j] += 1
            key = (i, j)
            if key not in risk_labels:
                risk_labels[key] = []
            risk_labels[key].append(risk.risk_name[:20])

        # Create heatmap
        fig, ax = plt.subplots(figsize=(7, 5))
        sns.heatmap(matrix, annot=True, fmt='.0f', cmap='YlOrRd',
                    cbar_kws={'label': 'Number of Risks'},
                    xticklabels=['Low', 'Medium', 'High'],
                    yticklabels=['High', 'Medium', 'Low'],
                    linewidths=1, linecolor='white')

        ax.set_xlabel('Probability', weight='bold', size=11)
        ax.set_ylabel('Impact', weight='bold', size=11)
        ax.set_title('Risk Heat Map', weight='bold', size=13, pad=15)

        # Save to temp file
        temp_path = f'/tmp/risk_heatmap_{datetime.now().timestamp()}.png'
        plt.tight_layout()
        plt.savefig(temp_path, format='png', dpi=150, bbox_inches='tight')
        plt.close()

        return temp_path

    def _create_financial_table(self, metrics) -> Table:
        """Create formatted financial metrics table"""
        data = [
            ['Metric', 'Value'],
            ['Current Revenue', f"${metrics.revenue_current:.1f}M" if metrics.revenue_current else "N/A"],
            ['Revenue Growth (YoY)', f"{metrics.revenue_growth_yoy:.1f}%" if metrics.revenue_growth_yoy else "N/A"],
            ['Monthly Burn Rate', f"${metrics.burn_rate_monthly:.0f}K" if metrics.burn_rate_monthly else "N/A"],
            ['Runway', f"{metrics.runway_months} months" if metrics.runway_months else "N/A"],
            ['CAC/LTV Ratio', f"{metrics.cac_to_ltv_ratio:.2f}" if metrics.cac_to_ltv_ratio else "N/A"],
            ['Gross Margin', f"{metrics.gross_margin:.1f}%" if metrics.gross_margin else "N/A"],
            ['Total Funding Raised', f"${metrics.funding_raised_total:.1f}M" if metrics.funding_raised_total else "N/A"],
            ['Last Valuation', f"${metrics.last_valuation:.1f}M" if metrics.last_valuation else "N/A"],
        ]

        table = Table(data, colWidths=[3*inch, 2*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#283593')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')])
        ]))

        return table

    def _create_risk_table(self, risks: List[RiskAssessment]) -> Table:
        """Create formatted risk assessment table"""
        if not risks:
            return Paragraph("No specific risks identified.", self.styles['Normal'])

        # Sort by severity
        severity_order = {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3}
        sorted_risks = sorted(risks, key=lambda r: severity_order[r.severity])

        data = [['Severity', 'Risk', 'Category', 'Mitigation']]

        for risk in sorted_risks[:10]:  # Top 10 risks
            data.append([
                risk.severity,
                Paragraph(risk.risk_name[:40], self.styles['Normal']),
                risk.risk_category,
                Paragraph(risk.mitigation_strategy[:100] + '...', self.styles['Normal'])
            ])

        table = Table(data, colWidths=[0.8*inch, 2*inch, 1*inch, 2.5*inch])

        # Color code severity
        style_commands = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#283593')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]

        # Add severity colors
        for i, risk in enumerate(sorted_risks[:10], 1):
            if risk.severity == 'Critical':
                style_commands.append(('BACKGROUND', (0, i), (0, i), colors.HexColor('#ffcdd2')))
            elif risk.severity == 'High':
                style_commands.append(('BACKGROUND', (0, i), (0, i), colors.HexColor('#ffe0b2')))

        table.setStyle(TableStyle(style_commands))
        return table

    def generate_report(self, report: DueDiligenceReport, output_path: str) -> str:
        """Generate complete PDF report"""
        doc = SimpleDocTemplate(output_path, pagesize=letter,
                                topMargin=0.75*inch, bottomMargin=0.75*inch)
        story = []

        # Title Page
        story.append(Spacer(1, 0.5*inch))
        story.append(Paragraph(
            "Due Diligence Report",
            self.styles['CustomTitle']
        ))
        story.append(Paragraph(
            report.company_profile.company_name,
            self.styles['CustomTitle']
        ))
        story.append(Spacer(1, 0.3*inch))

        # Recommendation badge
        rec_color = self._get_recommendation_color(report.recommendation)
        rec_table = Table([[Paragraph(report.recommendation, self.styles['Recommendation'])]],
                          colWidths=[3*inch])
        rec_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), rec_color),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 15),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
            ('ROUNDEDCORNERS', [10, 10, 10, 10]),
        ]))
        story.append(rec_table)
        story.append(Spacer(1, 0.3*inch))

        # Report metadata
        metadata_text = f"""
        <b>Report ID:</b> {report.report_id}<br/>
        <b>Analysis Date:</b> {report.analysis_date}<br/>
        <b>Investment Stage:</b> {report.company_profile.stage}<br/>
        <b>Overall Score:</b> {report.investment_scores.overall_score}/100
        """
        story.append(Paragraph(metadata_text, self.styles['Normal']))
        story.append(PageBreak())

        # Executive Summary
        story.append(Paragraph("Executive Summary", self.styles['SectionHeader']))
        story.append(Paragraph(report.executive_summary, self.styles['BodyText']))
        story.append(Spacer(1, 0.2*inch))

        story.append(Paragraph("Investment Thesis", self.styles['SectionHeader']))
        story.append(Paragraph(report.investment_thesis, self.styles['BodyText']))
        story.append(PageBreak())

        # Investment Scores with Radar Chart
        story.append(Paragraph("Investment Score Analysis", self.styles['SectionHeader']))

        # Add radar chart
        chart_path = self._create_score_chart(report)
        if chart_path:
            img = Image(chart_path, width=4.5*inch, height=4.5*inch)
            story.append(img)
            story.append(Spacer(1, 0.2*inch))

        # Score rationales
        scores = report.investment_scores
        rationale_text = f"""
        <b>Team ({scores.team_score}/100):</b> {scores.team_rationale}<br/><br/>
        <b>Market ({scores.market_score}/100):</b> {scores.market_rationale}<br/><br/>
        <b>Product ({scores.product_score}/100):</b> {scores.product_rationale}<br/><br/>
        <b>Financial ({scores.financial_score}/100):</b> {scores.financial_rationale}<br/><br/>
        <b>Execution ({scores.execution_score}/100):</b> {scores.execution_rationale}
        """
        story.append(Paragraph(rationale_text, self.styles['BodyText']))
        story.append(PageBreak())

        # Company Profile
        story.append(Paragraph("Company Profile", self.styles['SectionHeader']))
        profile = report.company_profile
        profile_text = f"""
        <b>Founded:</b> {profile.founded_year or 'N/A'}<br/>
        <b>Headquarters:</b> {profile.headquarters or 'N/A'}<br/>
        <b>Industry:</b> {profile.industry}<br/>
        <b>Business Model:</b> {profile.business_model}<br/><br/>
        <b>Elevator Pitch:</b><br/>
        {profile.elevator_pitch}<br/><br/>
        <b>Value Proposition:</b><br/>
        {profile.value_proposition}<br/><br/>
        <b>Key Products:</b><br/>
        {'<br/>'.join('• ' + p for p in profile.key_products)}<br/><br/>
        <b>Traction:</b><br/>
        {profile.traction_metrics}
        """
        story.append(Paragraph(profile_text, self.styles['BodyText']))
        story.append(Spacer(1, 0.3*inch))

        # Financial Metrics
        story.append(Paragraph("Financial Analysis", self.styles['SectionHeader']))
        story.append(self._create_financial_table(report.financial_metrics))
        story.append(PageBreak())

        # Market Analysis
        story.append(Paragraph("Market Analysis", self.styles['SectionHeader']))
        market = report.market_analysis
        market_text = f"""
        <b>Market Size:</b><br/>
        • TAM: ${market.tam:.0f}M<br/>
        • SAM: ${market.sam:.0f}M<br/>
        • SOM: ${market.som:.0f}M<br/>
        • Growth Rate: {market.market_growth_rate:.1f}% annually<br/><br/>
        <b>Target Segment:</b> {market.target_customer_segment}<br/><br/>
        <b>Key Competitors:</b><br/>
        {'<br/>'.join('• ' + c for c in market.key_competitors)}<br/><br/>
        <b>Competitive Advantages:</b><br/>
        {'<br/>'.join('• ' + a for a in market.competitive_advantages)}<br/><br/>
        <b>Market Timing:</b><br/>
        {market.market_timing}<br/><br/>
        <b>Barriers to Entry:</b><br/>
        {market.barriers_to_entry}
        """
        story.append(Paragraph(market_text, self.styles['BodyText']))
        story.append(PageBreak())

        # Risk Assessment
        story.append(Paragraph("Risk Assessment", self.styles['SectionHeader']))

        # Risk heatmap
        heatmap_path = self._create_risk_heatmap(report.key_risks)
        if heatmap_path:
            img = Image(heatmap_path, width=5*inch, height=3.5*inch)
            story.append(img)
            story.append(Spacer(1, 0.2*inch))

        # Risk table
        story.append(self._create_risk_table(report.key_risks))
        story.append(PageBreak())

        # Recommendation & Next Steps
        story.append(Paragraph("Investment Recommendation", self.styles['SectionHeader']))
        rec_text = f"""
        <b>Recommendation:</b> {report.recommendation}<br/><br/>
        """
        if report.recommended_investment_amount:
            rec_text += f"<b>Recommended Investment:</b> ${report.recommended_investment_amount:.1f}M<br/>"
        if report.target_ownership:
            rec_text += f"<b>Target Ownership:</b> {report.target_ownership:.1f}%<br/><br/>"

        rec_text += f"""
        <b>Deal Terms Considerations:</b><br/>
        {report.deal_terms_considerations}<br/><br/>
        <b>Next Steps:</b><br/>
        {'<br/>'.join('• ' + step for step in report.next_steps)}<br/><br/>
        <b>Additional Diligence Needed:</b><br/>
        {'<br/>'.join('• ' + item for item in report.additional_diligence_needed)}
        """
        story.append(Paragraph(rec_text, self.styles['BodyText']))

        # Build PDF
        doc.build(story)
        return output_path
