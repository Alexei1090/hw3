# 4 - Напишите программу, которая будет преобразовывать десятичное 
# число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def func(int1):
    int2 = ''
    while int1 >= 1:
        int2 = int2 + (str(int1 % 2))
        int1 = int1 // 2
    return int2[::-1]


m = int(input('введите число в десятичной систете: '))
print(func(m))