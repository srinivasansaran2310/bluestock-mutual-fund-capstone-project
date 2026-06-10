import pandas as pd
import os

# Get project root folder automatically
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load fund scorecard
file_path = os.path.join(
    base_dir,
    "data",
    "processed",
    "fund_scorecard.csv"
)

funds = pd.read_csv(file_path)

# Create risk grades using max drawdown
funds['risk_grade'] = pd.cut(
    funds['max_drawdown'],
    bins=[-1, -0.20, -0.10, 0],
    labels=['High', 'Moderate', 'Low']
)

# Take user input
risk = input(
    "Enter Risk Appetite (Low / Moderate / High): "
).strip()

# Filter top 3 funds by Sharpe Ratio
recommendations = (
    funds[
        funds['risk_grade']
        .astype(str)
        .str.lower()
        ==
        risk.lower()
    ]
    .sort_values(
        'sharpe',
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds\n")

if recommendations.empty:
    print("No funds found for selected risk profile.")
else:
    print(
        recommendations[
            [
                'amfi_code',
                'sharpe',
                'alpha',
                'fund_score',
                'risk_grade'
            ]
        ]
    )