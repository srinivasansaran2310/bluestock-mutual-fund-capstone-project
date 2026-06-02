import requests
import requests
import pandas as pd

funds = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    file_path = f"data/raw/{fund_name}.csv"

    df.to_csv(file_path, index=False)

    print(f"{fund_name} saved successfully")
