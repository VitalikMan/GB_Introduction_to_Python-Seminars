# Даны два массива чисел. Требуется вывести те элементы первого массива(в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива

import random

print("Необходимо ввести -> 1) Длина списка 1; 2) Длина списка 2; 3) Число min; 4) Число max")
my_vars = tuple(map(int, input("Введите числа через пробел: ").split()))
my_list1 = [random.randint(my_vars[2], my_vars[3]) for i in range(my_vars[0])]
my_list2 = [random.randint(my_vars[2], my_vars[3]) for i in range(my_vars[1])]

# Вариант 1:
my_list3 = [item for item in my_list1 if item not in my_list2]

print(my_list1)
print(my_list2)
print(my_list3)

# Вариант 2:
for item in my_list1:
    if item not in my_list2:
        print(item, end=" ")
