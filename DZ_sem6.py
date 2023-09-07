# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def a_progression (a1, d, n):
#     if n == 1:
#         return [a1]
#     else:
#         return a_progression (a1, d, n-1) + [a1 + (n-1)*d]
    
# a1 = int(input("Введите первый элемент прогрессии "))
# d = int(input("Введите разность "))
# n = int(input("Введите количество элементов прогрессии "))
    
# print(a_progression (a1, d, n))



# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

# def find_index(sp, min_value, max_value,index=0,result=[]):
#     if index == len(sp):
#         return result
#     elif sp[index] >= min_value and sp[index] <= max_value:
#         result.append(index)
#     return find_index(sp, min_value, max_value, index+1, result)

# import random
# n = int(input("Введите количество значений списка "))
# sp = list(random.randint(1, 1000) for i in range(n))
# min_value = int(input("Введите минимальное значение диапозона "))   
# max_value = int(input("Введите максимальное значение диапозона ")) 
# print(sp)
# print(find_index(sp, min_value, max_value))  

 