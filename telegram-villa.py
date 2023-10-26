import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import os

TOKEN = os.getenv("TOKEN")
APITOKEN = 'JQVl8GNrhQzVhdf7hLVnq1pw6BqvxOGUNhfyBsMm0Ty9H5chvGjYD85m1vhi'

URL = 'https://api.sportsmonks.com/api/v2.0'
TEAM = 'Aston Villa'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def get_team_stats(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Using filters.Text to filter messages by their content
    start_handler = MessageHandler(filters.Text()
    application.add_handler(start_handler)
    
    application.run_polling()
