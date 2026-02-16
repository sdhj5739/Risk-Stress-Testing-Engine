import numpy as np
import pandas as pd
from scipy.stats import norm


def historical_var(returns: pd.Series, confidence: float = 0.95) -> float:
    """
    Historical Value at Risk (VaR)
    """
    return np.percentile(returns, (1 - confidence) * 100)


def parametric_var(returns: pd.Series, confidence: float = 0.95) -> float:
    """
    Parametric VaR assuming normal distribution
    """
    mean = returns.mean()
    std = returns.std()

    return mean + std * norm.ppf(1 - confidence)


def expected_shortfall(returns: pd.Series, confidence: float = 0.95) -> float:
    """
    Expected Shortfall (CVaR)
    """
    var = historical_var(returns, confidence)
    return returns[returns <= var].mean()


if __name__ == "__main__":
    print("risk metrics module loaded successfully")
