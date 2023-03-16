# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

num = int(input("Введите число: "))

shift = int(input("Введите число для сдвига: "))

numbers = [_ for _ in range(num)]

print(numbers)
print(numbers[-shift:] + numbers[:-shift])

# # Вариант 2 - не доделан
# new_numbers = []
# for i in range(num):
#     new_numbers.insert(i-shift, i)

# print(new_numbers)
