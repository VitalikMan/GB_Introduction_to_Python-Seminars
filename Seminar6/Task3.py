# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

from random import randint

# print("Введите длину списка (>3) и диапазон")
# my_vars = list(map(int, input("Введите числа через пробел: ").split()))
# my_list1 = [randint(my_vars[1], my_vars[2]) for _ in range(my_vars[0])]
# print(my_list1)

# dict = {}

# for i in my_list1:
#     dict[i] = dict.get(i, 0) + 1

# s = 0
# for key, value in dict.items():
#     s += value // 2

# print(f'Таких пар в списке => {s}')


# Вариант от Стоуна
my_list2 = [randint(0, 10) for _ in range(10)]
print(my_list2)

count = 0
for item in range(11):
    count += my_list2.count(item)//2

print(f'Таких пар в списке => {count}')
