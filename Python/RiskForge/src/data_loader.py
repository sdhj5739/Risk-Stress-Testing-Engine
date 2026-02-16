import pandas as pd
import numpy as np
import yfinance as yf
from typing import List


def fetch_prices(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    """
    Fetch adjusted price data using yfinance.
    Uses auto-adjusted Close prices (preferred over Adj Close).
    """
    data = yf.download(
        tickers,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False
    )

    # Extract Close prices (already adjusted)
    if isinstance(data.columns, pd.MultiIndex):
        prices = data["Close"]
    else:
        prices = data["Close"]

    return prices.dropna()


def compute_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    returns = np.log(prices / prices.shift(1))
    return returns.dropna()


if __name__ == "__main__":
    print("data_loader.py ran successfully")
