# Реализация собственного метода replace на основе собственного класса str

class Str:

	def __init__(self, text):
		self.text = text
		
	def replaze(self, wh, na):
		self.text = self.text.split(" ")
		wh = wh.split(" ")
		new = []
		for nom, val in enumerate(self.text):
			for val1 in wh:
				if val == val1:
					self.text[nom] = na
		for i in self.text:
			if i not in new:
				new.append(i)	
		new = " ".join(new)
		return new

	def replaze2(self, wh, na):
		text = self.text.split(" ")
		wh = wh.split(" ")
		new = []
		for i in text:
			for j in wh:
				if i == j:
					text[text.index(i)] = na
		for elem in text:
			if elem not in new:
				new.append(elem)
		text = " ".join(new)
		return text


a = Str("Привет меня зовут Николай")

print(a.replaze2("Привет меня зовут", "Пока тебя называют"))
	