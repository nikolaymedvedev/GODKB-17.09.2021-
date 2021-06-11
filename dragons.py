class Dragon:
	def __init__(self, name):
			self.name = name
			self.healf = 100

	def is_alive(self):
			return self.healf > 0

	def get_damage(self, damage):
			self.healf -= damage
			if self.healf < 0:
				self.healf = 0

	def talk(self):
			print(self.name, ":Ударь меня, мое здоровье: ", self.healf)

	def enemy_screm(self):
		print("Враг", self.name, "побежден")

def main():
	dragon_list = [Dragon("Smog"), Dragon("Govard"), Dragon("Mity")]
	finish = False
	while not finish:
		dragon = dragon_list[0]
		dragon.talk()
		damage = int(input())
		dragon.get_damage(damage) 
		if not dragon.is_alive(): #Удаляем первого врага pop[0]
			dragon_list.pop(0) 
			dragon.enemy_screm()
		if not dragon_list: #Если нет списка врагов тогда закончим
			finish = True
	print("Вы победили всех!")
		
main()

