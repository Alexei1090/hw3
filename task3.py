# 3 - Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564

import math

num_list = [1.1, 1.2, 3.1, 5.567, 10.03]

def fun_r(lis):
    new_num_list = []
    for i in lis:
        new_num_list.append((i - int(i))*1000)
        #new_num_list.append(int((i%1)*1000))
    return max(new_num_list) - min(new_num_list)

print(fun_r(num_list))