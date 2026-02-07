import os
import threading
import secrets
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from github_manager import GitHubManager
from bot import bot

app = FastAPI(title="Trial Molt Bot - God Vision MVP")

# Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER", "divygoyal")
REPO_NAME = os.getenv("REPO_NAME", "trialmoltbot")
CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

# Simulating a database
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
    link_code = secrets.token_hex(4).upper()
    USER_DB[link_code] = {"github_token": GITHUB_TOKEN, "repo": REPO_NAME}
    
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

class SEOFixRequest(BaseModel):
    file_path: str
    fix_description: str
    target_keyword: str

@app.post("/apply-fix")
def apply_fix(request: SEOFixRequest):
    manager = GitHubManager(GITHUB_TOKEN)
    content, sha = manager.get_file_content(REPO_OWNER, REPO_NAME, request.file_path)
    if not content:
        raise HTTPException(status_code=404, detail="File not found")

    updated_content = content + f"\n<!-- SEO Fix: {request.fix_description} -->"
    success = manager.update_file(REPO_OWNER, REPO_NAME, request.file_path, updated_content, f"SEO: {request.fix_description}", sha)
    
    if success:
        return {"status": "success", "message": "Applied fix"}
    else:
        raise HTTPException(status_code=500, detail="Push failed")
