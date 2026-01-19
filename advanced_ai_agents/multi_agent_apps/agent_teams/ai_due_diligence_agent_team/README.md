# 📊 AI Due Diligence Agent Team - Professional Edition

A production-ready multi-agent AI system that performs institutional-grade due diligence analysis for startup investments. Built with GPT-4o and powered by the Agno framework, this platform delivers structured investment reports with quantitative scoring, PDF exports, and portfolio comparison capabilities.

## 🌟 What Makes This Professional-Grade?

This is not just another AI chatbot - it's a complete investment analysis platform used by VCs:

1. **Structured Data Output** - Returns Pydantic models, not just text
2. **Quantitative Scoring** - 0-100 scoring framework across 5 dimensions
3. **Document Analysis** - Processes pitch decks, financials, and cap tables with RAG
4. **PDF Report Generation** - Professional reports with charts and visualizations
5. **Portfolio Comparison** - Side-by-side analysis of multiple companies
6. **Interactive UI** - Streamlit dashboard with file upload and export

## 🎯 System Architecture

### Multi-Agent Team Structure

```
┌─────────────────────────────────────────────────┐
│      Due Diligence Orchestrator Agent           │
│   (Coordinates & Synthesizes All Findings)      │
└──────────────┬──────────────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
   ┌───▼────┐    ┌────▼────┐
   │Company │    │Financial│
   │Research│    │Analysis │
   │ Agent  │    │  Agent  │
   └───┬────┘    └────┬────┘
       │              │
   ┌───▼────┐    ┌────▼────┐
   │ Market │    │  Risk   │
   │Analysis│    │Assessment│
   │ Agent  │    │  Agent  │
   └────────┘    └──────────┘
```

### Specialized Agents

1. **Company Research Agent**
   - Tools: DuckDuckGo Search
   - Outputs: Company profile, team assessment, traction metrics
   - Extracts: Founding story, products, funding history, news

2. **Financial Analysis Agent**
   - Tools: YFinance, DuckDuckGo
   - Outputs: Financial metrics, unit economics, sustainability analysis
   - Calculates: Revenue growth, burn rate, CAC/LTV, gross margins

3. **Market Analysis Agent**
   - Tools: DuckDuckGo Search
   - Outputs: Market sizing, competitive landscape, timing assessment
   - Analyzes: TAM/SAM/SOM, competitors, trends, barriers

4. **Risk Assessment Agent**
   - Tools: DuckDuckGo Search
   - Outputs: Categorized risks with severity, impact, and mitigation
   - Identifies: Market, technology, team, financial, regulatory risks

5. **Document Analysis Agent** (Optional)
   - Tools: PyPDF2, RAG Knowledge Base
   - Outputs: Extracted data from pitch decks and financials
   - Validates: Claims, metrics, and projections in documents

## ✨ Key Features

### 1. Structured Output with Pydantic Schemas

All reports use strongly-typed Pydantic models:

```python
class DueDiligenceReport(BaseModel):
    company_profile: CompanyProfile
    team_assessment: TeamAssessment
    market_analysis: MarketAnalysis
    financial_metrics: FinancialMetrics
    investment_scores: InvestmentScore
    key_risks: List[RiskAssessment]
    recommendation: Literal["Strong Buy", "Buy", "Hold", "Pass"]
    # ... and more
```

**Benefits:**
- Type-safe data structures
- Easy JSON export for databases
- API-ready format
- Data validation built-in

### 2. Quantitative Investment Scoring Framework

**5-Dimensional Scoring System (0-100 scale):**

| Dimension | Weight | Evaluation Criteria |
|-----------|--------|-------------------|
| **Team** | 25% | Experience, execution, completeness |
| **Market** | 25% | Size, growth, timing, competition |
| **Product** | 20% | Differentiation, moat, scalability |
| **Financial** | 20% | Unit economics, growth, efficiency |
| **Execution** | 10% | Traction, momentum, milestones |

**Overall Score Calculation:**
- Weighted average of dimensional scores
- Risk penalty: -10 points per critical risk
- Automatic recommendation: Strong Buy (80+), Buy (65-79), Hold (50-64), Pass (<50)

**Example Output:**
```
Overall Score: 78/100
Recommendation: Buy
Team: 85/100 - Exceptional founders with relevant exits
Market: 90/100 - $50B TAM growing at 25% annually
Product: 75/100 - Strong differentiation, building moat
Financial: 70/100 - Good unit economics, needs revenue growth
Execution: 80/100 - Strong traction, on track with milestones
```

### 3. Document Analysis with RAG

Upload and analyze:
- **Pitch Decks** - Extract market size claims, product roadmap, traction
- **Financial Statements** - Parse P&L, balance sheet, cash flow
- **Cap Tables** - Analyze ownership, dilution, option pools
- **Term Sheets** - Review valuation, preferences, terms

**RAG Pipeline:**
1. Upload PDF documents
2. Extract text and chunk
3. Create vector embeddings (optional: PgVector)
4. Agent queries knowledge base
5. Cross-reference claims with market data
6. Flag inconsistencies and red flags

### 4. Professional PDF Report Generation

**Report Sections:**
1. **Cover Page** - Company name, recommendation badge, metadata
2. **Executive Summary** - Key findings and investment thesis
3. **Investment Scores** - Radar chart with score breakdowns
4. **Company Profile** - Background, team, products, traction
5. **Financial Analysis** - Metrics table, trends, benchmarks
6. **Market Analysis** - TAM/SAM/SOM, competitive positioning
7. **Risk Assessment** - Heat map, categorized risk table
8. **Recommendation** - Deal terms, next steps, diligence items

**Visualizations Included:**
- Radar chart for investment scores
- Risk heat map (Impact vs Probability)
- Financial metrics tables
- Color-coded severity indicators

### 5. Multi-Company Comparison Dashboard

Compare multiple companies side-by-side:

**Comparison Views:**
- **Overall Scores** - Horizontal bar chart with recommendations
- **Dimensional Breakdown** - Grouped bar chart (team, market, product, etc.)
- **Risk Profiles** - Stacked bar chart by severity
- **Financial Metrics** - Revenue, growth, runway comparison
- **Rankings Table** - Sorted by overall score

**Use Cases:**
- Portfolio review and prioritization
- Deal flow management
- Investment committee presentations
- Pattern recognition across deals

### 6. Interactive Streamlit UI

**Three Modes:**

1. **Single Company Analysis**
   - Enter company name
   - Upload documents (optional)
   - View structured analysis
   - Export to JSON/PDF

2. **Compare Multiple Companies**
   - Select 2+ saved reports
   - View comparison charts
   - Rank companies
   - Export comparisons

3. **Saved Reports**
   - Browse historical analyses
   - Quick metrics view
   - Re-export reports

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/multi_agent_apps/agent_teams/ai_due_diligence_agent_team

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY='your-api-key-here'
```

### Run the Platform

**Option 1: Interactive Streamlit UI (Recommended)**
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

**Option 2: Playground Interface**
```bash
python3 due_diligence_agent_team.py
```

Open `http://localhost:7777` in your browser.

**Option 3: Python API**
```python
from due_diligence_agent_team_structured import DueDiligenceTeamStructured

# Initialize team
dd_team = DueDiligenceTeamStructured(api_key="your-openai-key")

# Run analysis
report = dd_team.run_analysis("Analyze Stripe for investment")

# Access structured data
print(f"Overall Score: {report.investment_scores.overall_score}")
print(f"Recommendation: {report.recommendation}")
print(f"TAM: ${report.market_analysis.tam}M")

# Export to JSON
with open("stripe_analysis.json", "w") as f:
    f.write(report.model_dump_json(indent=2))

# Generate PDF
from utils.report_generator import PDFReportGenerator
pdf_gen = PDFReportGenerator()
pdf_gen.generate_report(report, "stripe_report.pdf")
```

## 💡 Usage Examples

### Example 1: Full Due Diligence with Documents

```bash
# Via Streamlit UI:
1. Enter company name: "Notion"
2. Upload pitch deck PDF
3. Upload financial statements
4. Click "Start Analysis"
5. Review structured output
6. Export PDF report
7. Compare with other companies
```

### Example 2: Quick Market Assessment

```python
from due_diligence_agent_team_structured import DueDiligenceTeamStructured

dd_team = DueDiligenceTeamStructured(api_key=api_key)

report = dd_team.run_analysis("""
    Analyze the market opportunity for Figma.
    Focus on design software market size, competition,
    and Adobe's acquisition rationale.
""")

# Access specific insights
print(f"TAM: ${report.market_analysis.tam:.0f}M")
print(f"Key Competitors: {', '.join(report.market_analysis.key_competitors)}")
print(f"Market Score: {report.investment_scores.market_score}/100")
```

### Example 3: Financial Deep Dive

```python
report = dd_team.run_analysis("""
    Perform financial analysis on Stripe.
    Evaluate revenue growth, unit economics (CAC/LTV),
    burn rate, and compare to payment processor benchmarks.
""")

metrics = report.financial_metrics
print(f"Revenue: ${metrics.revenue_current:.1f}M")
print(f"Growth: {metrics.revenue_growth_yoy:.1f}%")
print(f"CAC/LTV: {metrics.cac_to_ltv_ratio:.2f}")
print(f"Financial Score: {report.investment_scores.financial_score}/100")
```

### Example 4: Portfolio Comparison

```python
from utils.comparison import ComparisonDashboard

# Analyze multiple companies
report1 = dd_team.run_analysis("Analyze Notion")
report2 = dd_team.run_analysis("Analyze Coda")
report3 = dd_team.run_analysis("Analyze Airtable")

# Create comparison
dashboard = ComparisonDashboard()
comparison_df = dashboard.create_comparison_dataframe([report1, report2, report3])
print(comparison_df)

# Generate comparison charts
fig = dashboard.create_score_comparison_chart([report1, report2, report3])
fig.savefig("comparison.png")
```

## 📁 Project Structure

```
ai_due_diligence_agent_team/
├── models/
│   ├── __init__.py
│   └── schemas.py                  # Pydantic models for structured output
├── utils/
│   ├── scoring.py                  # Investment scoring framework
│   ├── report_generator.py         # PDF report generation
│   ├── comparison.py               # Multi-company comparison
│   └── document_analyzer.py        # Document RAG processing
├── due_diligence_agent_team.py     # Original Playground version
├── due_diligence_agent_team_structured.py  # Structured output version
├── app.py                          # Streamlit UI application
├── requirements.txt
└── README.md
```

## 🔧 Configuration

### Environment Variables

```bash
# Required
export OPENAI_API_KEY='your-openai-api-key'

# Optional: For advanced RAG with vector DB
export DATABASE_URL='postgresql://localhost/due_diligence'
```

### Customization

**Adjust Scoring Weights:**
```python
# In utils/scoring.py
WEIGHTS = {
    "team": 0.30,      # Increase team weight
    "market": 0.25,
    "product": 0.20,
    "financial": 0.15,
    "execution": 0.10
}
```

**Modify Risk Penalties:**
```python
# In utils/scoring.py
penalty += min(critical_count * 15, 45)  # Harsher critical risk penalty
```

**Change Models:**
```python
dd_team = DueDiligenceTeamStructured(
    api_key=api_key,
    model="gpt-4o-mini"  # Faster, cheaper analysis
)
```

## 📊 Output Examples

### Structured JSON Output

```json
{
  "report_id": "a3f2b891",
  "analysis_date": "2026-01-19",
  "recommendation": "Buy",
  "company_profile": {
    "company_name": "Stripe",
    "industry": "Fintech - Payments",
    "stage": "Series H",
    "elevator_pitch": "Complete payments infrastructure for the internet",
    "value_proposition": "Unified API for accepting payments, managing subscriptions, and building financial products"
  },
  "investment_scores": {
    "overall_score": 82,
    "team_score": 95,
    "market_score": 85,
    "product_score": 80,
    "financial_score": 75,
    "execution_score": 85
  },
  "financial_metrics": {
    "revenue_current": 7400.0,
    "revenue_growth_yoy": 38.0,
    "gross_margin": 46.0,
    "arr_mrr": 7400.0
  },
  "market_analysis": {
    "tam": 135000.0,
    "sam": 45000.0,
    "som": 8000.0,
    "market_growth_rate": 15.5
  },
  "key_risks": [
    {
      "severity": "High",
      "risk_category": "Market",
      "risk_name": "Increased Competition from Big Tech",
      "impact": "High",
      "probability": "Medium",
      "mitigation_strategy": "Focus on developer experience and international expansion"
    }
  ]
}
```

## 🎓 Technical Details

### Scoring Algorithm

```python
overall_score = (
    team_score * 0.25 +
    market_score * 0.25 +
    product_score * 0.20 +
    financial_score * 0.20 +
    execution_score * 0.10
) - risk_penalty

risk_penalty = (
    critical_risks * 10 +
    high_risks * 5 +
    medium_risks * 2
)

recommendation = {
    >= 80: "Strong Buy",
    >= 65: "Buy",
    >= 50: "Hold",
    < 50: "Pass"
}
```

### Performance

- **Analysis Time**: 2-3 minutes per company
- **Cost per Analysis**: ~$0.30-0.50 (using GPT-4o)
- **Document Processing**: ~30 seconds per 20-page PDF
- **PDF Generation**: ~5-10 seconds
- **Comparison Dashboard**: <1 second for up to 10 companies

## 🤝 Contributing

We welcome contributions! Areas for improvement:

- Additional data sources (Crunchbase, PitchBook APIs)
- Industry-specific scoring templates
- Enhanced document parsing (tables, charts)
- Integration with deal flow systems (Affinity, Airtable)
- Advanced RAG with LangChain/LlamaIndex
- Web app deployment (Streamlit Cloud, Railway)

## 📝 License

This project is part of the [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) repository.

## 🙏 Acknowledgments

- **Agno (PhiData)** - Agent orchestration framework
- **OpenAI GPT-4o** - LLM powering analysis
- **YFinance** - Financial market data
- **ReportLab** - PDF generation
- **Streamlit** - Interactive UI framework

## 📧 Support

For issues, questions, or feature requests:
- Open an issue on [GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps)
- Join the community discussions
- Check the documentation

## 🚀 Roadmap

**v2.0 (Coming Soon):**
- [ ] Integration with Crunchbase/PitchBook APIs
- [ ] Real-time collaboration features
- [ ] Custom scoring templates by industry
- [ ] Advanced financial modeling
- [ ] Automated comp table generation
- [ ] Integration with cap table platforms (Carta, Pulley)
- [ ] Email report distribution
- [ ] Slack/Discord notifications

---

**Built for VCs, by developers who understand due diligence.**

Transform your investment process from days to minutes with AI-powered analysis that matches institutional quality.
