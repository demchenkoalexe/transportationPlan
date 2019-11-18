import math
import copy
import sys
import numpy as np

#Жлобский метод
def hMethod(a, b, c):
	# Если задача несбалансированная, то вводим фиктивного участника сети
	if sum(a) < sum(b):
		dif = sum(b) - sum(a)
		a.append(dif)
		# Добавим тарифы для фиктивного поставщика
		c.append([0] * len(b))
	elif sum(b) < sum(a):
		dif = sum(a) - sum(b)
		b.append(dif)
		# Добавим тарифы для фиктивного потребителя
		for i in c:
			i.append(0)		

	route = [[None for j in range(len(b))] for i in range(len(a))]

	route = np.array(route)
	while(len(np.where(route == None)[1]) > 0):
		# Ищём самый низкий тариф
		iMax = 0
		jMax = 0 
		min = sys.maxsize
		for i in range(len(a)):
			for j in range(len(b)):
				if (route[i][j] == None and min > c[i][j]):
					min = c[i][j]
					iMax = i
					jMax = j

		if (b[jMax] > a[iMax]):
			route[iMax][jMax] = a[iMax]
			dif = a[iMax]
		else:
			route[iMax][jMax] = b[jMax]
			dif = b[jMax]
		a[iMax] -= dif
		b[jMax] -= dif
	
	return route

def print_plan(route, fict = 0, length = 0):
	print("Допустимый план:")
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
			c = [[int(j) for j in file.readline().split()] for i in range(len(a))]	# Тарифы
			c1 = copy.deepcopy(c)
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

		for i in range(lenA):
			row = []
			for j in range(lenB):
				row.append(int(input("Введите тариф поставок из пункта A" + str(i + 1) + " в пункт B" + str(j + 1) + ": ")))
			c.append(row)

	route = hMethod(a, b, c1)
	
	print_plan(route)	

if __name__ == '__main__':
    main()