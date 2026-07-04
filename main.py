from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

# =========================
# FRONTEND (INDEX.HTML)
# =========================
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")


# =========================
# AI ANALYSIS (V2 LOGIC)
# =========================
def analyze_market():
    # AI logic simulasi (nanti upgrade ke AI vision beneran)
    trend = random.choice(["bullish", "bearish"])

    return {
        "trend": trend,
        "strength": random.choice(["weak", "medium", "strong"]),
        "structure": random.choice(["higher_high", "lower_low", "sideways"])
    }


@app.post("/upload-chart")
async def upload_chart(file: UploadFile = File(...)):

    image = await file.read()

    market = analyze_market()

    # SIGNAL LOGIC (bukan random full, sudah pakai struktur)
    if market["trend"] == "bullish":
        signal = "BUY"
        entry = 1.2000
        sl = entry - 0.0020
        tp = [entry + 0.0020, entry + 0.0040, entry + 0.0060]
    else:
        signal = "SELL"
        entry = 1.2000
        sl = entry + 0.0020
        tp = [entry - 0.0020, entry - 0.0040, entry - 0.0060]

    confidence = random.randint(70, 95)

    return {
        "status": "success",
        "filename": file.filename,
        "analysis": {
            "signal": signal,
            "confidence": confidence,
            "entry": entry,
            "stop_loss": sl,
            "take_profit": tp,
            "market_structure": market,
            "note": "AI Trading v2 (logic-based, not vision yet)"
        }
    }
