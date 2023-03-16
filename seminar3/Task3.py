# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

import random

num = int(input("Введите размер массива: "))
numbers = []
count = 0

for i in range(num):
    i = random.randint(1, 100)
    numbers.append(i)

print(numbers)

for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        count += 1

print(count)
