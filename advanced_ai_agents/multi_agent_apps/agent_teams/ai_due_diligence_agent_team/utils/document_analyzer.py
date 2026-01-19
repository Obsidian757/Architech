"""
Document Analysis Utility

Processes uploaded documents (PDFs, pitch decks, financial statements)
and extracts structured information using RAG.
"""

import os
from typing import List, Optional
from pathlib import Path
import PyPDF2
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.pgvector import PgVector
from agno.embedder.openai import OpenAIEmbedder
from agno.storage.agent.sqlite import SqliteAgentStorage


class DocumentAnalyzer:
    """
    Analyzes uploaded due diligence documents using RAG.

    Supports:
    - Pitch decks
    - Financial statements
    - Cap tables
    - Legal documents
    - Business plans
    """

    def __init__(self, upload_dir: str = "uploaded_docs", use_vector_db: bool = False):
        """
        Initialize document analyzer.

        Args:
            upload_dir: Directory to store uploaded documents
            use_vector_db: Whether to use vector DB for RAG (requires PgVector setup)
        """
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(exist_ok=True)
        self.use_vector_db = use_vector_db

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract all text from a PDF file"""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n\n"
                return text
        except Exception as e:
            return f"Error extracting text: {str(e)}"

    def create_document_analysis_agent(
        self,
        documents: List[str],
        api_key: str
    ) -> Agent:
        """
        Create an agent with document knowledge base.

        Args:
            documents: List of document paths to analyze
            api_key: OpenAI API key

        Returns:
            Agent configured with document knowledge
        """
        if not self.use_vector_db:
            # Simple approach: Create agent with PDF knowledge base
            # This uses file-based storage instead of vector DB
            knowledge_base = PDFKnowledgeBase(
                path=str(self.upload_dir),
                reader=PDFReader()
            )
        else:
            # Advanced approach with vector DB (requires PostgreSQL)
            knowledge_base = PDFKnowledgeBase(
                path=str(self.upload_dir),
                vector_db=PgVector(
                    table_name="due_diligence_documents",
                    db_url=os.getenv("DATABASE_URL", "postgresql://localhost/due_diligence"),
                    embedder=OpenAIEmbedder(
                        model="text-embedding-3-large",
                        api_key=api_key
                    )
                )
            )

        # Load documents into knowledge base
        knowledge_base.load(upsert=True)

        # Create specialized document analysis agent
        agent = Agent(
            name="Document Analysis Agent",
            role="Expert at analyzing startup investment documents",
            model=OpenAIChat(id="gpt-4o", api_key=api_key),
            knowledge_base=knowledge_base,
            search_knowledge=True,
            markdown=True,
            instructions=[
                "Analyze uploaded documents thoroughly",
                "Extract key financial metrics, market claims, and team information",
                "Identify any red flags or inconsistencies",
                "Cross-reference claims with market data when possible",
                "Be specific and cite page numbers when referencing document content",
                "Focus on quantitative data: revenues, growth rates, market sizes, team size, etc.",
                "Identify gaps in the information provided"
            ],
            storage=SqliteAgentStorage(
                table_name="document_analysis_agent",
                db_file="due_diligence_agents.db"
            ),
            add_history_to_messages=True
        )

        return agent

    def analyze_pitch_deck(
        self,
        agent: Agent,
        focus_areas: Optional[List[str]] = None
    ) -> dict:
        """
        Analyze a pitch deck and extract structured information.

        Args:
            agent: Document analysis agent
            focus_areas: Specific areas to focus on

        Returns:
            Dictionary with extracted information
        """
        if focus_areas is None:
            focus_areas = [
                "Market size (TAM/SAM/SOM)",
                "Revenue model and pricing",
                "Competitive landscape",
                "Team background and experience",
                "Traction metrics and KPIs",
                "Go-to-market strategy",
                "Financial projections"
            ]

        query = f"""
        Analyze the pitch deck and extract the following information:

        {chr(10).join(f'{i+1}. {area}' for i, area in enumerate(focus_areas))}

        For each area, provide:
        - Specific data points mentioned (with page numbers)
        - Assessment of the claim's credibility
        - Any red flags or gaps in information

        Structure your response clearly with headers for each area.
        """

        response = agent.run(query, stream=False)
        return {
            "analysis": response.content,
            "focus_areas": focus_areas
        }

    def analyze_financials(
        self,
        agent: Agent
    ) -> dict:
        """
        Extract financial metrics from financial statements.

        Returns:
            Dictionary with financial data
        """
        query = """
        Extract and analyze the following financial metrics from the documents:

        Revenue Metrics:
        - Current annual revenue
        - Revenue growth rate (YoY)
        - Revenue by segment/product line
        - Recurring vs. one-time revenue

        Profitability:
        - Gross margin
        - Operating margin
        - Net profit/loss
        - Path to profitability

        Cash Flow:
        - Monthly burn rate
        - Cash runway
        - Operating cash flow
        - Free cash flow

        Unit Economics:
        - Customer Acquisition Cost (CAC)
        - Lifetime Value (LTV)
        - CAC payback period
        - Churn rate

        For each metric:
        1. Provide the specific value with units
        2. Note the time period
        3. Cite the page/section where found
        4. Flag any concerns or inconsistencies

        If any metrics are missing, explicitly note that.
        """

        response = agent.run(query, stream=False)
        return {
            "financial_analysis": response.content
        }

    def verify_claims(
        self,
        agent: Agent,
        claims: List[str]
    ) -> dict:
        """
        Verify specific claims made in documents.

        Args:
            agent: Document analysis agent
            claims: List of claims to verify

        Returns:
            Verification results
        """
        claims_text = "\n".join(f"{i+1}. {claim}" for i, claim in enumerate(claims))

        query = f"""
        Verify the following claims made in the documents:

        {claims_text}

        For each claim:
        1. State whether it is explicitly supported by the documents
        2. Cite the specific page/section
        3. Note any caveats or qualifications
        4. Flag if the claim seems exaggerated or unsupported

        Be critical and thorough in your verification.
        """

        response = agent.run(query, stream=False)
        return {
            "verification": response.content,
            "claims_checked": claims
        }

    def extract_risks_from_documents(
        self,
        agent: Agent
    ) -> dict:
        """
        Identify risks mentioned or implied in documents.

        Returns:
            Dictionary with identified risks
        """
        query = """
        Analyze the documents to identify potential risks and red flags:

        1. Explicit Risks:
           - What risks does the company acknowledge?
           - Are there risk factors listed?

        2. Implicit Risks:
           - What risks are NOT mentioned but should be?
           - What weaknesses can you infer from the data?
           - Are there inconsistencies that suggest problems?

        3. Financial Red Flags:
           - Concerning burn rate or runway
           - Deteriorating metrics
           - Unusual accounting treatments

        4. Market/Competition Risks:
           - Strong competitors not acknowledged
           - Market size claims that seem inflated
           - Competitive disadvantages

        5. Team Risks:
           - Key person dependencies
           - Gaps in expertise
           - High turnover indicators

        Categorize each risk by severity (Critical/High/Medium/Low) and provide rationale.
        """

        response = agent.run(query, stream=False)
        return {
            "document_risks": response.content
        }
