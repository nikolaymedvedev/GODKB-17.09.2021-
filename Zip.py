import os
import time


surse = ['C:/Users/nmedvedev/Desktop/Learn_Python/Python']
main_dir = ['D:/Backup/']         # Главный
target_dir = main_dir + time.strftime('%d.%m.%Y')  #папка в главном
now = time.strftime('%H.%M.%S')  # Время сейчас


сommit = input("Введите коментарий: ")
if len(commit) == 0:
	target = target_dir + "/" + now + ".zip"
else:
	target = target_dir + "/" + now + "(" +commit.replace(" ", "_") + ")" + ".zip"


if not os.path.exists(target_dir):
	os.mkdir(target_dir)
	print("Каталог создан")
else:
	print("Каталог уже есть\nПросто перемещаем туда что есть")


zip_comand = "zip -rq {0} {1}".format(target, surse)
if os.system(zip_comand) == 0:
	print(f"Получилось, папка \"{target}\" заархивирована")
else:
	print(f"Провал, папка \"{target}\" не заархивирована")
