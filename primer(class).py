class A:

	def __init__(self, name, age):
		self.name = name 
		self.age = age
		print("Работает матод __init__")

	def __str__(self):
		return "Это тестовый класс"

	def __len__(self):
		return (len(self.name) + len(str(self.age)))
	
	def __add__(self, other):
		return A(self.name + other.name, self.age + other.age)
	
	def __call__(self, age: int, name: str ="Nikolay"):
      		return f"Собака {self.name} с возрастом {age}"
	
	def __lt__(self, other):
      		if self.age < other:
         		return True
      		return False

   	def __gt__(self, other):
      		if self.age > other:
         		return True
      		return False

   	def __eq__(self, other):
      		if self.age == other:
         		return True
      		return False

   	def __getattribute__(self, name):
      		if name == "name":
         		return "Не трогай это имя!"
      		return object.__getattribute__(self, name)

   	def __getattr__(self, name):
      		return False

   	def __delattr__(self, name):
        	print(f"Удаляем аттрибут {name}")
      		object.__delattr__(self, name)

   	def __del__(self):
      		print(f"Удаляем обьект класса {__class__.__name__}")

	@classmethod
	def nameclass(cls):
		return cls.__name__

	def setattr(self, name, age):
		self.__name = name
		self.__age = age

	def getname(self):
		return self.__name

	def getage(self):
		return self.__age 


class B(A):

	def __init__(self, x, y, name, age):
		self.x = x
		self.y = y
		super().__init__(name, age)
		print("Работает субметод __init__")


kolya = A("Коля", 25)
Evgen = A("Евген", 24)

kolya.setattr("Коля", 25)

print(kolya)

print(len(kolya))

c = kolya + Evgen
print(c.age)
print(c.name)

Vova = B("Это:X", "Это:y", "Вова", 37)
print(Vova.name)



"""_______________________________Metaclass_____________________________"""

class typikal(object):
	def __str__(self):
		return "Это обычный класс"

def init(self, name, age):
	self.name = name
	self.age = age

def get_name(self):
	return f"Ваше имя {self.name}"

def get_age(self):
	return  f"Ваш возраст {self.age}"

nasled = (typikal, )
atr = {"__init__":init,"name":"", "age":"", "get_name":get_name, "get_age":get_age}

p1 = type("Metaclass", nasled, atr)
Man = p1("Nik", 25)

for i, j in {"Vova":25, "Nik":25, "Evgen":24}.items():
	Name = p1(i, j)
	print(Name.name)
	print(Name.age)

