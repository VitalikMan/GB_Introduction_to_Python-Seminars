# Дан список чисел. Определите, сколько в нем встречается различных чисел.

import random


numb_list = [random.randint(0, 20) for _ in range(40)]

print(numb_list)
print(type(numb_list))

numb_set = set(numb_list)
print(numb_set)
print(len(numb_set))

# print(len(set(numb_list)))        # решение в одну строку
