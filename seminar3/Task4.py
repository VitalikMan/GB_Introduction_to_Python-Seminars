# Дана упорядоченная последовательность an чисел от 1 до N.
# Из копии данной последовательности bn удалили одно число, а оставшиеся перемешали.
# Найти удаленное число.

import random

n = int(input("Введите длину последовательности: "))

numbers = []

for i in range(n + 1):
    numbers.append(i)
print(numbers)

set1 = set(numbers)
print(set1)

numbers.pop(int(input("Введите какой элемент удалить: ")))

random.shuffle(numbers)
print(numbers)

set2 = set(numbers)
print(set2)

print(set1.difference(set2))


# # Вариант 2:

# numb = []
# for i in range(n + 1):
#     i = random.randint(0, 100)
#     numb.append(i)

# print(numb)

# numb2 = numb.copy()

# numb.pop(int(input("Введите какой элемент удалить: ")))
# print(numb)

# for item in numb2:
#     if item not in numb:
#         print(item)

# random.shuffle(numb)
# print(numb)
