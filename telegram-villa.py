import logging
import requests
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import os
import json

TELEGRAMGRAMTOKEN = os.getenv("TOKEN")
url = "https://api-football-v1.p.rapidapi.com/v2/players/squad/66/2023-2024"

headers = {
    'x-rapidapi-host' :  "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key' : "7b8e4fe094msh920a3b9a254e231p1cba58jsnd985b6e2f537"
}

response = requests.request("GET", url, headers=headers)

playerlist = []

data = json.loads(response.text)

if "api" in data and "players" in data["api"]:
    for player in data["api"]["players"]:
        playerlist.append(f"{player['player_name']} - {player['position']}")
else:
    print("The response does not have the expected structure.")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=playerlist)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAMGRAMTOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()