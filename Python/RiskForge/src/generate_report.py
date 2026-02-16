import pandas as pd
import matplotlib.pyplot as plt

from src.portfolio import load_returns, build_portfolio_returns
from src.risk_metrics import historical_var, parametric_var, expected_shortfall
from src.monte_carlo import simulate_portfolio_returns

# Load data
returns = load_returns()

weights = {
    "SPY": 0.6,
    "TLT": 0.25,
    "EURUSD=X": 0.1,
    "GLD": 0.05
}

portfolio_returns = build_portfolio_returns(returns, weights)

# ------------------------
# Save risk metrics
# ------------------------

metrics = {
    "Historical VaR": historical_var(portfolio_returns),
    "Parametric VaR": parametric_var(portfolio_returns),
    "Expected Shortfall": expected_shortfall(portfolio_returns)
}

metrics_df = pd.DataFrame([metrics])
metrics_df.to_csv("results/risk_metrics_summary.csv", index=False)

# ------------------------
# Monte Carlo simulation
# ------------------------

simulated = simulate_portfolio_returns(portfolio_returns, num_simulations=50000)

plt.hist(simulated, bins=100)
plt.title("Monte Carlo Portfolio Return Distribution")
plt.xlabel("Simulated Return")
plt.ylabel("Frequency")

plt.savefig("results/monte_carlo_distribution.png")
plt.close()

print("Report generated in results/ folder")
