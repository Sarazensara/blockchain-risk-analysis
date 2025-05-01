# Blockchain Risk Analysis Tool

A data-driven Python application that analyzes and visualizes potential risks in blockchain smart contracts using security flags. This project aims to identify patterns in smart contract vulnerabilities through exploratory data analysis and visual reporting.

---
## Authot

Odette Saenz 
Linkedin: https://www.linkedin.com/in/odettesaenz/
Github: https://github.com/Sarazensara

## Features

- Loads and processes two datasets:
  - `webacy_risk_dataset.csv`
  - `compiled_risk_data.csv`
- Performs both basic and advanced analysis of boolean risk flags
- Visualizes frequency of specific risks using bar charts
- Modular code structure with separate files for data loading, analysis, and visualization
- Easily extendable with machine learning or dashboard components (e.g., Streamlit)

---

## Risk Factors Analyzed

Includes analysis of key contract security flags such as:
- `Is_honeypot`
- `Is_blacklisted`
- `can_take_back_ownership`
- `buy_tax`, `sell_tax`
- `reentrancy_without_eth_transfer`
- `selfdestruct`
- `centralized_risk_*` tags  
...and 30+ other risk indicators.

---

## How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/Sarazenara/blockchain-risk-analysis.git
cd blockchain-risk-analysis