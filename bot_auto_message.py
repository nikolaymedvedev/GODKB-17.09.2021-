import schedule
import telebot
import time
print("Бот активирован!")

bot = telebot.TeleBot("1329901094:AAGWu4A1ICJWYg__gONJXYUcc-2H52uzTBU")

@bot.message_handler()
def otvet_bot():
	if time.strftime('%d.%m') == "22.05":
		bot.send_message(-594023162, "Сегодня день рождения:\nНиколая Медведева") #здесь первый аргумент это id чата
	elif time.strftime('%d.%m') == "30.07":
		bot.send_message(-594023162, "Сегодня день рождения:\nИрины Замореевой!")

schedule.every().day.at("12:00").do(otvet_bot)

while 1: 
	schedule.run_pending() # заработает шаблон вызывающий функцию otvet_bot
	time.sleep(1)
	

"""
727952053 - user_id
-594023162 - chat_id
"""

