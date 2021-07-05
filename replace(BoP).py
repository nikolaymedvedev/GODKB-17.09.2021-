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


if __name__ == "__main__":
	a = Str("Привет меня зовут Николай")
	
	print(a.replaze("Привет меня зовут", "Пока тебя называют"))
	