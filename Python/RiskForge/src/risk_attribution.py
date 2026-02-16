import pandas as pd
import numpy as np
from typing import Dict


def asset_risk_contributions(
    returns: pd.DataFrame,
    weights: Dict[str, float]
) -> pd.Series:
    """
    Compute each asset's contribution to portfolio volatility.
    """

    weights_series = pd.Series(weights)
    weights_series = weights_series.loc[returns.columns]

    cov_matrix = returns.cov()

    portfolio_vol = np.sqrt(
        weights_series.T @ cov_matrix @ weights_series
    )

    marginal_contrib = cov_matrix @ weights_series / portfolio_vol
    risk_contrib = weights_series * marginal_contrib

    return risk_contrib.sort_values(ascending=False)


if __name__ == "__main__":
    print("Risk attribution module loaded successfully")
