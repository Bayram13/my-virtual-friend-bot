from flask import Flask, request
import telegram
import openai
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

bot = telegram.Bot(token=TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@app.route('/webhook', methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    
    if update.message and update.message.text:
        user_message = update.message.text
        chat_id = update.message.chat.id

        # OpenAI ilə cavab al
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content

        # Cavabı göndər
        bot.send_message(chat_id=chat_id, text=reply)
        
    return "ok"
