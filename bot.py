import telebot
import random
from telebot.types import Message

TOKEN = '857738427:AAGvnUpHK8shH7zj5mWtfkx8LUz9tR_I04U'
bot = telebot.TeleBot(TOKEN)

smiles = ['😯', '😟', '😂', '😘', '❤', '️😍', '😊', '😁']


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello')


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, random.choice(smiles))
    bot.send_sticker(message.chat.id)


bot.polling()
