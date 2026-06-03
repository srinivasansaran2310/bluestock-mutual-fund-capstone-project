import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print(fund_master.head())
print(nav_history.head())

print("Fund Master Shape:", fund_master.shape)
print("NAV History Shape:", nav_history.shape)

print(fund_master.duplicated().sum())
print(nav_history.dtypes)
nav_history["date"] = pd.to_datetime(
    nav_history["date"]
)

nav_history["nav"] = pd.to_numeric(
    nav_history["nav"]
)
fund_master.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)
import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print(fund_master.head())
print(nav_history.head())
print(aum.head())
print("Fund Master:", fund_master.shape)
print("NAV History:", nav_history.shape)
print("AUM:", aum.shape)
print(fund_master.isnull().sum())
print(nav_history.isnull().sum())
print(aum.isnull().sum())
print("Fund Master:", fund_master.duplicated().sum())
print("NAV History:", nav_history.duplicated().sum())
print("AUM:", aum.duplicated().sum())
print(fund_master.dtypes)
print(nav_history.dtypes)
print(aum.dtypes)
nav_history['date'] = pd.to_datetime(nav_history['date'])
print(nav_history.dtypes)
fund_master.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

nav_history.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

aum.to_csv(
    "data/processed/aum_clean.csv",
    index=False
)