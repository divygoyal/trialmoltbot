import os
import telebot
from telebot import types
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
bot = telebot.TeleBot(TOKEN)

# In-memory storage mapping Telegram ID to GitHub session
SESSIONS = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = (
        "🚀 **Trial Molt Bot: Vibecoding Activated**\n\n"
        "To start coding via Telegram, you first need to link your account:\n"
        "1. Go to our website and Login with GitHub.\n"
        "2. You will get a 4-character code.\n"
        "3. Type `/connect CODE` here."
    )
    bot.reply_to(message, msg, parse_mode='Markdown')

@bot.message_handler(commands=['connect'])
def connect_account(message):
    try:
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "📝 Please use the format: `/connect CODE`")
            return
            
        code = parts[1].upper()
        bot.send_message(message.chat.id, f"📡 Verifying code `{code}` with Jarvis API...")
        
        # Verify code with backend
        response = requests.get(f"{BACKEND_URL}/user/{code}", timeout=10)
        
        if response.status_code == 200:
            user_data = response.json()
            SESSIONS[message.chat.id] = user_data
            bot.reply_to(message, f"✅ **Connected!** I am now your engineer for `{user_data['repo']}`. \n\nWhat should we build today?")
        elif response.status_code == 404:
            bot.reply_to(message, "❌ **Invalid Code.** The session may have expired. Please refresh the website and get a new code.")
        else:
            bot.reply_to(message, f"⚠️ **API Error:** Backend returned status `{response.status_code}`. Check Render logs.")
            
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"🌐 **Connection Error:** I couldn't reach the backend at `{BACKEND_URL}`. Make sure the API is awake!")
    except Exception as e:
        bot.reply_to(message, f"🐞 **Unexpected Error:** `{str(e)}`")

@bot.message_handler(func=lambda m: True)
def handle_vibecode(message):
    user_session = SESSIONS.get(message.chat.id)
    if not user_session:
        bot.reply_to(message, "⚠️ You need to /connect your GitHub account first!")
        return

    user_request = message.text
    bot.reply_to(message, f"🛠️ **Vibecoding...**\n`Request: {user_request}`\n\nI'm drafting the code and pushing to `{user_session['repo']}`...")

    # Here we call our GitHub Manager logic
    # (Simplified for the launch demo)
    from .github_manager import GitHubManager
    token = user_session['github_token']
    
    # In the prototype, we use your existing PAT if the mock fails
    if "mock" in token:
        token = os.getenv("GITHUB_TOKEN") 

    manager = GitHubManager(token)
    repo_owner = "divygoyal" # Simulating dynamic lookup
    repo_name = user_session['repo']
    
    content, sha = manager.get_file_content(repo_owner, repo_name, "index.html")
    if content:
        # Simulate AI coding by adding a comment of the user's request
        new_content = content + f"\n    <!-- AI Update: {user_request} -->"
        success = manager.update_file(repo_owner, repo_name, "index.html", new_content, f"Vibecode: {user_request}", sha)
        
        if success:
            bot.send_message(message.chat.id, "✨ **Done!** The change is live on GitHub.")
        else:
            bot.send_message(message.chat.id, "❌ Push failed. Check repository permissions.")
    else:
        bot.send_message(message.chat.id, "❌ Could not find `index.html` to edit.")

if __name__ == "__main__":
    bot.infinity_polling()
