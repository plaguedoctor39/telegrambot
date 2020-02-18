# -*- coding: utf-8 -*-
import config
import telebot
import requests
import json
#import botan
from telebot import types
import random
random.seed()
s_city = "Moscow,RU"
city_id = 524901
appid = config.appid
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
"""
WEBHOOK_HOST = 'IP-адрес сервера, на котором запущен бот'
WEBHOOK_PORT = 443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)
"""

bot = telebot.TeleBot(config.token)

cmds = 'Вот список доступных команд: \n' + '/Hello \n' + '/tg \n' + '/vk \n' + '/weather'
@bot.message_handler(commands=['commands'])
def start_message(message):
    bot.send_message(message.chat.id, cmds)
    


@bot.message_handler(commands=['random'])
def cmd_random(message):
    bot.send_message(message.chat.id, random.randint(1, 10))
    # Если не нужно собирать ничего, кроме количества использований, замените третий аргумент message на None
    #botan.track(config.botan_key, message.chat.id, message, 'Случайное число')
    return

@bot.message_handler(commands=['weather'])
def cmd_random(message):
    bot.send_message(message.chat.id, weather_get)

@bot.message_handler(commands=['vk'])
def cmd_random(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на страницу вк", url="https://vk.com/daniilshishov39")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми на кнопку и переходи на мою страницу.", reply_markup=keyboard)
@bot.message_handler(commands=['tg'])
def cmd_random(message):
    bot.send_message(message.chat.id, '@ssandess')
@bot.message_handler(commands=['Hello'])
def cmd_random(message):
    helloname = ''
    helloname += 'Hello, ' + str(message.chat.username)
    bot.send_message(message.chat.id, helloname)
"""
def request_current_weather(city_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': appid})
        data = res.json()
        print("conditions:", data['weather'][0]['description'])
        print("temp:", data['main']['temp'])
        print("temp_min:", data['main']['temp_min'])
        print("temp_max:", data['main']['temp_max'])
        #print("data:", data)
    except Exception as e:
        print("Exception (weather):", e)
        pass
"""

"""
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    url_button = types.InlineKeyboardButton(text="VK", url="https://vk.com/daniilshishov39")
    callback_button = types.InlineKeyboardButton(text="Привет", callback_data="test")
    switch_button = types.InlineKeyboardButton(text="Switch", switch_inline_query="Telegram")
    keyboard.add(url_button, callback_button, switch_button)
    bot.send_message(message.chat.id, "Да да я", reply_markup=keyboard)
"""

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Привет, пользователь!")
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Привет, пользователь!")
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Привет, пользователь")

weather_get = ''
weather_out = dict.copy(data['main'])
"""
for key, value in weather_out.items():
    print(str(key), " : " , str(value))
    """
weather_get += data['weather'][0]['description'] + "\n"
for key, value in weather_out.items():
    weather_get += str(key) + ": " + str(value) + "\n"

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'i love u':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'chat' :
        print(message.chat)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button = types.InlineKeyboardButton(text="VK", url="https://vk.com/daniilshishov39")
        callback_button = types.InlineKeyboardButton(text="Привет", callback_data="test")
        switch_button = types.InlineKeyboardButton(text="Поприветствовать другого", switch_inline_query="heh, здарова")
        keyboard.add(url_button, callback_button, switch_button)
        bot.send_message(message.chat.id, "Выбирай кнопку или пользуйся доступными командами /commands", reply_markup=keyboard)
            
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
