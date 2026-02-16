from data_loader import fetch_prices, compute_log_returns

TICKERS = ["^GSPC", "IEF", "EURUSD=X", "GLD"]
START_DATE = "2015-01-01"
END_DATE = "2024-12-31"

prices = fetch_prices(TICKERS, START_DATE, END_DATE)
returns = compute_log_returns(prices)

prices.to_csv("data/market_prices.csv")
returns.to_csv("data/market_returns.csv")

print("Market data pipeline completed successfully")

