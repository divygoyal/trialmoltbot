import telebot
import os

TOKEN = "8452177885:AAGkjBgfyha_Z5uU5X70uoSzrkEaCg09kJQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Trial Molt Bot! 🤖\n\nI am your Autonomous SEO Engineer. Link your GitHub and GSC on the dashboard to begin our vibecoding journey.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "I've received your request. Let me analyze the repo...")

if __name__ == "__main__":
    print("Bot is polling...")
    bot.infinity_polling()
