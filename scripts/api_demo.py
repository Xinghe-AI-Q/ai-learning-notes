from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/echo")
def echo_text(text: str):
    return {
        "input_text": text,
        "length": len(text)
    }

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(request: TextRequest):
    text = request.text
    words = text.lower().split()

    return {
        "original_text": text,
        "word_count": len(words),
        "words": words
    }
