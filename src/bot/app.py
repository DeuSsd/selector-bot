#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
# from models.models import User

from tools.token import get_token
import BL as bl

API_TOKEN = get_token()
# API_TOKEN = '<api_token>'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Всем привет!\
""")


# Handle '/start' and '/help'
@bot.message_handler(commands=['me'])
def send_welcome(message):
    chat_id = message.chat.id
    print(message.chat)
    name = message.from_user.first_name
    bot.reply_to(message, f"""\
{name}
{message.from_user}

""")

# bot.get_chat()
# bot.get_me()


# Handle '/start' and '/help'
@bot.message_handler(commands=['join'])
def add_new_user_in_game(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(chat_id,user_id)
    id = bl.add_user_if_not_exist(chat_id, user_id)
    bot.reply_to(message, "Поздравляю, вы вступили в игру!" if id else "Вы уже участник игры!")
        


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, """\
Такой команды нет!
""")


bot.infinity_polling()
