"""
_______________muzkloud Yellowcard______________
from requests import get
from bs4 import BeautifulSoup as bs

r = get("https://w1.musify.club/artist/yellowcard-144/releases")
html = bs(r.content, "html.parser")
for i in html.select(".card-deck > .release-thumbnail"):
	title = i.select(".card-subtitle > a")
	print(title[0].text)
	
"""
"""
_______________Новости Кинопоиска______________
import requests
from bs4 import BeautifulSoup as bs

page = 1
while True:
	url = 'https://www.kinopoisk.ru/media/news/?page='
	r = requests.get(url + str(page))
	html = bs(r.content, "html.parser")
	items = html.select(".posts-grid__row > .posts-grid__main-section-column")
	if len(items):
		for i in items:
			print(i.text)
		page += 1
	else:
		break

"""
"""
_______________Новости ГОДКБ______________
import requests
from bs4 import BeautifulSoup as bs

page = 0
news = 0
while True:	
	url = 'https://www.godkb.by/news.html'
	r = requests.get(url)
	html = bs(r.content, "html.parser")ы
	items = html.select(".items-leading > .leading-" + str(page))
	if len(items):
		for i in items:
			page += 1
			news +=1
			title = i.select("a")
			print(news, title[0].text)
	else:
		break

"""
"""
_______________Погода на неделю______________
import requests
from bs4 import BeautifulSoup as bs

url = 'https://yandex.by/pogoda/gomel'
r = requests.get(url)
html = bs(r.content, "html.parser")
items = html.select(".forecast-briefly__day")
print(items[0].text,"\n", 
	items[1].text,"\n", 
	items[2].text,"\n", 
	items[3].text,"\n", 
	items[4].text,"\n", 
	items[5].text,"\n", 
	items[6].text,"\n",
	items[7].text,"\n",
	items[8].text,
	)

"""
"""
_______________Температура сейчас______________
from requests import get
from bs4 import BeautifulSoup as bs

r = get("https://world-weather.ru/pogoda/belarus/gomel/")
html = bs(r.content, "html.parser")
title = html.select(".weather-now-info")
result = title[0].text
print(f"{result[0:6]}({result[6:11]}): {result[18:]}℃")

"""
"""
_______________Курс долара от select.by_______________
from requests import get
from bs4 import BeautifulSoup as bs

r = get("https://select.by/kurs/gomel") 
html = bs(r.content, "html.parser")
item = html.select(".mb-3 > .p-3 ")
tkurs = item[0].text.split("\n")

pok = tkurs[22]
prod = tkurs[30]

print(f"Курс долара США:\nПокупка: {pok} бр.\nПродажа: {prod} бр.")

"""
"""

_______________Курс долара от Нацбанка_________________
from requests import get
from bs4 import BeautifulSoup as bs

r = get("https://www.nbrb.by/statistics/rates/ratesdaily.asp")
html = bs(r.content, "html.parser")
item = html.select(".currencyTable")
for i in item:
	title =  i.select(".curCours")
	print(f"Долар США на сегодня(BYN):{title[5].text}")

"""
"""
_______________Курсы валют всех банков РБ______________
from requests import get
from bs4 import BeautifulSoup as bs
banks = [
		"Абсолютбанк", "Паритетбанк", "Банк Решение",
		"БНБ-Банк","Альфа-Банк", "Белинвестбанк",
		"ТехноБанк", "РРБ-Банк", "Франсабанк",
		"Банк Дабрабыт", "Приорбанк", "Белгазпромбанк",
		"МТБанк", "Идея Банк", "БПС-Сбербанк",
		"Белагропромбанк", "ВТБ Беларусь"
		]
r = get("https://select.by/kurs/gomel") 
html = bs(r.content, "html.parser")
item = html.select(".no-gutters > .mx-2 > .mb-3")
info = item[0].text.split("\n")		
for elem in info:
	for bank in banks:
		if elem == bank:
			print(f"{info[info.index(elem)]}: покупка:{info[info.index(elem) + 3]}, продажа:{info[info.index(elem) + 4]}")

"""
"""
_______________Стоимость топлива на БелАЗС______________
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
	print(f"{AI92.rstrip()} руб;\n{AI95.rstrip()} руб;\n{AI98.rstrip()} руб;\n{GAZ.rstrip()} руб;\n{DIZ.rstrip()} руб.")

"""
"""
_______________С av.by passsat b3______________
import requests
from bs4 import BeautifulSoup as bs
page = 1
while True:
	url = "https://cars.av.by/filter?brands[0][brand]=1216&brands[0][model]=5912&page="
	r = requests.get(url + str(page))
	html = bs(r.content, "html.parser")
	items = html.select(".listing-item__wrap")
	if len(items):
		for i in items:
			title = i.select(".listing-item__about > .listing-item__title")
			title1 = i.select(".listing-item__params")
			title2 = i.select(".listing-item__prices")
			title3 = i.select(".listing-item__photo")
			print(f" {title3}\n\n {title[0].text} ({title1[0].text}) Цена:, {title2[0].text}")
		page += 1
	else:
		break
"""