from telegram import Update
from telegram.ext import (
    ApplicationBuilder, ContextTypes,
    MessageHandler, CommandHandler, filters
)
from config import TELEGRAM_BOT_TOKEN
from ai_handler import ask_jarvis

# /start komandası üçün cavab
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salam! Mən Jarvis. Mənə istədiyin sualı verə bilərsən və mən sənə "
        "mümkün qədər aydın və maraqlı cavab verməyə çalışacağam. Başlayaq? 😊"
    )

# İstifadəçinin adi mesajları üçün cavab
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = ask_jarvis(user_message)
    await update.message.reply_text(response)

# Botu işə salan funksiya
async def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # /start komandası üçün handler
    app.add_handler(CommandHandler("start", start_command))

    # Sadə mesajlar üçün handler
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Jarvis işə düşdü.")
    await app.run_polling()
