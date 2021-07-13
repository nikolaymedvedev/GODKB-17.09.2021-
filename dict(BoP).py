import time
from pickle import dump, load
End = False
class Personals:
	d = {}
	def __init__(self, name, age):
			self.name = name
			self.age = age
	def add_dict(self):
		Personals.d[f"{self.name}"] = self.age
	
	def dell_dict():
		del(Personals.d[key])
	
	def load_at_file():
		with open("test.txt", "rb") as f:
			Personals.d = load(f)
	
	def dump_in_file():
		with open("test.txt", "wb") as f:
			dump(Personals.d, f)
	
	def read():
		f = open("test.txt", "rt")
		a = f.read()
		print(a)
	
	def loock_one():
		vvod00 = input("Ведите имя контакта для просмотра данных:\n")
		for i in Personals.d.keys():
			if i == vvod00:
				time.sleep(1)
				print(f"Контактные данные '{vvod00}':",  Personals.d[vvod00])
				time.sleep(1)
		if vvod00 not in Personals.d.keys():
			time.sleep(1)
			print("Данные '{0}' не найдены\nВыход в главное меню..".format(vvod00))
			time.sleep(1)

try:
	while not End:
		vvod = input("Введите действия: 1)Посмотреть; 2)Изменить (<Ctrl+C>_выйти из программы): \n")
		if vvod == "1":
			vvod0 = input("1)Найти данные; 2)Просмотреть все: \n")
			if vvod0 == "1":
				try:	
					Personals.load_at_file()
					Personals.loock_one()
				except EOFError:
					print(f"Ваш словарь пока еще пуст: {Personals.d}")
					print("Выход в главное меню..")
					time.sleep(1)
			elif vvod0 == "2":
				try:	
					Personals.load_at_file()
					print("Ваш словарь:", str(Personals.d))
				except EOFError:
					print('Словарь пуст:', Personals.d)
			else:
				print("Выход в главное меню..")
				time.sleep(1)
		elif vvod == "2":
			vvod1 = input("1)Добавить; 2)Удалить \n")
			if vvod1 == "1":
				try:
					Personals.load_at_file()
					key = input("Введите имя: ")
					if len(key) == 0:
						print("Вы ничего не ввели!\nВыход в главное меню..")
						time.sleep(2)
						pass
					else:
						value = input("Введите контактные данные: ")
						if len(value) == 0:
							print("Вы ничего не ввели!\nВыход в главное меню..")
							time.sleep(2)
						else:
							a = Personals(key, value)
							a.add_dict()
							print("Идет сохранение данных..")
							time.sleep(3)
							Personals.dump_in_file()
				except EOFError:
					print("Словарь пуст, записываем данные в файл..")
					time.sleep(3)
					print("Повторите пожалуйста еще раз эту операцию")
					Personals.dump_in_file()
				print("Ваша записная книжка выглядит следующим образом", Personals.d)
			elif vvod1 == "2":
				try:
					Personals.load_at_file()
					print("\nВаш словарь:", Personals.d) 
					key = input("Введите имя которое хотите удалить из словаря: ")

					if len(key) == 0:
						time.sleep(2)
						print("Вы ничего не ввели!\nВыход в главное меню..")
						time.sleep(1)
						pass
					else:
						Personals.dell_dict()
						print("Обновление записной книжки..")
						time.sleep(1)
						print("Ваша записная книжка выглядит следующим образом: ", Personals.d)
						Personals.dump_in_file()
				except EOFError:
					print("Невозможно удалить из пустого словаря!")
					print("Выход в главное меню..")
					Personals.dump_in_file()
					time.sleep(2)
				except KeyError:
					time.sleep(1)
					print("Контакта %s не существует!\n" % (key))			
		else:
			print("Введите действия!")
except KeyboardInterrupt:
	print("\nВыход из программы...")
	time.sleep(1)