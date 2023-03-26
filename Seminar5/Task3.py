# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Поиск простого числа

import math


def simple(num: int) -> bool:     # первый вариант (быстро считает)
    if num in [1, 2, 3]:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


print(simple(49))


# def is_simple(num: int) -> bool:        # второй вариант (очень долго считает, не стоит включать!)
#     for i in range(2, num):
#         if not num % i:
#             return False
#     return True

# print(is_simple(int(input("Введите число: "))))
