# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.

N = int(input("Введите число до которого хотите найти степени: "))
k = 0
i  = 0
while 2 ** i < N :
    k = 2 ** i
    i += 1
    print(k)