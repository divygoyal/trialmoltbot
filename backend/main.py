import os
import threading
import secrets
import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from github_manager import GitHubManager
from bot import bot

app = FastAPI(title="Trial Molt Bot - SaaS Engine")

# Configuration (from Render Env)
CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME", "trialmoltbot")
FRONTEND_URL = os.getenv("FRONTEND_URL", "https://trialmoltbot-o5r5.vercel.app")

# Simulating a database (In production, use PostgreSQL/Redis)
USER_DB = {}

@app.on_event("startup")
def startup_event():
    def run_bot():
        print("🤖 Starting Telegram Bot thread...")
        try:
            bot.infinity_polling(timeout=20, long_polling_timeout=10)
        except Exception as e:
            print(f"Bot Error: {e}")
    
    thread = threading.Thread(target=run_bot, daemon=True)
    thread.start()

@app.get("/")
def home():
    return {"status": "Jarvis is Online", "vision": "Autonomous SEO & Vibecoding"}

@app.get("/login")
def login():
    return RedirectResponse(f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope=repo")

@app.get("/callback")
def callback(code: str):
    token_url = "https://github.com/login/oauth/access_token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code
    }
    headers = {"Accept": "application/json"}
    
    response = requests.post(token_url, json=payload, headers=headers)
    token_data = response.json()
    
    access_token = token_data.get("access_token")
    if not access_token:
        return {"error": "Failed to authenticate with GitHub", "details": token_data}

    # Create a unique link code
    link_code = secrets.token_hex(4).upper()
    
    # Store the session
    USER_DB[link_code] = {
        "github_token": access_token,
        "repo": REPO_NAME
    }
    
    # REDIRECT to the beautiful frontend success page instead of returning JSON
    return RedirectResponse(f"{FRONTEND_URL}/success?code={link_code}")

@app.get("/user/{link_code}")
def get_user(link_code: str):
    user = USER_DB.get(link_code)
    if not user:
        raise HTTPException(status_code=404, detail="Code invalid or expired")
    return user

@app.post("/apply-fix")
def apply_fix(link_code: str, file_path: str, fix_description: str):
    user = USER_DB.get(link_code)
    if not user:
        raise HTTPException(status_code=401, detail="User not authenticated")
        
    manager = GitHubManager(user['github_token'])
    return {"status": "success"}
