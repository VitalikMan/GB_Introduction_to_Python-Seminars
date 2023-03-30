# numbers = '123456789'
# numbers = list(numbers)
# print(numbers)

# # numbers = list(map(lambda x: int(x)**2, numbers))     # объяснение функции lambda
# print(numbers)
# print((lambda x, y, z: x+y+z)(1, 2, 3))

# numbers = list(map(int, numbers))
# numbers = list(filter(lambda x: x % 2 == 0, numbers))        # объяснение функции filter
# print(numbers)

import random

# numbers = [random.randint(0, 100) for _ in range(10)]
# print(numbers)

# for i, item in enumerate(numbers, 100):
#     # print(i, item)
#     if item > 50:
#         print(i)


numbers = [random.randint(0, 100) for _ in range(10)]
letters = list('fjdslfjsdlkjf')
signs = 'jk;k'
print(numbers)
print(letters)

final = list(zip(numbers, letters, signs))

print(final)
