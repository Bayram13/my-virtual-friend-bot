from flask import Flask, request
import telegram
import openai
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

bot = telegram.Bot(token=TELEGRAM_TOKEN)

# OpenAI API açarını təyin et
openai.api_key = OPENAI_API_KEY

@app.route('/')
def index():
    return "Bot is alive!"

@app.route('/webhook', methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        update = telegram.Update.de_json(data, bot)

        if update.message and update.message.text:
            user_message = update.message.text
            chat_id = update.message.chat.id

            # OpenAI API çağırışı
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            reply = response['choices'][0]['message']['content']
            bot.send_message(chat_id=chat_id, text=reply)

        return "ok"
    except Exception as e:
        print("XƏTA:", str(e))
        return "error"
