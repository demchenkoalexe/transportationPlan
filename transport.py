import math

def heuristicMethod(a, b):
	# Если задача несбалансированная, то вводим фиктивного участника сети
	if sum(a) < sum(b):
		dif = sum(b) - sum(a)
		a.append(dif)
	elif sum(b) < sum(a):
		dif = sum(a) - sum(b)
		b.append(dif)

	route = [[int(0) for j in range(len(b))] for i in range(len(a))]

	# Для a
	i = 0
	ai = a[i] 
	# Для b
	j = 0
	bj = b[j]
	# Превращаем каждое из a и b в 0, только затем перемещаемся 
	# к следующему поставщику или потребителю и так до окончания
	# транспортного маршрута. 
	while (len(a) > i or len(b) > j):
		if (ai < bj):
			route[i][j] = ai
			bj -= ai
			i += 1
			ai = a[i]
		elif (ai > bj):
			route[i][j] = bj
			ai -= bj
			j += 1
			bj = b[j]
		else:
			route[i][j] = ai
			i += 1
			if (i != len(a)):
				ai = a[i]
			j += 1
			if (j != len(b)):
				bj = b[j]
	return(route)

def print_plan(route, fict = 0, length = 0):
	print("Допустимый план:")
	# Если был добавлен фиктивный поставщик
	if (fict == 1 and length > 0):
		for i in range(length):
			for j in range(len(route[i])):
				if route[i][j] > 0:
					print("Из пункта A" + str(i + 1) + " в пункт В" + str(j + 1) + " ->", route[i][j])
		print("Из фиктивного пункта A в пункт В" + str(len(route[0])) + " ->", route[length][len(route) - 1])
	# Если был добавлен фиктивный потребитель
	elif (fict == 2 and length > 0):
		for i in range(len(route)):
			for j in range(length):
				if route[i][j] > 0:
					print("Из пункта A" + str(i + 1) + " в пункт В" + str(j + 1) + " ->", route[i][j])
		print("Из пункта A" + str(len(route)) + " в фиктивный пункт В ->", route[len(route) - 1][length])
	# Вывод сбалансированной задачи
	else:
		for i in range(len(route)):
			for j in range(len(route[i])):
				if route[i][j] > 0:
					print("Из пункта A" + str(i + 1) + " в пункт В" + str(j + 1) + " ->", route[i][j])

def main():
	fileOrNot = input("Ввод из файла? (Y/n) ")
	if (fileOrNot == 'Y' or fileOrNot == 'y' or fileOrNot == 'Д' or fileOrNot == 'д'):
		with open("exampleInput.txt") as file:
			a = [int(i) for i in file.readline().split()]	# Запасы
			lenA = len(a)
			b = [int(i) for i in file.readline().split()]	# Потребности
			lenB = len(b)
	else:
		print("Ручной ввод.")
		lenA = int(input("Введите количество поставщиков: "))
		a = []
		for i in range(lenA):
			a.append(int(input("Введите объём производства в пункте A" + str(i + 1) + ": ")))
		lenB = int(input("Введите количество потребителей: "))
		b = []
		for i in range(lenB):
			b.append(int(input("Введите объём необходимых поставок в пункт B" + str(i + 1) + ": ")))


	route = heuristicMethod(a, b)

	if (lenA < len(route)):
		print_plan(route, 1, lenA)
	elif (lenB < len(route[0])):
		print_plan(route, 2, lenB)	
	else:
		print_plan(route)	

if __name__ == '__main__':
    main()