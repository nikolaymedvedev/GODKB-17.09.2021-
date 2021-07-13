# Калькулятор
from  colorama  import  Fore ,  Back ,  Style 
from colorama import init
init()
print( Back.RED )
print( Fore.BLACK )
what = input("Введите действие: ")
print( Back.YELLOW )
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if what == "+":
	c = a + b
	print( Back.GREEN )
	print("Результат: " + str(c))
elif what == "-":
	c = a - b
	print( Back.GREEN )
	print("Результат: " + str(c))
elif what == "/":
	c = a / b
	print( Back.GREEN )
	print("Результат: " + str(c))
elif what == "*":
	c = a * b
	print( Back.GREEN )
	print("Результат умножения " + str(c))
else:
	print( Back.RED )
	print("Я такого не умею")
input()

