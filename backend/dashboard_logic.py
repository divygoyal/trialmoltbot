from .seo_analyzer import analyze_gsc
from .github_manager import GitHubManager
import os

class AutonomousDashboard:
    def __init__(self, gsc_file, repo_owner, repo_name):
        self.gsc_file = gsc_file
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.github_token = os.getenv("GITHUB_TOKEN")
        
    def run_daily_audit(self):
        """
        The core autonomous loop: 
        1. Analyze GSC 
        2. Find opportunities
        3. Format for Telegram notification
        """
        recommendations = analyze_gsc(self.gsc_file)
        
        # In the real app, this list is sent to the Telegram Bot
        # for human-in-the-loop approval.
        pending_actions = []
        for rec in recommendations:
            if rec['impact'] == "HIGH":
                pending_actions.append(rec)
                
        return pending_actions

    def execute_approved_fix(self, file_path, query, fix_type):
        """
        Executes the 'Vibecoding' push once user clicks [Approve] on Telegram
        """
        manager = GitHubManager(self.github_token)
        content, sha = manager.get_file_content(self.repo_owner, self.repo_name, file_path)
        
        if not content:
            return False
            
        # Logic to 'Vibecode' based on the specific SEO query
        if fix_type == "STRIKING_DISTANCE":
            fix_msg = f"SEO: Optimize for '{query}'"
            new_content = content.replace("</h1>", f"</h1>\n    <h2>Unlock the power of {query}</h2>")
        else:
            fix_msg = f"SEO: Improve CTR for '{query}'"
            new_content = content # Title logic would go here
            
        return manager.update_file(self.repo_owner, self.repo_name, file_path, new_content, fix_msg, sha)
