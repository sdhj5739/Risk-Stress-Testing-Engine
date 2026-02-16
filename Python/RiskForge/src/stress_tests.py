import pandas as pd
from typing import Dict


def apply_stress_scenario(
    latest_returns: pd.Series,
    shocks: Dict[str, float]
) -> pd.Series:
    """
    Apply shocks to asset returns.
    shocks example: {"SPY": -0.3, "TLT": 0.05}
    """

    stressed = latest_returns.copy()

    for asset, shock in shocks.items():
        if asset in stressed.index:
            stressed[asset] += shock

    return stressed


def portfolio_loss_under_stress(
    stressed_returns: pd.Series,
    weights: Dict[str, float]
) -> float:
    """
    Compute portfolio return under stress scenario.
    """

    weights_series = pd.Series(weights)
    weights_series = weights_series.loc[stressed_returns.index]

    portfolio_return = (stressed_returns * weights_series).sum()

    return portfolio_return


if __name__ == "__main__":
    print("Stress testing module loaded successfully")
