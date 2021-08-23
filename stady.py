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
info = item[1].text.split("\n")		
for elem in info:
	for bank in banks:
		if elem == bank:
			print(f"{info[info.index(elem)]}:\nПродажа: {info[info.index(elem) + 4]} б.р\nПокупка: {info[info.index(elem) + 3]} б.р")
	