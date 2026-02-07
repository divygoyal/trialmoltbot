from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
import os
import secrets

app = FastAPI(title="Trial Molt Bot - Launch MVP")

# Simulating a database
USER_DB = {}

# GitHub OAuth App Credentials (User would replace these)
CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "YOUR_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "YOUR_CLIENT_SECRET")

@app.get("/")
def home():
    return {"message": "God Vision MVP is Live. Go to /login to start."}

@app.get("/login")
def login():
    # Redirect to GitHub OAuth
    return RedirectResponse(f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope=repo")

@app.get("/callback")
def callback(code: str):
    # In a real app, exchange code for token. 
    # For the MVP Launch, we simulate getting the token and generating a Telegram Link Code.
    temp_token = "ghp_mock_token_12345" 
    link_code = secrets.token_hex(4).upper()
    
    USER_DB[link_code] = {"github_token": temp_token, "repo": "trialmoltbot"}
    
    return {
        "status": "Success",
        "message": "GitHub Authenticated!",
        "telegram_instruction": f"Now open your Telegram Bot and type: /connect {link_code}"
    }

@app.get("/user/{link_code}")
def get_user(link_code: str):
    user = USER_DB.get(link_code)
    if not user:
        raise HTTPException(status_code=404, detail="Code invalid")
    return user
