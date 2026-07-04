from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI Trader Active", "endpoints": ["/analyze"]}
    
# =========================
# FETCH REAL MARKET DATA
# =========================
def get_market_data(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=5m&limit=50"
    data = requests.get(url).json()

    closes = [float(candle[4]) for candle in data]
    return closes


# =========================
# REAL AI ANALYSIS ENGINE
# =========================
def analyze_real_market(closes):

    avg_short = sum(closes[-10:]) / 10
    avg_long = sum(closes[-30:]) / 30

    # Trend logic (real price action based)
    if closes[-1] > avg_short and avg_short > avg_long:
        signal = "BUY"
        trend = "uptrend"
    elif closes[-1] < avg_short and avg_short < avg_long:
        signal = "SELL"
        trend = "downtrend"
    else:
        signal = "HOLD"
        trend = "sideways"

    return signal, trend


# =========================
# API ENDPOINT (REAL AI)
# =========================
@app.get("/analyze")
def analyze():

    closes = get_market_data()

    signal, trend = analyze_real_market(closes)

    entry = closes[-1]

    if signal == "BUY":
        sl = entry * 0.99
        tp = [entry * 1.01, entry * 1.02, entry * 1.03]
    elif signal == "SELL":
        sl = entry * 1.01
        tp = [entry * 0.99, entry * 0.98, entry * 0.97]
    else:
        sl = entry
        tp = [entry]

    return {
        "status": "success",
        "symbol": "BTCUSDT",
        "analysis": {
            "signal": signal,
            "trend": trend,
            "entry": entry,
            "stop_loss": sl,
            "take_profit": tp,
            "note": "REAL AI TRADING v1 (OHLC MARKET DATA)"
        }
    }
