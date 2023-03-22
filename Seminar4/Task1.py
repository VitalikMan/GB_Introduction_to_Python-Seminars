# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется
# к символам с помощью постфикса формата _n.

import string
import random

in_str = input("Введите строку: ")

dict_1 = {}


for i in in_str:
    if i in dict_1:
        print(f"{i}_{dict_1[i]}", end=" ")
        dict_1[i] += 1
    else:
        dict_1[i] = 1
        print(i, end=" ")

# below rand string example
# print()
# # my_string = [random.choice(string.ascii_letters)] # все символы алфавита
# #print(my_string)
#
# my_string2 = ''.join(random.choice(string.ascii_letters) for _ in range (0,30))
# print(my_string2)
