class Godkb:

	def __init__(self, otdel=str, job=str) -> str:
		self.otdel = otdel
		self.job = job
		print("Работает функция init главная")
	def graf(self):
		print("Отдел", self.otdel, "занимается", self.job)

class Odkp(Godkb):

	def __init__(self, oad=100, job=20) -> str:
		self.xp = None
		print("Работает функция инит подкласса")
		super().__init__(job)
		
AD = Odkp()

print(AD.job)

