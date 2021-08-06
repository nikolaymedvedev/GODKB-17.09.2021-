# Это телеграмм бот, присылает пароль по номеру из карты кодов АСБ"Беларусьбанк"
import telebot
print("Бот активирован!")
bot = telebot.TeleBot("1329901094:AAGWu4A1ICJWYg__gONJXYUcc-2H52uzTBU")
@bot.message_handler(content_types=['text'])
def otvet_bot(message):
	d = {"1":"0748", "2":"9592", "3":"9300", "4":"9192", "5":"0664",
	"6":"3582", "7":"7580", "8":"3990", "9":"8071", "10":"5504", "11":"4762",
	"12":"3861", "13":"0974", "14":"2451", "15":"5602", "16":"9018",
	"17":"3326", "18":"5798", "19":"0031", "20":"9474", "21":"0640",
	"22":"2039", "23":"8739","24":"8567", "25":"8381", "26":"7490",
	"27":"7829", "28":"1517", "29":"0259", "30":"2897", "31":"9038",
	"32":"0840", "33":"4218", "34":"5833", "35":"5307", "36":"2904",
	"37":"6315", "38":"4328", "39":"1546","40":"1656"}		
	if message.text == "1":
		bot.send_message(message.chat.id, d["1"])
	elif message.text == "2":
		bot.send_message(message.chat.id, d["2"])
	elif message.text == "3":
		bot.send_message(message.chat.id, d["3"])
	elif message.text == "4":
		bot.send_message(message.chat.id, d["4"])
	elif message.text == "5":
		bot.send_message(message.chat.id, d["5"])
	elif message.text == "6":
		bot.send_message(message.chat.id, d["6"])
	elif message.text == "7":
		bot.send_message(message.chat.id, d["7"])
	elif message.text == "8":
		bot.send_message(message.chat.id, d["8"])
	elif message.text == "9":
		bot.send_message(message.chat.id, d["9"])
	elif message.text == "10":
		bot.send_message(message.chat.id, d["10"])
	elif message.text == "11":
		bot.send_message(message.chat.id, d["11"])
	elif message.text == "12":
		bot.send_message(message.chat.id, d["12"])
	elif message.text == "13":
		bot.send_message(message.chat.id, d["13"])
	elif message.text == "14":
		bot.send_message(message.chat.id, d["14"])
	elif message.text == "15":
		bot.send_message(message.chat.id, d["15"])
	elif message.text == "16":
		bot.send_message(message.chat.id, d["16"])
	elif message.text == "17":
		bot.send_message(message.chat.id, d["17"])
	elif message.text == "18":
		bot.send_message(message.chat.id, d["18"])
	elif message.text == "19":
		bot.send_message(message.chat.id, d["19"])
	elif message.text == "20":
		bot.send_message(message.chat.id, d["20"])
	elif message.text == "21":
		bot.send_message(message.chat.id, d["21"])
	elif message.text == "22":
		bot.send_message(message.chat.id, d["22"])
	elif message.text == "23":
		bot.send_message(message.chat.id, d["23"])
	elif message.text == "24":
		bot.send_message(message.chat.id, d["24"])
	elif message.text == "25":
		bot.send_message(message.chat.id, d["25"])
	elif message.text == "26":
		bot.send_message(message.chat.id, d["26"])
	elif message.text == "27":
		bot.send_message(message.chat.id, d["27"])
	elif message.text == "28":
		bot.send_message(message.chat.id, d["28"])
	elif message.text == "29":
		bot.send_message(message.chat.id, d["29"])
	elif message.text == "30":
		bot.send_message(message.chat.id, d["30"])
	elif message.text == "31":
		bot.send_message(message.chat.id, d["31"])
	elif message.text == "32":
		bot.send_message(message.chat.id, d["32"])
	elif message.text == "33":
		bot.send_message(message.chat.id, d["33"])
	elif message.text == "34":
		bot.send_message(message.chat.id, d["34"])
	elif message.text == "35":
		bot.send_message(message.chat.id, d["35"])
	elif message.text == "36":
		bot.send_message(message.chat.id, d["36"])
	elif message.text == "37":
		bot.send_message(message.chat.id, d["37"])
	elif message.text == "38":
		bot.send_message(message.chat.id, d["38"])
	elif message.text == "39":
		bot.send_message(message.chat.id, d["39"])
	elif message.text == "40":
		bot.send_message(message.chat.id, d["40"])
	else:
		bot.send_message(message.chat.id, "Веди правильно номер кода!")
bot.polling(none_stop=True)