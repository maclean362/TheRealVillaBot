import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import os

TOKEN = os.getenv("TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def We(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Super John Mcginn")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Using filters.Text to filter messages by their content
    start_handler = MessageHandler(filters.Text('Weve got Mcginn'), We)
    application.add_handler(start_handler)
    
    application.run_polling()
