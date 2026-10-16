from fastapi import FastAPI

app = FastAPI(title="ResQbox Backend")

@app.get("/")
def home():
    return {"message": "ResQbox backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}