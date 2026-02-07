import requests
import base64
import json

class GitHubManager:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_file_content(self, repo_owner, repo_name, file_path):
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            content = base64.b64decode(data['content']).decode('utf-8')
            return content, data['sha']
        return None, None

    def update_file(self, repo_owner, repo_name, file_path, new_content, commit_message, sha):
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
        encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
        payload = {
            "message": commit_message,
            "content": encoded_content,
            "sha": sha
        }
        response = requests.put(url, headers=self.headers, json=payload)
        return response.status_code == 200 or response.status_code == 201

# Example usage for the God Vision App:
# manager = GitHubManager("YOUR_PAT")
# content, sha = manager.get_file_content("divygoyal", "trialmoltbot", "index.html")
# if content:
#     # AI Logic here to generate 'updated_content'
#     success = manager.update_file("divygoyal", "trialmoltbot", "index.html", updated_content, "SEO: Auto-fix headers", sha)
