## Trading Agent Swarm with Quantum Portfolio Optimizer

A small multi-agent demo that picks a basket of stocks by formulating the
selection as a QUBO and solving with QAOA on a local Qiskit Aer simulator.
The optimization node is one specialist agent inside an Agno team; the rest
are LLM-driven agents for research, signal generation, risk checks, and a
paper-execution replay.

This is a teaching demo. It is not financial advice and does not place real
trades.

### Features

- Five-agent swarm coordinated by an Agno team root:
    - **Research Agent** — recent news and fundamentals via DuckDuckGo + yfinance
    - **Signal Agent** — annualized return, vol, and 3-month momentum from 1y of daily closes
    - **Quantum Optimizer** — QAOA-based basket selection on a local Aer simulator
    - **Risk Agent** — basket-level vol and worst monthly drawdown, returns GO / NO-GO
    - **Paper Execution Agent** — last-month equal-weight return and Sharpe, labelled as paper
- QAOA portfolio optimization via `qiskit-finance` + `qiskit-optimization`, executed on the local `qiskit-aer` simulator (no IBM Quantum credentials needed)
- Interactive Agno Playground UI
- SQLite-backed per-agent conversation history

### Architecture

```
User prompt  ->  Trading Agent Swarm (coordinator)
                    |
                    +--> Research Agent     (DuckDuckGo, yfinance news)
                    +--> Signal Agent       (yfinance prices)
                    +--> Quantum Optimizer  (qiskit-finance + QAOA on Aer)
                    +--> Risk Agent         (yfinance prices)
                    +--> Paper Execution    (yfinance prices)
```

The optimizer agent calls a single tool, `quantum_portfolio_optimize`, which
fetches recent prices, computes mean log-returns and covariance, builds a
mean-variance QUBO with a cardinality (budget) constraint, and solves it
with QAOA. The universe is capped at 8 tickers so the simulator finishes
in seconds on a laptop.

### How to get Started

1. Clone the repository
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   cd awesome-llm-apps/advanced_ai_agents/multi_agent_apps/trading_agent_swarm
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key
   ```bash
   cp .env.example .env
   export OPENAI_API_KEY='your-api-key-here'
   ```

4. Run the swarm
   ```bash
   python trading_agent_swarm.py
   ```

5. Open the Playground URL printed in the console and try a prompt like:
   > Pick 3 of AAPL, MSFT, GOOGL, NVDA, META, AMZN for the next quarter.

### Configuration

- Universe size is capped at `MAX_UNIVERSE = 8` in `quantum_optimizer.py`. QAOA scales poorly past that on a laptop simulator.
- `risk_factor` defaults to `0.5` (mean-variance trade-off). Lower values favor return, higher values favor low variance.
- The QAOA call is seeded (`seed=42`) so results are reproducible across runs.
- Swap the model by editing `MODEL_ID` in `trading_agent_swarm.py`.

### Caveats

- `qiskit-finance` (last release Feb 2024) and `qiskit-optimization` (no longer officially supported by IBM as of 2025) are community-maintained. They install and run today, but expect occasional breakage as Qiskit moves forward. A fully-supported alternative is to hand-build the QUBO and call `qiskit-algorithms`'s `QAOA` directly.
- Universe is capped at 8 because QAOA on a local simulator is exponential in qubit count. Real hardware via IBM Quantum is out of scope for this demo.
- Equal weights are assumed across the selected basket. Continuous-weight optimization is a separate (harder) problem and would not benefit from QAOA in the same way.
- `yfinance` is unofficial and rate-limited. If a ticker fails to download, agents will say so rather than fabricate numbers.
