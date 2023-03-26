# Задача по Фибоначчи
# Вывести все числа по Фибоначчи.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 и т.д.

# def fib(num):
#     if num == 1 or num == 2:
#         return 1
#     return fib(num - 1) + fib(num - 2)

# print(fib(10))


def summa(a: int, b: int) -> int:   # стрелка означает то, что функция будет возвращать
    return a + b


print(summa(5, 6))
# print(summa("5", "6"))    # в этом случае будет проблема в выводе и решении
