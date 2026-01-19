"""
AI Due Diligence Agent Team - Streamlit Application

Professional investment due diligence platform with:
- Document upload and analysis
- Structured output with quantitative scoring
- PDF report generation
- Multi-company comparison dashboard
"""

import streamlit as st
import json
import os
from datetime import datetime
from pathlib import Path
import uuid

# Import agent components
from due_diligence_agent_team_structured import DueDiligenceTeamStructured
from models.schemas import DueDiligenceReport
from utils.report_generator import PDFReportGenerator
from utils.comparison import ComparisonDashboard
from utils.document_analyzer import DocumentAnalyzer

# Page configuration
st.set_page_config(
    page_title="AI Due Diligence Team",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1a237e;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f5f5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1976d2;
    }
    .recommendation-strong-buy {
        background-color: #2e7d32;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
    }
    .recommendation-buy {
        background-color: #558b2f;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
    }
    .recommendation-hold {
        background-color: #f57c00;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
    }
    .recommendation-pass {
        background-color: #c62828;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'reports' not in st.session_state:
    st.session_state.reports = []
if 'current_report' not in st.session_state:
    st.session_state.current_report = None
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []

# Sidebar
with st.sidebar:
    st.title("⚙️ Configuration")

    # API Key input
    api_key = st.text_input("OpenAI API Key", type="password", key="api_key")

    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key to proceed")
        st.stop()

    st.divider()

    # Mode selection
    mode = st.radio(
        "Select Mode",
        ["Single Company Analysis", "Compare Multiple Companies", "Saved Reports"],
        help="Choose what you want to do"
    )

    st.divider()

    # Document upload section
    if mode == "Single Company Analysis":
        st.subheader("📄 Upload Documents (Optional)")
        uploaded_files = st.file_uploader(
            "Pitch Deck, Financials, etc.",
            type=["pdf"],
            accept_multiple_files=True,
            help="Upload pitch decks, financial statements, or other due diligence documents"
        )

        if uploaded_files:
            st.session_state.uploaded_files = uploaded_files
            st.success(f"✓ {len(uploaded_files)} file(s) uploaded")

# Main content
st.markdown('<div class="main-header">📊 AI Due Diligence Team</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Professional Investment Analysis Platform</div>', unsafe_allow_html=True)

# MODE 1: Single Company Analysis
if mode == "Single Company Analysis":
    st.markdown("## 🔍 Analyze a Company")

    col1, col2 = st.columns([2, 1])

    with col1:
        company_name = st.text_input(
            "Company Name",
            placeholder="e.g., Stripe, Notion, Figma",
            help="Enter the name of the company you want to analyze"
        )

    with col2:
        analysis_depth = st.selectbox(
            "Analysis Depth",
            ["Standard", "Deep Dive"],
            help="Standard: Quick analysis | Deep Dive: Comprehensive research"
        )

    # Additional context
    additional_context = st.text_area(
        "Additional Context (Optional)",
        placeholder="E.g., Company stage, industry, specific concerns, focus areas...",
        help="Provide any additional context to guide the analysis"
    )

    # Advanced options
    with st.expander("🎛️ Advanced Options"):
        col_a, col_b = st.columns(2)
        with col_a:
            include_competitors = st.checkbox("Include Competitor Analysis", value=True)
            include_financials = st.checkbox("Deep Financial Analysis", value=True)
        with col_b:
            include_team = st.checkbox("Team Assessment", value=True)
            include_market = st.checkbox("Market Sizing", value=True)

    # Analysis button
    if st.button("🚀 Start Analysis", type="primary", use_container_width=True):
        if not company_name:
            st.error("❌ Please enter a company name")
        else:
            with st.spinner(f"🔬 Analyzing {company_name}... This may take 2-3 minutes..."):
                try:
                    # Initialize the due diligence team
                    dd_team = DueDiligenceTeamStructured(api_key=api_key)

                    # Process uploaded documents if any
                    document_context = ""
                    if st.session_state.uploaded_files:
                        st.info(f"📄 Processing {len(st.session_state.uploaded_files)} uploaded documents...")
                        doc_analyzer = DocumentAnalyzer()

                        # Save uploaded files
                        for uploaded_file in st.session_state.uploaded_files:
                            file_path = doc_analyzer.upload_dir / uploaded_file.name
                            with open(file_path, "wb") as f:
                                f.write(uploaded_file.getbuffer())

                        # Analyze documents
                        doc_agent = doc_analyzer.create_document_analysis_agent(
                            documents=[str(f) for f in st.session_state.uploaded_files],
                            api_key=api_key
                        )

                        # Extract key insights from documents
                        pitch_analysis = doc_analyzer.analyze_pitch_deck(doc_agent)
                        financial_analysis = doc_analyzer.analyze_financials(doc_agent)

                        document_context = f"""

                        DOCUMENT ANALYSIS:
                        {pitch_analysis['analysis']}

                        FINANCIAL DOCUMENT ANALYSIS:
                        {financial_analysis['financial_analysis']}
                        """

                    # Build analysis prompt
                    prompt = f"Perform a comprehensive due diligence analysis on {company_name}."

                    if additional_context:
                        prompt += f"\n\nAdditional Context: {additional_context}"

                    if document_context:
                        prompt += document_context

                    prompt += "\n\nProvide a complete investment analysis with structured output."

                    # Run analysis
                    report = dd_team.run_analysis(prompt)

                    if report:
                        st.session_state.current_report = report
                        st.session_state.reports.append(report)
                        st.success("✅ Analysis complete!")
                        st.rerun()
                    else:
                        st.error("❌ Analysis failed. Please try again.")

                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")
                    st.exception(e)

    # Display current report
    if st.session_state.current_report:
        report = st.session_state.current_report

        st.divider()

        # Recommendation banner
        rec_class = f"recommendation-{report.recommendation.lower().replace(' ', '-')}"
        st.markdown(f'<div class="{rec_class}">{report.recommendation}</div>', unsafe_allow_html=True)

        st.divider()

        # Key Metrics Row
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Overall Score",
                f"{report.investment_scores.overall_score}/100",
                delta=None
            )

        with col2:
            critical_risks = sum(1 for r in report.key_risks if r.severity == "Critical")
            st.metric("Critical Risks", critical_risks)

        with col3:
            if report.market_analysis.tam:
                st.metric("TAM", f"${report.market_analysis.tam:.0f}M")
            else:
                st.metric("TAM", "N/A")

        with col4:
            if report.financial_metrics.runway_months:
                st.metric("Runway", f"{report.financial_metrics.runway_months} mo")
            else:
                st.metric("Runway", "N/A")

        # Tabs for different sections
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📝 Executive Summary",
            "📊 Scores & Metrics",
            "💰 Financial Analysis",
            "📈 Market Analysis",
            "⚠️ Risk Assessment",
            "🎯 Recommendation"
        ])

        with tab1:
            st.markdown("### Executive Summary")
            st.write(report.executive_summary)

            st.markdown("### Investment Thesis")
            st.write(report.investment_thesis)

            st.markdown("### Company Profile")
            col_a, col_b = st.columns(2)
            with col_a:
                st.write(f"**Industry:** {report.company_profile.industry}")
                st.write(f"**Stage:** {report.company_profile.stage}")
                st.write(f"**Business Model:** {report.company_profile.business_model}")
            with col_b:
                if report.company_profile.founded_year:
                    st.write(f"**Founded:** {report.company_profile.founded_year}")
                if report.company_profile.headquarters:
                    st.write(f"**Location:** {report.company_profile.headquarters}")

            st.markdown(f"**Value Proposition:**\n{report.company_profile.value_proposition}")

        with tab2:
            st.markdown("### Investment Score Breakdown")

            # Create radar chart
            import plotly.graph_objects as go
            import numpy as np

            categories = ['Team', 'Market', 'Product', 'Financial', 'Execution']
            scores = [
                report.investment_scores.team_score,
                report.investment_scores.market_score,
                report.investment_scores.product_score,
                report.investment_scores.financial_score,
                report.investment_scores.execution_score
            ]

            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=scores,
                theta=categories,
                fill='toself',
                name='Investment Scores',
                line_color='#1976d2',
                fillcolor='rgba(25, 118, 210, 0.3)'
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=False,
                title=f"Overall Score: {report.investment_scores.overall_score}/100",
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)

            # Score rationales
            st.markdown("#### Score Rationales")
            with st.expander("📋 Team Score Details"):
                st.write(f"**Score: {report.investment_scores.team_score}/100**")
                st.write(report.investment_scores.team_rationale)

            with st.expander("📊 Market Score Details"):
                st.write(f"**Score: {report.investment_scores.market_score}/100**")
                st.write(report.investment_scores.market_rationale)

            with st.expander("🔧 Product Score Details"):
                st.write(f"**Score: {report.investment_scores.product_score}/100**")
                st.write(report.investment_scores.product_rationale)

            with st.expander("💰 Financial Score Details"):
                st.write(f"**Score: {report.investment_scores.financial_score}/100**")
                st.write(report.investment_scores.financial_rationale)

            with st.expander("🚀 Execution Score Details"):
                st.write(f"**Score: {report.investment_scores.execution_score}/100**")
                st.write(report.investment_scores.execution_rationale)

        with tab3:
            st.markdown("### Financial Metrics")

            # Financial metrics table
            metrics = report.financial_metrics

            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("#### Revenue & Growth")
                if metrics.revenue_current:
                    st.metric("Current Revenue", f"${metrics.revenue_current:.1f}M")
                if metrics.revenue_growth_yoy:
                    st.metric("YoY Growth", f"{metrics.revenue_growth_yoy:.1f}%")
                if metrics.arr_mrr:
                    st.metric("ARR/MRR", f"${metrics.arr_mrr:.1f}M")

            with col_b:
                st.markdown("#### Cash & Burn")
                if metrics.burn_rate_monthly:
                    st.metric("Monthly Burn", f"${metrics.burn_rate_monthly:.0f}K")
                if metrics.runway_months:
                    st.metric("Runway", f"{metrics.runway_months} months")
                if metrics.funding_raised_total:
                    st.metric("Total Funding", f"${metrics.funding_raised_total:.1f}M")

            col_c, col_d = st.columns(2)
            with col_c:
                st.markdown("#### Unit Economics")
                if metrics.cac_to_ltv_ratio:
                    st.metric("CAC/LTV Ratio", f"{metrics.cac_to_ltv_ratio:.2f}")
                if metrics.gross_margin:
                    st.metric("Gross Margin", f"{metrics.gross_margin:.1f}%")

            with col_d:
                st.markdown("#### Valuation")
                if metrics.last_valuation:
                    st.metric("Last Valuation", f"${metrics.last_valuation:.1f}M")
                if metrics.profitability_status:
                    st.write(f"**Status:** {metrics.profitability_status}")

        with tab4:
            st.markdown("### Market Analysis")

            # Market sizing
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                if report.market_analysis.tam:
                    st.metric("TAM", f"${report.market_analysis.tam:.0f}M")
            with col_b:
                if report.market_analysis.sam:
                    st.metric("SAM", f"${report.market_analysis.sam:.0f}M")
            with col_c:
                if report.market_analysis.som:
                    st.metric("SOM", f"${report.market_analysis.som:.0f}M")

            if report.market_analysis.market_growth_rate:
                st.metric("Market Growth Rate", f"{report.market_analysis.market_growth_rate:.1f}% annually")

            st.markdown("#### Target Customer Segment")
            st.write(report.market_analysis.target_customer_segment)

            st.markdown("#### Key Competitors")
            for competitor in report.market_analysis.key_competitors:
                st.write(f"• {competitor}")

            st.markdown("#### Competitive Advantages")
            for advantage in report.market_analysis.competitive_advantages:
                st.write(f"✓ {advantage}")

            st.markdown("#### Market Timing")
            st.write(report.market_analysis.market_timing)

        with tab5:
            st.markdown("### Risk Assessment")

            # Risk summary
            critical = sum(1 for r in report.key_risks if r.severity == "Critical")
            high = sum(1 for r in report.key_risks if r.severity == "High")
            medium = sum(1 for r in report.key_risks if r.severity == "Medium")
            low = sum(1 for r in report.key_risks if r.severity == "Low")

            col_a, col_b, col_c, col_d = st.columns(4)
            with col_a:
                st.metric("Critical", critical, delta=None, delta_color="inverse")
            with col_b:
                st.metric("High", high)
            with col_c:
                st.metric("Medium", medium)
            with col_d:
                st.metric("Low", low)

            # Risk details
            for risk in report.key_risks:
                severity_color = {
                    "Critical": "🔴",
                    "High": "🟠",
                    "Medium": "🟡",
                    "Low": "🟢"
                }
                icon = severity_color.get(risk.severity, "⚪")

                with st.expander(f"{icon} {risk.risk_name} ({risk.severity} - {risk.risk_category})"):
                    st.write(f"**Description:** {risk.description}")
                    st.write(f"**Impact:** {risk.impact} | **Probability:** {risk.probability}")
                    st.write(f"**Mitigation Strategy:** {risk.mitigation_strategy}")

        with tab6:
            st.markdown("### Investment Recommendation")

            rec_class = f"recommendation-{report.recommendation.lower().replace(' ', '-')}"
            st.markdown(f'<div class="{rec_class}">{report.recommendation}</div>', unsafe_allow_html=True)

            if report.recommended_investment_amount:
                st.write(f"**Recommended Investment Amount:** ${report.recommended_investment_amount:.1f}M")

            if report.target_ownership:
                st.write(f"**Target Ownership:** {report.target_ownership:.1f}%")

            st.markdown("#### Deal Terms Considerations")
            st.write(report.deal_terms_considerations)

            st.markdown("#### Next Steps")
            for step in report.next_steps:
                st.write(f"□ {step}")

            st.markdown("#### Additional Diligence Needed")
            for item in report.additional_diligence_needed:
                st.write(f"• {item}")

        # Export options
        st.divider()
        col_export1, col_export2, col_export3 = st.columns(3)

        with col_export1:
            # Export as JSON
            json_data = report.model_dump_json(indent=2)
            st.download_button(
                "📥 Export as JSON",
                data=json_data,
                file_name=f"{report.company_profile.company_name}_due_diligence.json",
                mime="application/json",
                use_container_width=True
            )

        with col_export2:
            # Generate PDF
            if st.button("📄 Generate PDF Report", use_container_width=True):
                with st.spinner("Generating PDF..."):
                    try:
                        pdf_gen = PDFReportGenerator()
                        pdf_path = f"/tmp/{report.report_id}_report.pdf"
                        pdf_gen.generate_report(report, pdf_path)

                        with open(pdf_path, "rb") as f:
                            st.download_button(
                                "📥 Download PDF",
                                data=f,
                                file_name=f"{report.company_profile.company_name}_due_diligence.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )
                        st.success("✅ PDF generated successfully!")
                    except Exception as e:
                        st.error(f"Error generating PDF: {str(e)}")

        with col_export3:
            if st.button("💾 Save to Reports", use_container_width=True):
                st.success("✅ Report saved! View in 'Saved Reports' mode")

# MODE 2: Compare Multiple Companies
elif mode == "Compare Multiple Companies":
    st.markdown("## 📊 Company Comparison Dashboard")

    if len(st.session_state.reports) < 2:
        st.info("ℹ️ You need at least 2 saved reports to use comparison mode. Analyze some companies first!")
    else:
        # Select companies to compare
        company_names = [r.company_profile.company_name for r in st.session_state.reports]
        selected = st.multiselect(
            "Select companies to compare",
            company_names,
            default=company_names[:min(3, len(company_names))]
        )

        if len(selected) < 2:
            st.warning("⚠️ Please select at least 2 companies to compare")
        else:
            # Filter reports
            selected_reports = [r for r in st.session_state.reports
                                if r.company_profile.company_name in selected]

            # Comparison dashboard
            dashboard = ComparisonDashboard()

            # Comparison table
            st.markdown("### 📋 Comparison Table")
            df = dashboard.create_comparison_dataframe(selected_reports)
            st.dataframe(df, use_container_width=True, hide_index=True)

            # Rankings
            st.markdown("### 🏆 Rankings")
            rankings = dashboard.rank_companies(selected_reports)
            st.dataframe(rankings[['Rank', 'Company', 'Overall Score', 'Recommendation', 'Stage']],
                         use_container_width=True, hide_index=True)

            # Charts
            st.markdown("### 📈 Comparison Charts")

            tab1, tab2, tab3, tab4 = st.tabs([
                "Overall Scores",
                "Dimension Scores",
                "Risk Profiles",
                "Financial Metrics"
            ])

            with tab1:
                fig = dashboard.create_score_comparison_chart(selected_reports)
                st.pyplot(fig)

            with tab2:
                fig = dashboard.create_dimension_comparison_chart(selected_reports)
                st.pyplot(fig)

            with tab3:
                fig = dashboard.create_risk_comparison_chart(selected_reports)
                st.pyplot(fig)

            with tab4:
                fig = dashboard.create_financial_comparison_chart(selected_reports)
                st.pyplot(fig)

# MODE 3: Saved Reports
elif mode == "Saved Reports":
    st.markdown("## 💾 Saved Reports")

    if not st.session_state.reports:
        st.info("ℹ️ No saved reports yet. Analyze some companies to get started!")
    else:
        st.write(f"📊 Total Reports: {len(st.session_state.reports)}")

        for i, report in enumerate(st.session_state.reports):
            with st.expander(f"{report.company_profile.company_name} - {report.recommendation} ({report.analysis_date})"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Overall Score", f"{report.investment_scores.overall_score}/100")
                with col2:
                    st.metric("Recommendation", report.recommendation)
                with col3:
                    critical = sum(1 for r in report.key_risks if r.severity == "Critical")
                    st.metric("Critical Risks", critical)

                if st.button(f"View Full Report", key=f"view_{i}"):
                    st.session_state.current_report = report
                    st.rerun()

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #757575; padding: 2rem;">
    <strong>AI Due Diligence Team</strong> | Powered by GPT-4o & Agno Framework<br>
    Professional Investment Analysis Platform
</div>
""", unsafe_allow_html=True)
