# -*- coding: utf-8 -*-
import config
import telebot
import requests
s_city = "Moscow,RU"
city_id = 524901
appid = config.appid
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': appid})
data = res.json()

bot = telebot.TeleBot(config.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('hello', 'tg', 'vkpage', 'weather')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

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
        #request_current_weather(city_id)
        bot.send_message(message.chat.id, "conditions:")
        bot.send_message(message.chat.id, data['weather'][0]['description'])
        bot.send_message(message.chat.id, "temp")
        bot.send_message(message.chat.id, data['main']['temp'])
        bot.send_message(message.chat.id, "temp_min:")
        bot.send_message(message.chat.id, data['main']['temp_min'])
        bot.send_message(message.chat.id, "temp_max")
        bot.send_message(message.chat.id, data['main']['temp_max'])
            
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
