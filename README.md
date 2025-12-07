# 🚀 Bitcoin Historical Compression API  
#### High-Performance BTC Market Analytics • FastAPI • Institutional-Grade Insights

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009485.svg)]()
[![Status](https://img.shields.io/badge/Status-Production-brightgreen.svg)]()
[![Latency](https://img.shields.io/badge/Response%20Time-%3C400ms-lightgrey.svg)]()

A high-efficiency analytical engine that transforms any Bitcoin historical date range into a compact, research-ready insight package. Instead of raw OHLC candles, it provides volatility models, drawdown metrics, monthly performance behavior, seasonal patterns, event detection, and a natural-language summary that describes the chosen timeframe. Everything is computed from real BTC-USD historical data, with no forecasts and no trading signals. Designed for quant developers, analysts, dashboards, bots, and institutional research systems.
https://rapidapi.com/z0art2000/api/btc-statistical-compression-api
---

## 🔍 What the API Provides

Every request processes the selected interval and returns a structured analytical narrative of Bitcoin’s behavior.  
You receive daily statistical compression (volatility, mean and median returns, spike detection), risk-oriented metrics such as maximum drawdown, a full monthly performance engine that identifies the strongest and weakest periods, pattern recognition that highlights seasonality and volatility clusters, and automatic inclusion of major Bitcoin network events such as halvings and protocol upgrades.  

The goal is simple: eliminate heavy datasets and deliver **immediate, actionable insight**.

---

## 🌐 Endpoints

The service exposes three essential endpoints that cover all use cases:

### `/health`  
Confirms the API is running and reachable, returning a simple status object.

### `/range-info`  
Reports the earliest and latest available BTC historical dates stored in the engine’s dataset, allowing clients to validate their requested intervals.

### `/compress`  
The core analytical endpoint. A POST request with `start` and `end` dates generates the full compressed statistical package, including the narrative summary and all quantitative sections.

---

## 🧪 Example Usage

### Python
```python
import requests

url = "https://api.btcinsights.online/compress"

payload = {
    "start": "2018-01-01",
    "end": "2020-01-01"
}

response = requests.post(url, json=payload)
print(response.json())
