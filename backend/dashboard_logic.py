import os
from github_manager import GitHubManager

class AutonomousDashboard:
    def __init__(self, gsc_file, repo_owner, repo_name):
        self.gsc_file = gsc_file
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.github_token = os.getenv("GITHUB_TOKEN")
        
    def run_daily_audit(self):
        # Importing here to avoid circular imports if any
        from seo_analyzer import analyze_gsc
        
        # Use relative path if the script is run from backend/
        try:
            recommendations = analyze_gsc(self.gsc_file)
        except FileNotFoundError:
            # Fallback for prototype testing
            recommendations = analyze_gsc("../gsc_data.json")
            
        pending_actions = [rec for rec in recommendations if rec['impact'] == "HIGH"]
        return pending_actions

    def execute_approved_fix(self, file_path, query, fix_type):
        manager = GitHubManager(self.github_token)
        content, sha = manager.get_file_content(self.repo_owner, self.repo_name, file_path)
        
        if not content:
            return False
            
        if fix_type == "STRIKING_DISTANCE":
            fix_msg = f"SEO: Optimize for '{query}'"
            new_content = content.replace("</h1>", f"</h1>\n    <h2>Unlock the power of {query}</h2>")
        else:
            # VIBECODE logic: Simulate AI edit
            fix_msg = f"Vibecode: {query}"
            new_content = content + f"\n    <!-- User Vibecode: {query} -->"
            
        return manager.update_file(self.repo_owner, self.repo_name, file_path, new_content, fix_msg, sha)
