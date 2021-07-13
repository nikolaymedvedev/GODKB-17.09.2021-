vvod = input('Вводи текст: ')
spik = ['!', '?', ' ']
new_spik = []

def reverse(text):
	return text[::-1]

def polindrom(text):
	return text == reverse(text)

for i in vvod:
	if i not in spik:
		new_spik.append(i)

a = ''.join(new_spik)
b = a.lower()

if polindrom(b):
	print("Да, это полиндром!")
else:
	print("Нет, это не полиндром")