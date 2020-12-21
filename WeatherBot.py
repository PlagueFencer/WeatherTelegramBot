import pyowm
import telebot

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('dfc8f65597d21cfb5dd4409621bb31f6', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("1424640295:AAGK-eTOjFaEsSSBYinGYW50uh2E7m8-Ugw")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']

    answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
    answer += 'Температура сейчас в районе ' + str(temp) + ' градуса' + '\n\n'

    if temp < 10:
        answer += 'Сейчас ппц как холодно, одевайся как танк!'
    elif temp < 20:
        answer += 'Сейчас холодно, оденься потеплее'
    else:
        answer += 'Температура норм, одевай что угодно'

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )