from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .github_manager import GitHubManager
import os

app = FastAPI(title="Trial Molt Bot API")

# In a real app, these would come from the database based on the authenticated user
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "your_token_here")
REPO_OWNER = os.getenv("REPO_OWNER", "divygoyal")
REPO_NAME = os.getenv("REPO_NAME", "trialmoltbot")

class SEOFixRequest(BaseModel):
    file_path: str
    fix_description: str
    target_keyword: str

@app.get("/")
def read_root():
    return {"status": "Jarvis is Online", "vision": "Autonomous SEO & Vibecoding"}

@app.post("/apply-fix")
def apply_fix(request: SEOFixRequest):
    manager = GitHubManager(GITHUB_TOKEN)
    
    # 1. Get current content
    content, sha = manager.get_file_content(REPO_OWNER, REPO_NAME, request.file_path)
    if not content:
        raise HTTPException(status_code=404, detail="File not found in repository")

    # 2. Logic to "Vibecode" (In the real app, this sends the content to an LLM)
    # For now, we simulate a simple header injection
    if "header" in request.fix_description.lower():
        updated_content = content.replace("</h1>", f"</h1>\n    <h2>Optimized for: {request.target_keyword}</h2>")
    else:
        updated_content = content + f"\n<!-- SEO Fix: {request.fix_description} -->"

    # 3. Push to GitHub
    commit_msg = f"SEO: {request.fix_description}"
    success = manager.update_file(REPO_OWNER, REPO_NAME, request.file_path, updated_content, commit_msg, sha)
    
    if success:
        return {"status": "success", "message": f"Applied fix to {request.file_path} and pushed to GitHub."}
    else:
        raise HTTPException(status_code=500, detail="Failed to push changes to GitHub")
