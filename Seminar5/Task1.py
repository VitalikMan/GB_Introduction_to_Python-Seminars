import random

# #1 задача в дз
# my_list = [random.randint(0, 5) for _ in range(20)]
# print(my_list)
# number = int(input("Введите искомое число: "))
# print(f"Число {number} встречается в списке {my_list.count(number)} раз")

# #2 задача в дз
# my_list = [random.randint(0, 100) for _ in range(20)]
# print(my_list)

# number = int(input("Введите искомое число: "))

# nearest_number = my_list[0]
# dist = abs(number - nearest_number)

# for num in my_list:
#     if abs(num - number) < dist:
#         dist = abs(num - number)
#         nearest_number = num

# if my_list.count(number):
#     print(f"")

# # рекурсия


def list_summa(numb: int):
    if numb == 0:
        return numb
    return numb + list_summa(numb - 1)


print(list_summa(5))
