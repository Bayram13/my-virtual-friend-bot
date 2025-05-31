from flask import Flask
import threading
import asyncio
from telegram_bot_main import main as telegram_bot_main

app = Flask(__name__)

@app.route('/')
def home():
    return "Jarvis  serveri işləyir!"

# Telegram botu ayrıca thread-də işə sal
def run_bot():
    asyncio.run(telegram_bot_main())

# Server başladıqda bot da başlasın
threading.Thread(target=run_bot).start()

if __name__ == '__main__':
    app.run()
