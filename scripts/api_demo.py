from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
