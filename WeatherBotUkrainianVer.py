import pyowm
import telebot

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'uk'
owm = OWM('dfc8f65597d21cfb5dd4409621bb31f6', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']

    answer = 'У місті ' + message.text + ' зараз ' + w.detailed_status + '\n'
    answer += 'Температура зараз приблизно в районі десь ' + str(temp) + ' градусів' + '\n\n'

    if temp < 10:
        answer += 'Холодрига на вулиці, краще не виходити сьогодні взагалі'
    elif temp < 20:
        answer += 'Холодно на вулиці, одягай щось тепле'
    else:
        answer += 'Норм, одягай що хочеш'

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )