# 5 - Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи](https://clck.ru/sH87m)

m = int(input('введите сколько числе фибоначчи вывести'))

def fun_feb(n):
    num1 = 1
    num2 = 1
    rez = [0,num1,num2,]
    i = 0
    while i < n - 2:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        i = i + 1
        rez.append(num3)
    return rez

def fun_feb2(n):
    num1 = 1
    num2 = -1
    rez = [num1,num2,]
    i = 0
    while i < -n - 2:
        num3 = (num1 + num2*(-1))
        num1 = num2
        num2 = num3
        i = i + 1
        rez.append(num3)
    return rez[::-1]

if m > 0:
    print(fun_feb(m))
else:
    print(fun_feb2(m)+fun_feb(-m))








