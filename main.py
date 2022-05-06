import os
import telebot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_message(message):
    bot.reply_to(message, 'Привет, я ботик, у меня баги')


bot.infinity_polling()
