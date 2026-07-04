from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import random

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/upload-chart")
async def upload_chart(file: UploadFile = File(...)):

    signal = random.choice(["BUY", "SELL"])
    confidence = random.randint(70, 95)

    entry = round(random.uniform(1.1000, 1.3000), 5)

    return {
        "signal": signal,
        "confidence": confidence,
        "entry": entry,
        "sl": entry - 0.0020,
        "tp": [entry + 0.002, entry + 0.004, entry + 0.006]
    }
