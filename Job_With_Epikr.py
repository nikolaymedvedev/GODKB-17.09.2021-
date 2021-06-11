import os
import sys
import shutil
from pathlib import Path
from datetime import date
import dell
input("Для запуска программы нажмите Enter: ")
def Copy_in_tmp():
    shutil.copytree("S:/Медперсонал/Эпикризы для отправки/", "S:/Медперсонал/tmp_epikr/")

""" ___________Удаление файлов < 0kb__________"""

def Brag_0():
    basedir = "S:/Медперсонал/tmp_epikr/Брагин ЦРБ/"
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

def Bud_Koshel_0():
    basedir = "S:/Медперсонал/tmp_epikr/Буда-Кошелево ЦРБ"
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

def Vetka_0():
    basedir = "S:/Медперсонал/tmp_epikr/Ветка ЦРБ"
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

def GCGDP_0():
    basedir = "S:/Медперсонал/tmp_epikr/ГЦГДКП"
    names = os.listdir(basedir)
    paths = [os.path.join(basedir, name) for name in names]
    sizes = [(path, os.stat(path).st_size) for path in paths]    
    for element in sizes:
        listik = []
        a = listik.append(element[1])
        for i in listik:
            if i == 0 or i == 1:
                os.remove(element[i])
                print("Удален файл:", element[i])

def Dobrush_0():
    basedir = "S:/Медперсонал/tmp_epikr/Добруш ЦРБ"
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

def Elisk_0():
    basedir = "S:/Медперсонал/tmp_epikr/Ельск ЦРБ"
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

def Jitkovichi_0():
    basedir = "S:/Медперсонал/tmp_epikr/Житковичи ЦРБ"
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

def jlobin_0():
    basedir = "S:/Медперсонал/tmp_epikr/Жлобин ЦРБ"
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

def Kalinkovichi_0():
    basedir = "S:/Медперсонал/tmp_epikr/Калинковичи ЦРБ"
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

def Korma_0():
    basedir = "S:/Медперсонал/tmp_epikr/Корма ЦРБ"
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

def Lelichitsi_0():
    basedir = "S:/Медперсонал/tmp_epikr/Лельчицы ЦРБ"
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

def Loev_0():
    basedir = "S:/Медперсонал/tmp_epikr/Лоев ЦРБ"
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

def Mozir_0():
    basedir = "S:/Медперсонал/tmp_epikr/Мозырь ЦРБ"
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

def Narovlia_0():
    basedir = "S:/Медперсонал/tmp_epikr/Наровля ЦРБ"
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

def Oktiabri_0():
    basedir = "S:/Медперсонал/tmp_epikr/Октябрь ЦРБ"
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

def Petrikov_0():
    basedir = "S:/Медперсонал/tmp_epikr/Петриков ЦРБ"
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

def Rechitsa_0():
    basedir = "S:/Медперсонал/tmp_epikr/Речица ЦРБ"
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

def Rogachov_0():
    basedir = "S:/Медперсонал/tmp_epikr/Рогачев ЦРБ"
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

def Svetlogorsk_0():
    basedir = "S:/Медперсонал/tmp_epikr/Светлогорск ЦРБ"
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

def Choiniki_0():
    basedir = "S:/Медперсонал/tmp_epikr/Хойники ЦРБ"
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

def Chechersk_0():
    basedir = "S:/Медперсонал/tmp_epikr/Чечерск ЦРБ"
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


Brag_Route = "S:/Медперсонал/tmp_epikr/Брагин ЦРБ/"
def Brag_tip():
    for event in os.listdir(Brag_Route):
        infilename = os.path.join(Brag_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Buda_Route = "S:/Медперсонал/tmp_epikr/Буда-Кошелево ЦРБ/"
def Buda_koshel_tip():
    for event in os.listdir(Buda_Route):
        infilename = os.path.join(Buda_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Vetka_Route = "S:/Медперсонал/tmp_epikr/Ветка ЦРБ/"
def Vetka_tip():
    for event in os.listdir(Vetka_Route):
        infilename = os.path.join(Vetka_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

GCGDP_Route = "S:/Медперсонал/tmp_epikr/ГЦГДКП/"
def GCGDP_tip():
    for event in os.listdir(GCGDP_Route):
        infilename = os.path.join(GCGDP_Route,event)
        if not os.path.isfile(infilename):
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Dobrish_Route = "S:/Медперсонал/tmp_epikr/Добруш ЦРБ/"
def Dobrush_tip():
    for event in os.listdir(Dobrish_Route):
        infilename = os.path.join(Dobrish_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Elisk_Route = "S:/Медперсонал/tmp_epikr/Ельск ЦРБ/"
def Elisk_tip():
    for event in os.listdir(Elisk_Route):
        infilename = os.path.join(Elisk_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Jitk_Route = "S:/Медперсонал/tmp_epikr/Житковичи ЦРБ/"
def Jitkovichi_tip():
    for event in os.listdir(Jitk_Route):
        infilename = os.path.join(Jitk_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Jlob_Route = "S:/Медперсонал/tmp_epikr/Жлобин ЦРБ/"
def jlobin_tip():
    for event in os.listdir(Jlob_Route):
        infilename = os.path.join(Jlob_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Kalin_Route = "S:/Медперсонал/tmp_epikr/Калинковичи ЦРБ/"
def Kalinkovichi_tip():
    for event in os.listdir(Kalin_Route):
        infilename = os.path.join(Kalin_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Korm_Route = "S:/Медперсонал/tmp_epikr/Корма ЦРБ/"
def Korma_tip():
    for event in os.listdir(Korm_Route):
        infilename = os.path.join(Korm_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Lelich_Route = "S:/Медперсонал/tmp_epikr/Лельчицы ЦРБ/"
def Lelichitsi_tip():
    for event in os.listdir(Lelich_Route):
        infilename = os.path.join(Lelich_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Loev_Route = "S:/Медперсонал/tmp_epikr/Лоев ЦРБ/"
def Loev_tip():
    for event in os.listdir(Loev_Route):
        infilename = os.path.join(Loev_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Mozir_Route = "S:/Медперсонал/tmp_epikr/Мозырь ЦРБ/"
def Mozir_tip():
    for event in os.listdir(Mozir_Route):
        infilename = os.path.join(Mozir_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Narov_Route = "S:/Медперсонал/tmp_epikr/Наровля ЦРБ/"
def Narovlia_tip():
    for event in os.listdir(Narov_Route):
        infilename = os.path.join(Narov_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Okt_Route = "S:/Медперсонал/tmp_epikr/Октябрь ЦРБ/"
def Oktiabri_tip():
    for event in os.listdir(Okt_Route):
        infilename = os.path.join(Okt_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Petr_Route = "S:/Медперсонал/tmp_epikr/Петриков ЦРБ/"
def Petrikov_tip():
    for event in os.listdir(Petr_Route):
        infilename = os.path.join(Petr_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Rech_Route = "S:/Медперсонал/tmp_epikr/Речица ЦРБ/"
def Rechitsa_tip():
    for event in os.listdir(Rech_Route):
        infilename = os.path.join(Rech_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Rog_Route = "S:/Медперсонал/tmp_epikr/Рогачев ЦРБ/"
def Rogachov_tip():
    for event in os.listdir(Rog_Route):
        infilename = os.path.join(Rog_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Svetl_Route = "S:/Медперсонал/tmp_epikr/Светлогорск ЦРБ/"
def Svetlogorsk_tip():
    for event in os.listdir(Svetl_Route):
        infilename = os.path.join(Svetl_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Choin_Route = "S:/Медперсонал/tmp_epikr/Хойники ЦРБ/"
def Choiniki_tip():
    for event in os.listdir(Choin_Route):
        infilename = os.path.join(Choin_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

Chech_Route = "S:/Медперсонал/tmp_epikr/Чечерск ЦРБ/"
def Chechersk_tip():
    for event in os.listdir(Chech_Route):
        infilename = os.path.join(Chech_Route,event)
        if not os.path.isfile(infilename):
            print("Файлов необнаружено")
            continue
        oldbase = os.path.splitext(event)
        newname = infilename.replace('.tmp', '.doc')
        output = os.rename(infilename, newname)
        print("Файлы перетипизирован:", event)

"""_______________Содание новой дирректории и копирование туда файлов_____________"""

def Copy_mkdir():
    try:
    	a = str(date.today())
    	path = f"S:/Медперсонал/Архив отправленных эпикризов/2021/Июнь/{a}"
    	shutil.copytree("S:/Медперсонал/tmp_epikr/", path)
    except FileExistsError:
        print(f"Папка с именем {a} уже существует!!!\nУдалите сначала эту папку!!!")
        input("Для ее удаления нажмите клавишу 'Y': ")
        shutil.rmtree(f'S:/Медперсонал/Архив отправленных эпикризов/2021/Июнь/'+ str(date.today()))
        print("Папка "+ str(date.today()) + " Была создана заново")
        print ("Начато повторное копирование файлов в архивную папку:", str(date.today()), "...")
        b = str(date.today())
        path = f"S:/Медперсонал/Архив отправленных эпикризов/2021/Июнь/{b}"
        shutil.copytree("S:/Медперсонал/tmp_epikr/", path)




"""______________Удаление временной папки temp_epikr_____________"""

def Dell_tmp_epikr():
    shutil.rmtree('S:/Медперсонал/tmp_epikr/')

if __name__ == "__main__":
    def main():
        print(f"Идет копирование файлов в папку 'tmp_epikr' ...")
        Copy_in_tmp()
        print("Удаляются файлы нулевого размера")
        Brag_0()
        Bud_Koshel_0()
        Vetka_0()
        GCGDP_0()
        Dobrush_0()
        Elisk_0()
        Jitkovichi_0()
        jlobin_0()
        Kalinkovichi_0()
        Korma_0()
        Lelichitsi_0()
        Loev_0()
        Mozir_0()
        Narovlia_0()
        Oktiabri_0()
        Petrikov_0()
        Rechitsa_0()
        Rogachov_0()
        Svetlogorsk_0()
        Choiniki_0()
        Chechersk_0()
        print("Успешно")
        print("Идет перетипизация файлов")
        Brag_tip()
        Buda_koshel_tip()
        Vetka_tip()
        GCGDP_tip()
        Dobrush_tip()
        Elisk_tip()
        Jitkovichi_tip()
        jlobin_tip()
        Kalinkovichi_tip()
        Korma_tip()
        Lelichitsi_tip()
        Loev_tip()
        Mozir_tip()
        Narovlia_tip()
        Oktiabri_tip()
        Petrikov_tip()
        Rechitsa_tip()
        Rogachov_tip()
        Svetlogorsk_tip()
        Choiniki_tip()
        Chechersk_tip()
        print("Успешно")
        print ("Начато копирование файлов в архивную папку:", str(date.today()), "...")
        Copy_mkdir()
        print("Копирование файлов завершено")
        print("Удаление временной папки temp_epikr")
        Dell_tmp_epikr()
        print("Удаление завершено")
        dell.dell()


main()