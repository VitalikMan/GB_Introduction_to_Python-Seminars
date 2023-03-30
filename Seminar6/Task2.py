# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного

import random

my_list = [random.randint(1, 100) for _ in range(10)]
print(my_list)
size = len(my_list)

count = 0
for i in range(size):
    if my_list[(i-1)] % size < my_list[i % size] > my_list[(i + 1) % size]:
        count += 1

print(f'Таких элементов в списке => {count}')
