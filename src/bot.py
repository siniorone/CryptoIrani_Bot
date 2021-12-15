import os
import telebot
from src.api.api import doge
from loguru import logger

bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['doge'])
def doge_coin(message):
    logger.info("doge...")
    a = doge()
    bot.send_message(message.chat.id, f"{a}")


# @bot.message_handler(func=lambda ـ: True)
# def echo(message):
#     bot.send_message(
#         message.chat.id,eval(message) )

bot.infinity_polling()

