# Задача 8: Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input("Введите ширину шоколадки:"))
m = int(input("Введите длинну шоколадки:"))
k = int(input("Сколько долек вы хотите отломить? "))
if k < m*n and (k%m==0 or k%n==0):
    print("Вы можете разделить шоколадку на 2 прямоугольника")
else:
    print("Вы не можете разделить шоколадку на 2 треугольника")