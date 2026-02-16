import numpy as np
import pandas as pd


def simulate_portfolio_returns(
    returns: pd.Series,
    num_simulations: int = 10000,
    time_horizon: int = 1
) -> np.ndarray:
    """
    Monte Carlo simulation of portfolio returns assuming normal distribution.
    """

    mean = returns.mean()
    std = returns.std()

    simulated_returns = np.random.normal(
        loc=mean * time_horizon,
        scale=std * np.sqrt(time_horizon),
        size=num_simulations
    )

    return simulated_returns


def monte_carlo_var(simulated_returns: np.ndarray, confidence: float = 0.95) -> float:
    """
    VaR from simulated returns
    """
    return np.percentile(simulated_returns, (1 - confidence) * 100)


def monte_carlo_es(simulated_returns: np.ndarray, confidence: float = 0.95) -> float:
    """
    Expected Shortfall from simulated returns
    """
    var = monte_carlo_var(simulated_returns, confidence)
    return simulated_returns[simulated_returns <= var].mean()


if __name__ == "__main__":
    print("Monte Carlo module loaded successfully")
