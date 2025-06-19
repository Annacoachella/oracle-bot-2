import json
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Загружаем карточки из файла
with open("oracle_cards.json", encoding="utf-8") as f:
    cards = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я — Оракул Стихий 💫\nНапиши /oracle, чтобы получить послание."
    )

async def oracle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = random.choice(cards["общие"])
    await update.message.reply_text(f"🔮 {message}")

if name == '__main__':
    app = ApplicationBuilder().token("7912585872:AAG9bdYKmlByt8W_sAomP0VEsJU_SdCL-MU").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("oracle", oracle))
    app.run_polling()
