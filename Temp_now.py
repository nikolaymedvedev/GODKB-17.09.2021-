# Импортируем бота;
import telebot
# Подключаем округление;
import math
# Импортируем погодный патч;
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
# Русификация погоды;
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
# Установка индентификационного ключа;
owm = OWM('3195a3e22b9c92b203bb5dffdde84cb8')
mgr = owm.weather_manager ()
# Установка id ключа для бота;
bot = telebot.TeleBot("1329901094:AAGWu4A1ICJWYg__gONJXYUcc-2H52uzTBU")
# Подключаем обработчик входящих сообщений
@bot.message_handler(func=lambda message: True)
def otvet_bot(message):
# Вставка для определения текущей погоды из текстового сообщения;
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
# Вывод текущкей температуры, максимальной, минимальной и обращение к модулю [temp];
	temp = w.temperature('celsius') ["temp"]
	temp_max = w.temperature('celsius') ["temp_max"]
	temp_min = w.temperature('celsius') ["temp_min"]
# Вывод в переменную текстового сообщения;
	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer = answer + "Температура в " + message.text + " составляет " + str(math.ceil(temp)) + " градусов" + "\n"
	answer = answer + "Максимальная температура воздуха по области состовляет: " + str(math.ceil(temp_max))+ "\n"
	answer = answer + "Минимальная температура воздуха по области состовляет: " + str (math.ceil(temp_min)) + " градусов " + "\n"
	# Логическая операция;
	if temp < 0:
		answer = answer + "Сейчас на улице очень холодно"
	elif temp < 10:
		answer = answer + "На улице холодно"
	elif temp < 20:
		answer = answer + "На улице тепло)"
	elif temp > 20:
		answer = answer + "На улице очень жарко!!!"
	bot.send_message(message.chat.id, answer)
# Строка для вывода данных (если она есть, программа не закроется);
bot.polling()