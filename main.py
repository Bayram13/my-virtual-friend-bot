from flask import Flask
from telegram_bot_main import app as telegram_bot_app  # webhook'u ordan alırıq

app = Flask(__name__)

@app.route('/')
def index():
    return "Telegram bot is running!"  # Sadə test üçün homepage

# gunicorn istifadə etdiyimiz üçün aşağıdakı hissəyə ehtiyac yoxdur:
# if __name__ == "__main__":
#     app.run(debug=True)
