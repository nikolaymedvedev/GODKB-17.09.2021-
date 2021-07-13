""" Открывает файл текстовый или вордовский, но только если сам .doc записан в utf-8 """

import os
import glob
import shutil
import time

def read_copy(n, m, k):
#n -  Слово которое мы должны прочитать, m - дирректория где находятся текстовые файлы, k - дирректория куда мы будем перемещать файлы с ключевым словом n
	a = []
	new = []
	for i in glob.glob(m): 
		if i in glob.glob(m):
			if os.path.isfile(i):
				print("Найден файл:", i)
				time.sleep(2)
				f = open(i, "r", encoding = "utf-8")
				try:
					while True:
						line = f.readline()
						if len(line) == 0:
							break
						if "ГЦГДКП" in line:	
							shutil.copy(i, k)
							print("В файле {0} найдено совпадение!\nОн будт перемещен..".format(i))
							f.close()
							os.remove(i)
							time.sleep(2)
							print("Готово!")
							time.sleep(1)
					if "ГЦГДКП" not in line:
						print("В файле \"{0}\" совпадений не найдено! ".format(i))
						time.sleep(2)			
				except ValueError:
					f.close()
					print("файл \"{0}\" закрыт".format(i))
					time.sleep(1)
	print("Программа завершена успешно!")

read_copy("ГЦГДКП", "C:/Users/nmedvedev/Desktop/123/*", "C:/Users/nmedvedev/Desktop/TEST")