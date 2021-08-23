import telebot
import schedule
import time
from requests import get
from bs4 import BeautifulSoup as bs
print("Бот активирован!")
bot = telebot.TeleBot("1329901094:AAGWu4A1ICJWYg__gONJXYUcc-2H52uzTBU")
@bot.message_handler(content_types=['text'])
def otvet_bot(message):
	d = {
	"1":"0748", "2":"9592", "3":"9300", "4":"9192", "5":"0664",
	"6":"3582", "7":"7580", "8":"3990", "9":"8071", "10":"5504", "11":"4762",
	"12":"3861", "13":"0974", "14":"2451", "15":"5602", "16":"9018",
	"17":"3326", "18":"5798", "19":"0031", "20":"9474", "21":"0640",
	"22":"2039", "23":"8739","24":"8567", "25":"8381", "26":"7490",
	"27":"7829", "28":"1517", "29":"0259", "30":"2897", "31":"9038",
	"32":"0840", "33":"4218", "34":"5833", "35":"5307", "36":"2904",
	"37":"6315", "38":"4328", "39":"1546","40":"1656"
	}	
	banks = [
			"Абсолютбанк", "Паритетбанк", "Банк Решение",
			"БНБ-Банк","Альфа-Банк", "Белинвестбанк",
			"ТехноБанк", "РРБ-Банк", "Франсабанк",
			"Банк Дабрабыт", "Приорбанк", "Белгазпромбанк",
			"МТБанк", "Идея Банк", "БПС-Сбербанк",
			"Белагропромбанк", "ВТБ Беларусь"
			]
	def kurs_bank():
		r = get("https://select.by/kurs/gomel") 
		html = bs(r.content, "html.parser")
		item = html.select(".no-gutters > .mx-2 > .mb-3")
		info = item[1].text.split("\n")		
		for elem in info:
			for bank in banks:
				if elem == bank:
					bot.send_message(message.chat.id, f"{info[info.index(elem)]}:\nПродажа: {info[info.index(elem) + 4]} б.р\nПокупка: {info[info.index(elem) + 3]} б.р")
	def kurs():
		r = get("https://select.by/kurs/gomel") 
		html = bs(r.content, "html.parser")
		item = html.select(".mb-3 > .p-3 ")
		tkurs = item[0].text.split("\n")
		pok = tkurs[22]
		prod = tkurs[30]
		bot.send_message(message.chat.id, f"Курс долара США:\nПродажа: {prod} б.р\nПокупка: {pok} б.р")
	def toplivo():
		r = get("https://azs.belorusneft.by/sitebeloil/ru/center/azs/center/fuelandService/price")
		html = bs(r.content, "html.parser")
		item = html.select(".b-left__informer")
		for i in item:
			title = i.select(".col2")
			AI92 = f"{title[0].text}: {title[2].text}"
			AI95 = f"{title[1].text}: {title[3].text}".replace(",", "")
			AI98 = f"{title[4].text}: {title[6].text}"
			GAZ = f"{title[5].text}: {title[7].text}".replace(" ", "-", 1)
			DIZ = f"{title[8].text}: {title[9].text}"
			bot.send_message(message.chat.id, f"Стоимость топлива:\n{AI92.rstrip()} б.р;\n{AI95.rstrip()} б.р;\n{AI98.rstrip()} б.р;\n{GAZ.rstrip()} б.р;\n{DIZ.rstrip()} б.р")
	def pogoda_nedel():
		r = get('https://yandex.by/pogoda/gomel')
		html = bs(r.content, "html.parser")
		items = html.select(".forecast-briefly__day")
		status = items[1].text.replace(" ","")
		bot.send_message(message.chat.id, f"{status}")
		status = items[2].text.replace(" ","")
		bot.send_message(message.chat.id, f"Завтра: {status}")
		for day in range(3, 9):
			status = items[day].text.replace(" ","")
			bot.send_message(message.chat.id, f"{status}")
	def temp_now():
		r = get("https://world-weather.ru/pogoda/belarus/gomel/")
		html = bs(r.content, "html.parser")
		title = html.select(".weather-now-info")
		result = (title[0].text)
		bot.send_message(message.chat.id, f"{result[0:6]}({result[6:11]}): {result[19:]}C")
	key = (list(d.keys()))
	val = (list(d.values()))
	if message.text in key:
		bot.send_message(message.chat.id, d[message.text])	
	elif message.text == "/kurs_bank" or message.text == "Курсы" or message.text == "Курсы в банках":
		kurs_bank()
	elif message.text == "/kurs" or message.text == "Курс":
		kurs()
	elif message.text == "/toplivo" or message.text == "Топливо":
		toplivo()
	elif message.text == "/pogoda_nedel" or message.text == "Погода на неделю":
		pogoda_nedel()
	elif message.text == "/temp_now" or message.text == "Погода сейчас" or message.text == "Температура сейчас" or message.text == "Погода":
		temp_now()
	elif message.text == "/help":
		bot.send_message(message.chat.id, f"Сегодня: {time.strftime('%d.%m.%Yг.')}\n\nВеди:\n/temp_now для просмотра температуры воздуха сейчас\n/pogoda_nedel для просмотра погоды на неделю\n/kurs для актуального курса долара \"$\" на сегодня;\n/kurs_bank для курса долара \"$\" во всех банкх РБ;\n/toplivo для просмотра стоимости топлива на сегодня;\n\nИли просто номер для карты кодов!")
	else:
		bot.send_message(message.chat.id, "Введи \"/help\" для справки")

bot.polling(none_stop=True)