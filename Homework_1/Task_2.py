# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = int(input("Введите пожалуйста трёх значное число:"))
if number > 999 or number < 100:
    print("Это не трёхзначное число, попробуйте заново")
else:
    n1 = number // 100
    n2 = number % 100 // 10
    n3 = number % 10
    print(n1 + n2 + n3) 