import os
from flask import Flask
import threading
from telegram_bot_main import run_bot

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "Virtual dost bot işləyir!"

if __name__ == '__main__':
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host='0.0.0.0', port=port)
