from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Get token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Define /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m your Telegram bot 🤖")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
