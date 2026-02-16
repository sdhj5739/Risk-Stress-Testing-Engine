import pandas as pd
import numpy as np
from typing import Dict


def load_returns(path: str = "data/market_returns.csv") -> pd.DataFrame:
    """
    Load asset returns from CSV.
    """
    returns = pd.read_csv(path, index_col=0, parse_dates=True)
    return returns.dropna()


def build_portfolio_returns(
    returns: pd.DataFrame,
    weights: Dict[str, float]
) -> pd.Series:
    """
    Compute portfolio returns given asset returns and weights.
    """
    weights_series = pd.Series(weights)

    # Align weights with returns columns
    weights_series = weights_series.loc[returns.columns]

    portfolio_returns = returns @ weights_series
    return portfolio_returns


def portfolio_stats(
    portfolio_returns: pd.Series,
    periods_per_year: int = 252
) -> dict:
    """
    Compute basic portfolio statistics.
    """
    mean_return = portfolio_returns.mean() * periods_per_year
    volatility = portfolio_returns.std() * np.sqrt(periods_per_year)
    sharpe = mean_return / volatility if volatility != 0 else np.nan

    return {
        "annual_return": mean_return,
        "annual_volatility": volatility,
        "sharpe_ratio": sharpe
    }


if __name__ == "__main__":
    print("portfolio module loaded successfully")
