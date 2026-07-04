from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Trader Backend Running 🚀"}

@app.post("/upload-chart")
async def upload_chart(file: UploadFile = File(...)):
    image = await file.read()

    return {
        "status": "success",
        "filename": file.filename,
        "analysis": {
            "signal": "BUY",
            "confidence": 75,
            "entry": 0,
            "sl": 0,
            "tp": [0, 0, 0],
            "note": "AI basic mode aktif (belum full AI)"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
