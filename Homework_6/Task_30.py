# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии:  an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first = int(input('Введите первый элемент прогрессии: '))
step = int(input('Введите шаг прогрессии: '))
size = int(input('Введите количество элементов прогрессии: '))
n = 1
list = []
for i in range(size) :
    list.append(first + (n - 1) * step)
    n += 1
print(list)