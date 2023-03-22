# Дополнительная задача от Стоуна (необязательная)
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырехзначных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
import random

# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
import string

# 1
size = int(input('Введите размер списка: '))
my_list = [random.randint(1000, 10000) for _ in range(size)]
print(my_list)

# 2
number = input('Введите цифру: ')

for i in range(size):
    my_list[i] = str(my_list[i])

for j in range(len(my_list)):

    if number in my_list[j]:
        my_list[j] = my_list[j].replace(number, '')

print(my_list)

# 3
for v in range(size):
    my_list[v] = int(my_list[v])

print(my_list)

my_list_1 = []
count = 0

for n in my_list:

    while n > 0:
        count += n % 10
        n = n//10
    my_list_1.append(count)
    count = 0


print(my_list_1)

# 3 от Стоуна
for i in range(len(my_list)):
    while len(my_list[i]) > 1:
        my_list[i] = str(sum(list(map(int, list(my_list[i])))))
print(my_list)
