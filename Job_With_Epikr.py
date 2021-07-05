import os
import sys
import shutil
from pathlib import Path
import time
import dell

input("Для запуска программы нажмите Enter: ")

def Copy_in_tmp(n, m):
    try:
        shutil.copytree(n, m)
    except FileExistsError:
        print("Папка tmp_epikr уже существует")
        input("нажмите \"Enter\" для ее удаления")
        shutil.rmtree(m)
        print ("Начато повторное копирование файлов в папку tmp_epikr...:")
        shutil.copytree(n, m)

""" ___________Удаление файлов < 0kb__________"""

def Del_0(n):
    basedir = n
    names = os.listdir(basedir)
    paths = [os.path.join(basedir, name) for name in names]
    sizes = [(path, os.stat(path).st_size) for path in paths]    
    for element in sizes:
        listik = []
        a = listik.append(element[1])
        for i in listik:
            if i == 0:
                os.remove(element[i])
                print("Удален файл:", element[i])

""" ___________Перетипизация файлов__________"""

def Tip(n):
    for event in os.listdir(n):
        infilename = os.path.join(n,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

"""_______________Содание новой дирректории и копирование туда файлов_____________"""

def Copy_mkdir(n, m):
    try:
    	a = str(time.strftime('%d.%m.%Y'))
    	path = f"{n}{a}"
    	shutil.copytree(m, path)
    except FileExistsError:
        print(f"Папка с именем {a} уже существует!!!\nУдалите сначала эту папку!!!")
        input("Для ее удаления нажмите клавишу 'Enter': ")
        shutil.rmtree(f'{n}'+ str(time.strftime('%d.%m.%Y')))
        print("Папка "+ str(time.strftime('%d.%m.%Y')) + " Была создана заново")
        print ("Начато повторное копирование файлов в архивную папку:", str(time.strftime('%d.%m.%Y')), "...")
        b = str(time.strftime('%d.%m.%Y'))
        path = f"{n}{b}"
        shutil.copytree(m, path)

def Dell_tmp_epikr(n):
    shutil.rmtree(n)

if __name__ == "__main__":
	def main():
		print(f"Идет копирование файлов в папку 'tmp_epikr' ...")
		Copy_in_tmp("S:/Медперсонал/Эпикризы для отправки/", "S:/Медперсонал/tmp_epikr/")
		print("Удаляются файлы нулевого размера")
		Del_0("S:/Медперсонал/tmp_epikr/Брагин ЦРБ/")
		Del_0("S:/Медперсонал/tmp_epikr/Буда-Кошелево ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Ветка ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/ГЦГДКП")
		Del_0("S:/Медперсонал/tmp_epikr/Добруш ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Ельск ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Житковичи ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Жлобин ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Калинковичи ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Корма ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Лельчицы ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Лоев ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Мозырь ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Наровля ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Октябрь ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Петриков ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Речица ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Рогачев ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Светлогорск ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Хойники ЦРБ")
		Del_0("S:/Медперсонал/tmp_epikr/Чечерск ЦРБ")
		print("Успешно")
		time.sleep(3)
		print("Идет перетипизация файлов")
		time.sleep(2)
		Tip("S:/Медперсонал/tmp_epikr/Брагин ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Буда-Кошелево ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Ветка ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/ГЦГДКП/")
		Tip("S:/Медперсонал/tmp_epikr/Добруш ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Ельск ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Житковичи ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Жлобин ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Калинковичи ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Корма ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Лельчицы ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Лоев ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Мозырь ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Наровля ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Октябрь ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Петриков ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Речица ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Рогачев ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Светлогорск ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Хойники ЦРБ/")
		Tip("S:/Медперсонал/tmp_epikr/Чечерск ЦРБ/")
		print("Успешно")
		time.sleep(3)
		print ("Начато копирование файлов в архивную папку:", str(time.strftime('%d.%m.%Y')), "...")
		Copy_mkdir("S:/Медперсонал/Архив отправленных эпикризов/2021/Июль/", "S:/Медперсонал/tmp_epikr/")
		print("Копирование файлов завершено")
		time.sleep(3)
		print("Удаление временной папки temp_epikr")
		Dell_tmp_epikr('S:/Медперсонал/tmp_epikr/')
		print("Удаление завершено")
		time.sleep(2)
		dell.dell()


main()