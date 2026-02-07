import os
import telebot
from telebot import types
from .dashboard_logic import AutonomousDashboard

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# In a real app, this would be a database mapping Telegram IDs to User Data
# Simulating a user session for the prototype
USER_DATA = {
    "repo_owner": "divygoyal",
    "repo_name": "trialmoltbot",
    "file_path": "index.html"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "👋 **Welcome to the Trial Molt Bot!**\n\n"
        "I am your Autonomous SEO Engineer. I've connected to your GitHub repo: "
        f"`{USER_DATA['repo_owner']}/{USER_DATA['repo_name']}`.\n\n"
        "Commands:\n"
        "🔍 /audit - Run a manual SEO audit\n"
        "✍️ Or just tell me what to change (e.g., 'Change the header to Blue')"
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['audit'])
def run_audit(message):
    bot.send_message(message.chat.id, "🔎 *Analyzing GSC data and GitHub repository...*", parse_mode='Markdown')
    
    # Run the dashboard logic
    dash = AutonomousDashboard("gsc_data.json", USER_DATA['repo_owner'], USER_DATA['repo_name'])
    recommendations = dash.run_daily_audit()
    
    if not recommendations:
        bot.send_message(message.chat.id, "✅ Everything looks great! No urgent fixes needed.")
        return

    for rec in recommendations:
        markup = types.InlineKeyboardMarkup()
        # We pass the data in the callback_data (limited to 64 chars in real Telegram, using simple keys here)
        approve_btn = types.InlineKeyboardButton("✅ Approve & Push", callback_data=f"fix_{rec['query'][:20]}")
        markup.add(approve_btn)
        
        msg = (
            f"🎯 **Opportunity Found!**\n"
            f"Keyword: `{rec['query']}`\n"
            f"Current Position: `{rec['current_pos']}`\n\n"
            f"💡 *Suggestion:* {rec['suggestion']}"
        )
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('fix_'))
def handle_approval(call):
    query_part = call.data.replace('fix_', '')
    bot.answer_callback_query(call.id, "🚀 Processing Vibecode...")
    bot.edit_message_text(f"⏳ **Vibecoding in progress...** (Optimizing for {query_part})", call.message.chat.id, call.message.message_id, parse_mode='Markdown')
    
    dash = AutonomousDashboard("gsc_data.json", USER_DATA['repo_owner'], USER_DATA['repo_name'])
    
    # For the prototype, we assume it's a striking distance fix
    success = dash.execute_approved_fix(USER_DATA['file_path'], query_part, "STRIKING_DISTANCE")
    
    if success:
        bot.send_message(call.message.chat.id, f"✅ **Success!** I've pushed the optimization for `{query_part}` to GitHub. Your site is now self-healing.")
    else:
        bot.send_message(call.message.chat.id, "❌ **Error:** I couldn't push the changes. Check my GitHub permissions.")

@bot.message_handler(func=lambda m: True)
def handle_vibecode(message):
    # This is the 'Vibecoding' catch-all
    user_request = message.text
    bot.reply_to(message, f"🛠️ **Vibecoding Mode Activated.**\n\nI'm translating your request: `{user_request}` into code changes for `{USER_DATA['file_path']}`. Hold on...")
    
    # In the real app, this text goes to a GPT-4/Claude model to generate the git edit
    dash = AutonomousDashboard("gsc_data.json", USER_DATA['repo_owner'], USER_DATA['repo_name'])
    success = dash.execute_approved_fix(USER_DATA['file_path'], user_request, "VIBECODE")
    
    if success:
        bot.reply_to(message, "✨ **Done!** I've vibecoded your request and pushed it to GitHub. Check your repo!")
    else:
        bot.reply_to(message, "❌ I ran into an issue while coding that. Let's try again?")

if __name__ == "__main__":
    bot.infinity_polling()
