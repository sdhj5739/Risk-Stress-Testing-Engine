# RiskForge — Portfolio Risk & Stress Testing Engine

## Overview

RiskForge is an end-to-end portfolio risk engine built in Python that models financial uncertainty, simulates extreme market conditions, and identifies key drivers of downside risk across asset classes.

The system mirrors workflows used by market risk, enterprise risk, and consulting teams to evaluate portfolio resilience under stress.

Instead of focusing on average outcomes, RiskForge emphasizes tail risk, scenario analysis, and explainability.

---

## Key Features

### Multi-Asset Portfolio Modeling
- Equities (S&P 500 proxy)
- US Treasuries (rates proxy)
- FX (USD/EUR)
- Commodities (Gold)

### Risk Metrics
- Historical Value at Risk (VaR)
- Parametric VaR (Normal assumption)
- Expected Shortfall (CVaR)

### Monte Carlo Simulation
- Simulates thousands of potential future outcomes
- Generates portfolio loss distributions
- Computes simulated VaR and Expected Shortfall

### Stress Testing & Scenario Analysis
- Equity crash scenarios
- Interest rate shocks
- FX devaluation
- Commodity price shocks

### Risk Attribution
- Identifies which assets drive portfolio risk
- Measures contribution to volatility
- Highlights concentration risk

---

## Architecture


### Modules

**data_loader.py**
- Downloads and preprocesses historical market data

**portfolio.py**
- Constructs weighted portfolio returns
- Computes portfolio statistics

**risk_metrics.py**
- Calculates VaR and Expected Shortfall

**monte_carlo.py**
- Simulates future return paths

**stress_tests.py**
- Applies macro shock scenarios

**risk_attribution.py**
- Breaks down sources of portfolio risk

---

## Example Use Cases

- Market risk analysis
- Enterprise risk stress testing
- Consulting-style scenario planning
- Portfolio vulnerability assessment

---

## Sample Results

Example outputs include:

- Annualized portfolio volatility
- 95% Value at Risk estimates
- Expected Shortfall during tail events
- Portfolio losses under crisis scenarios
- Asset-level risk contributions

---

## How to Run

### 1. Install dependencies

### 2. Run the data pipeline

### 3. Execute modules individually

---

## Motivation

Financial systems behave like complex engineered systems — failures often occur under extreme conditions rather than normal ones.

This project applies engineering-style failure analysis to financial portfolios by:

- Modeling uncertainty
- Stress-testing extreme scenarios
- Identing system vulnerabilities
- Explaining risk drivers

---

## Technologies Used

- Python
- Pandas
- NumPy
- SciPy

---

## Author

Built as a portfolio project demonstrating quantitative risk modeling, scenario analysis, and system-level thinking applicable to consulting, finance, and data roles.
