from fastapi import FastAPI, UploadFile, File
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Trader Backend Running 🚀"}

@app.post("/upload-chart")
async def upload_chart(file: UploadFile = File(...)):
    image = await file.read()

    # 🔥 SIMULASI AI (nanti kita upgrade ke AI vision beneran)
    signal = random.choice(["BUY", "SELL"])

    confidence = random.randint(70, 95)

    entry = round(random.uniform(1.1000, 1.3000), 5)
    sl = round(entry - 0.0020, 5)
    tp1 = round(entry + 0.0025, 5)
    tp2 = round(entry + 0.0040, 5)
    tp3 = round(entry + 0.0060, 5)

    return {
        "status": "success",
        "filename": file.filename,
        "analysis": {
            "signal": signal,
            "confidence": confidence,
            "entry": entry,
            "stop_loss": sl,
            "take_profit": [tp1, tp2, tp3],
            "note": "AI v1 simulation active"
        }
    }