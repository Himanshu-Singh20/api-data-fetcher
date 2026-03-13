import requests
import pandas as pd
from datetime import datetime


def fetch_crypto_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:
        print("Fetching data from API...")

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        time_updated = data["time"]["updated"]
        usd_price = data["bpi"]["USD"]["rate"]
        gbp_price = data["bpi"]["GBP"]["rate"]
        eur_price = data["bpi"]["EUR"]["rate"]

        record = {
            "timestamp": datetime.now(),
            "updated_time": time_updated,
            "BTC_USD": usd_price,
            "BTC_GBP": gbp_price,
            "BTC_EUR": eur_price
        }

        df = pd.DataFrame([record])

        df.to_csv("output_data.csv", mode="a", index=False, header=not pd.io.common.file_exists("output_data.csv"))

        print("Data saved successfully!")
        print(df)

    except Exception as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    fetch_crypto_price()