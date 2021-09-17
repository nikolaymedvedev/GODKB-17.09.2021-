"""________Бинарный_поиск________"""

def asd(spis, item):      # O(log n)
	low = 0
	hid = len(spis) - 1
	while low <= hid:
		mid = (low + hid) // 2
		mid_znachenie = spis[mid]
		if item == mid_znachenie:
			return mid
		if item < mid_znachenie:
			hid = mid - 1
		if item > mid_znachenie:
			low = mid + 1
	return None

"""____________Сортировка_выбором__________"""

def minimum(spisok):
	min_item = spisok[0]
	min_item_index = 0
	for i in range(1, len(spisok)):
		if spisok[i] < min_item:
			min_item = spisok[i]
			min_item_index = i
	return min_item_index

def sortet(spisok):
	new_spisok = []
	for i in range(len(spisok)):
		new_spisok.append(spisok.pop(minimum(spisok)))
	return new_spisok


"""_______________Рекурсия_________________"""

def fact(n):                            #1)Факториал
	if n == 1:
		return n
	else:
		return n * fact(n-1)

def fibb(a):                            #2)Фиббоначчи
	if a < 2:
		return n
	else:
		return fibb(a-1) + fibb(a-2)

def find_max(spis):                     #3)Поиск максимального элемента списка
	if len(spis) == 2:
		if spis[0] > spis[1]:
			return spis[0]
		else:
			return spis[1]
	else:
		max_event = find_max(spis[1:])
		if spis[0] > max_event:
			return spis[0]
		else:
			return max_event

a = {"a":12, "b":{"baba":13, "ded":14}, "c":{"caca":22, "cara":55}, "g":{"gard":222, "gara":554}}
def asd(dic, key):                     #4) Вложенные списки(хеш таблицы)
    if key in dic:
        return dic[key]
    else:
        for k, v in dic.items():
            if type(v) == dict:
                recurt = asd(v, key)
                if recurt != None:
                    return recurt


"""_________Быстрая_сортировка____________"""

def fast_sorted(spisok):   # O(n*log n)-среднее(лучшее) время, O(n^2)-худшее время выполнения.
	if len(spisok) < 2:
		return spisok
	else:
		oporn_event = spisok[0]
		low = [i for i in spisok[1:] if i <= oporn_event]
		more = [i for i in spisok[1:] if i > oporn_event]
		result = fast_sorted(low) + [oporn_event] + fast_sorted(more)
		return result

"""_________Поиск_в_ширину(Графы)__________"""

a = {
    'Aruba_floor1':["Odkp1", "Odkp2", "Odkp3", "Old2", "Old1", "Aruba_floor4", "picheblok", "kdl2", "kdl1"],
    'Aruba_floor4':["mikrotik", "telemed_floor4"],
    'mikrotik':["Белтелеком"],
    'telemed_floor4':["telemed_floor7"],
    'telemed_floor7':["telemed_floor4"],
    'Odkp1':["Aruba_floor1"],
    'Odkp2':["Kassa_aruba", "Aruba_floor1"],
    'Odkp3':["Aruba_floor1"],
    'Kassa_aruba':["Odkp2"],
    'Old2':["Aruba_floor1"],
    'Old1':["Old3", "Asu", "Aruba_floor1"],
    'Old3':["Old_HPE", "Teh", "Old1"],
    "Old_HPE":["Old3"],
    'Asu':["Old1"],
    'Teh':["Old3"],
    'kdl1':["Aruba_floor1"],
    'kdl2':["Aruba_floor1"],
    'picheblok':["Aruba_floor1"]
    }
    
def func(name):
    return name == "Белтелеком"

def find_hid(name):
    main_spis = []
    chek_spik = []
    main_spis += a[name]
    while len(main_spis) != 0:
        event = main_spis.pop(0)
        if event not in chek_spik:
            if func(event) == True:
                return "Нашли!"
            else:
                chek_spik.append(event)
                main_spis += a[event]
    return None

"""_____________Алгоритм_Дейкстры(Взвешанные_напраленные_графы)_______________"""

graf = {"start":{"A":5, "B":2}, "A":{"C":4, "D":2}, "B":{"A":8, "D":7}, "C":{"D":6, "fin":3}, "D":{"fin":1}}

costs = {"A":5, "B":2, "C":float('inf'), "D":float('inf'), "fin":float('inf')}

parents = {"A":"start", "B":"start", "C":"A", "D":None, "fin":None}

dublikate = []

def find_min_cost_event(costs):
    min_cost = float('inf')
    min_cost_event = None
    for event in costs:
        if event not in dublikate:
            if costs[event] < min_cost:
                min_cost = costs[event]
                min_cost_event = event
    return min_cost_event
    
def algoritm_deikstri():
    event = find_min_cost_event(costs)
    while event != None:
        costs_event = costs[event]
        nighbroks = graf[event]
        for i in nighbroks.keys():
            new_route = costs_event + nighbroks[i]
            if new_route < costs[i]:
                costs[i] = new_route
                parents[i] = event
        dublikate.append(event)
        event = find_min_cost_event(costs)
        return new_route

"""_______________Жадные_алгоритмы(приближенные_алгоритмы - NP_задачи)__________"""

vse_goroda = {"Гомель", "Витебск", "Гродно", "Минск", "Могилев"}
ohvat = {
		"fm1":{"Гомель", "Витебск", "Гродно"},
		"fm2":{"Гродно", "Гомель"},
		"fm3":{"Гродно", "Витебск"},
		"fm4":{"Могилев", "Гомель", "Витебск", "Гродно", "Минск"}
		}
result = set()

def greed_algoritm():
    global vse_goroda
    while len(vse_goroda) != 0:
        best_radio = None
        obchiy_ohvat = set()
        for radio, goroda in ohvat.items():
            peresechenie = goroda & vse_goroda
            if len(peresechenie) > len(obchiy_ohvat):
                best_radio = radio
                obchiy_ohvat = peresechenie
                result.add(radio)
                vse_goroda -= peresechenie
    return result


"""__________________dinamik_programming_______________"""

def dinamik_algoritm():
    for i in word_a:
        for j in word_b
            if word_a[i] == word_b[j]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                cell[i][j] = 0
    return cell[i][j]