# -*- coding: utf-8 -*-
import config
import telebot


bot = telebot.TeleBot(config.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('hello', 'tg', 'vkpage', 'weather')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello, guest')
    elif message.text.lower() == 'tg':
        bot.send_message(message.chat.id, '@ssandess')
    elif message.text.lower() == 'i love u':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'chat' :
        #print(message.from_user)
        print(message.chat)
    elif message.text.lower() == 'vkpage' :
        bot.send_message(message.chat.id, 'https://vk.com/daniilshishov39')
    elif message.text.lower() == 'weather' :
        bot.send_message(message.chat.id, 'https://yandex.ru/pogoda/moscow/details?via=mf#16')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
