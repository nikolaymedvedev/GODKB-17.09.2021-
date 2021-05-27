from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
import math
config_dict['language'] = 'ru'
owm = OWM('3195a3e22b9c92b203bb5dffdde84cb8', config_dict)
mgr = owm.weather_manager()
place = input("Выберете город: ")
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius') ["temp"]
temp_max = w.temperature('celsius') ["temp_max"]
temp_min = w.temperature('celsius') ["temp_min"]
print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура в " + place + " сейчас " + str(math.ceil(temp)) + " градусов")
print ("Максимальная температура: " + str(math.ceil(temp_max))+ "грудусов")
print ("Минимальная температура: " + str (math.ceil(temp_min)) + "градусов")
if temp < 10:
	print ("Сейчас на улице очень холодно")
elif temp < 20:
	 print ("Можно на лясе")
elif temp > 20:
	print("Жара!!!!")