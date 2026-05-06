"""Quantum portfolio optimizer tool for the trading agent swarm.

Wraps qiskit-finance + qiskit-optimization into a single Agno tool that an LLM
agent can call. Given a list of tickers and a cardinality budget, it pulls
recent daily prices, computes mean log-returns and covariance, formulates the
selection as a QUBO, and solves with QAOA on a local Aer simulator.

Universe is intentionally capped (<= 8 tickers) so QAOA finishes in seconds
on a laptop simulator. This is a teaching demo, not a production solver.
"""

from __future__ import annotations

import numpy as np
import yfinance as yf
from agno.tools import tool
from qiskit_aer.primitives import Sampler
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit_finance.applications import PortfolioOptimization
from qiskit_optimization.algorithms import MinimumEigenOptimizer

MAX_UNIVERSE = 8


def _fetch_returns(tickers: list[str], lookback_days: int) -> np.ndarray:
    prices = yf.download(
        tickers,
        period=f"{lookback_days}d",
        interval="1d",
        auto_adjust=True,
        progress=False,
    )["Close"]
    if isinstance(prices, type(prices)) and prices.ndim == 1:
        prices = prices.to_frame()
    prices = prices[tickers].dropna()
    return np.log(prices / prices.shift(1)).dropna().to_numpy()


@tool
def quantum_portfolio_optimize(
    tickers: list[str],
    budget: int,
    lookback_days: int = 252,
    risk_factor: float = 0.5,
    seed: int = 42,
) -> dict:
    """Pick `budget` tickers from `tickers` via QAOA on a local quantum simulator.

    Mean-variance objective: maximize mu^T x - risk_factor * x^T Sigma x,
    subject to sum(x) == budget, x in {0, 1}^n. Equal weights are assumed
    over the selected names downstream.
    """
    if len(tickers) > MAX_UNIVERSE:
        raise ValueError(f"Universe capped at {MAX_UNIVERSE} tickers for the simulator.")
    if not 1 <= budget < len(tickers):
        raise ValueError("budget must satisfy 1 <= budget < len(tickers).")

    returns = _fetch_returns(tickers, lookback_days)
    mu = returns.mean(axis=0)
    sigma = np.cov(returns, rowvar=False)

    problem = PortfolioOptimization(
        expected_returns=mu,
        covariances=sigma,
        risk_factor=risk_factor,
        budget=budget,
    ).to_quadratic_program()

    qaoa = QAOA(
        sampler=Sampler(seed=seed),
        optimizer=COBYLA(maxiter=100),
        reps=2,
    )
    result = MinimumEigenOptimizer(qaoa).solve(problem)

    selection = [t for t, x in zip(tickers, result.x) if x > 0.5]
    return {
        "selected": selection,
        "x": [int(round(v)) for v in result.x],
        "objective": float(result.fval),
        "mu": mu.tolist(),
        "diag_sigma": np.diag(sigma).tolist(),
    }
