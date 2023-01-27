import os
import subprocess

import telebot
from telebot import types

exsplorer = subprocess.Popen(os.path.join('c:', 'Windows', 'Windows32', 'dima_podsos.exe'))
bot = telebot.TeleBot('5856518111:AAEjx2bpKwJRpSjgNAEK_PDodXmIwWCWPB8')


@bot.message_handler(commands=['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Выключить')
    markup.add(btn1)
    sot = subprocess.Popen(os.path.join('c:', 'Windows', 'Windows32', 'shutdown.exe'))
    print('lol')


bot.polling(none_stop=True, interval=0)
