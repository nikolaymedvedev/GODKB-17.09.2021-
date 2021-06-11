import os
import sys
import shutil
from datetime import date
def Copy_mkdir():
    try:
        a = str(date.today())
        path = f"S:/Медперсонал/Архив отправленных эпикризов/2021/Июнь/{a}"
        shutil.copytree("S:/Медперсонал/tmp_epikr/", path)
    except FileExistsError:
        print(f"Папка с именем {a} уже существует\nУдалите сначала эту папку!!!")

Copy_mkdir()