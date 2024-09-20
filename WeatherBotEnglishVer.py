import pyowm
import telebot

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'en'
owm = OWM('dfc8f65597d21cfb5dd4409621bb31f6', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']

    answer = 'In town ' + message.text + ' now ' + w.detailed_status + '\n'
    answer += 'Temperature is now ' + str(temp) + ' degree celsius' + '\n\n'

    if temp < 10:
        answer += 'Better to stay at home today'
    elif temp < 20:
        answer += 'Wear something warm'
    else:
        answer += 'Wear anything you want'

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )