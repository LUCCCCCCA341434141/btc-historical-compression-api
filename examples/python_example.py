import requests

# Endpoint principale
API_URL = "https://api.btcinsights.online/compress"

# Example payload
payload = {
    "start": "2018-01-01",
    "end": "2020-01-01"
}

def main():
    print("Sending request to BTC Compression API...")
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        data = response.json()
        print("\n=== Compression Result Summary ===")
        print(f"Range: {data['range']['start']} → {data['range']['end']}")
        print(f"Volatility: {data['statistics']['volatility']}")
        print(f"Max Drawdown: {data['statistics']['max_drawdown']}")
        print(f"Spike Days: {data['statistics']['spike_days']}")
        print("\nMonthly Best:", data["monthly_analysis"]["best_months"])
        print("Monthly Worst:", data["monthly_analysis"]["worst_months"])
        print("\nSummary:")
        print(data["summary"])
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    main()
