from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Trial Molt Bot API")

@app.get("/")
def read_root():
    return {"status": "Jarvis is Online", "vision": "Autonomous SEO & Vibecoding"}

@app.post("/analyze")
def run_analysis(site_url: str):
    # This will trigger the OpenClaw SEO agent
    return {"message": f"Analyzing {site_url}...", "recommendations": []}
