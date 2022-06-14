#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from os import environ
from time import sleep
import telebot
# from models.models import User

from tools.token import get_token
import BL as bl

# API_TOKEN = get_token()
# API_TOKEN = '<api_token>'



_load_env = lambda config_data_dict, ENV_KEY: config_data_dict.get(ENV_KEY) if ENV_KEY not in environ.keys() else environ[ENV_KEY]

API_TOKEN = _load_env(get_token(), "TOKEN")

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
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    print(chat_id, user_id)
    id = bl.add_user_if_not_exist(chat_id, user_id, first_name, last_name)
    bot.reply_to(
        message, "Поздравляю, вы вступили в игру!" if id else "Вы уже участник игры!")


@bot.message_handler(commands=['delete_me'])
def remove_user_from_game(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = f"{first_name} {last_name}" if last_name else f"{first_name}"
    status = bl.remove_user(chat_id, user_id)
    bot.reply_to(
        message, f"Пользователь {full_name}  выбыл из игры" if status else "Вы уже выбыли из игры!")

    # TODO write agree


@bot.message_handler(commands=['drop_statistics'])
def remove_user_from_game(message):
    chat_id = message.chat.id
    bl.drop_statistics(chat_id)
    bot.reply_to(message, f"Статистика была обнулена!")


# Handle '/start' and '/help'
@bot.message_handler(commands=['stats'])
def add_new_user_in_game(message):
    chat_id = message.chat.id
    msg = bl.get_statistics(chat_id)
    bot.reply_to(message, msg)


# Handle '/start' and '/help'
@bot.message_handler(commands=['run'])
def add_new_user_in_game(message):
    chat_id = message.chat.id
    user_id, msg  = bl.randomly_choose_one_user(chat_id)
    for line in msg.split("\n"):
        bot.send_message(chat_id, line)
        sleep(1)
    list_user_id = bl.user_selected_title(chat_id)
    for id in list_user_id:
        bot.set_chat_administrator_custom_title(chat_id, user_id, "Красавчик дня" if id == user_id else "")


# Handle '/start' and '/help'
@bot.message_handler(commands=['test'])
def test(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(chat_id,user_id)
    print(bot.set_chat_administrator_custom_title(chat_id, user_id, "Красавчик дня"))


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, """\
# Такой команды нет!
# """)

bot.infinity_polling()
