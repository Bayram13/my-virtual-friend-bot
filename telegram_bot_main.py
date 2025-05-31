import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters
import openai

# OpenAI API açarını environment-dən götür
openai.api_key = os.getenv("OPENAI_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salam! Mən Jarvisəm, sənə necə kömək edə bilərəm?")

def ask_jarvis(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        print(f"OpenAI API xətası: {e}")
        return "Bağışlayın, cavab alınarkən xəta baş verdi."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_message = update.message.text
        print(f"İstifadəçi mesajı: {user_message}")
        reply = ask_jarvis(user_message)
        print(f"Jarvis cavabı: {reply}")
        await update.message.reply_text(reply)
    except Exception as e:
        print(f"Telegram mesajında xəta: {e}")
        await update.message.reply_text("Bağışlayın, sistemdə xəta baş verdi. Bir az sonra yenidən cəhd edin.")

async def telegram_bot_main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Xəta: BOT_TOKEN təyin olunmayıb!")
        return

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Telegram bot işə düşür...")
    await app.run_polling()
