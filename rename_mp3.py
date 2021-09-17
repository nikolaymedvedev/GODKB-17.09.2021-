import os
import time

def asd(route, name_gruop):
	n = 0
	for event in os.listdir(route):
		n += 1
		new = []
		files = os.path.join(route, event)
		gruop = name_gruop.split(" ")
		for i in event:
			split_text = event.split("-")
		for i in split_text:
			upper_text = i.replace(i[0], i[0].upper())
			if upper_text not in gruop:
				new.append(upper_text)
		new_name = " ".join(new)
		new_name1 = route + "/" + "0" + str(n) + ". " + new_name
		output = os.rename(files, new_name1) 
		print(f"Песня: \"{event}\" переименована")
		time.sleep(1)
		
asd(r"C:\Users\nmedvedev\Desktop\Freak Out! (2012)", "Teenage Bottlerocket")


