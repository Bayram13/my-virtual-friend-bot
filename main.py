from flask import Flask
from telegram_bot_main import run_bot
import asyncio
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Jarvis aktivdir!😎"

if __name__ == '__main__':
    # Telegram botu asyncio ilə birbaşa başlat
    asyncio.get_event_loop().create_task(run_bot())

    # Flask serveri portla işə sal (Render üçün vacibdir)
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
