"""
!!! Функции
"""

# x = 5
# print(abs(x))         # Также в скобках можно поставить цифру
# print()
# input()
# len()
# list

# s = {"k": 2}
# # p = list(s)           # Prints key of s
# # p = list(s.values())  # Prints value of s
# p = list(s.items())     # Prints key and value of s
# print(p)

# tuple()
# int()
# str()
# type()
# dir()

# map(), filter(), reduce()

# lists = [3, -5, 8, -12]

# def factorial(x):
#     fact = []
#     counter = 1
#     for i in x:
#         if i < 0:
#             i = abs(i)
#         else:
#             return abs(i)
#         for y in range(1, i + 1):
#             counter = counter * y
#         fact.append(counter)
#     return fact
# print(factorial(lists))       # Не получилось

# def fact(a):
#     if a < 0:
#         a = abs(a)
#     x = 1
#     for i in range(1, a+1):
#         x *= i
#     return x
#
#
# lists = [-3, 5, -8, 2]
# lists_new = list(map(fact, lists))
# print(lists_new)

"""
filter()
"""

# def test(number):
#     if number <= 3:
#         return number
#
# numbers = [1, 19, 13, 3]
# result = filter(test, numbers)
# print(list(result))


# polindrom = ['Anna', 'Civic', 'китнаморенеромантик', 'Almaz', 'Ulukbek']
#
# def only_polindroms(x):
#         reverse_ = x[::-1]
#         if x.lower() == reverse_.lower():
#             return x
#
#
# result = list(filter(only_polindroms, polindrom))
# print(result)

# polindrom = ['Anna', 'Civic', 'китнаморенеромантик', 'Almaz', 'Ulukbek']
#
#
# def is_polindrom(strin):
#     new_str = strin[::-1]
#     if strin.lower() == new_str.lower():
#         return strin
#
# new_polindrom = list(filter(is_polindrom, polindrom))
# print(new_polindrom)

"""
reduce function
"""
# from functools import reduce
#
# def proiz(a, b):
#     return a * b
#
#
# numbers = [4, 2, 2, 3]
# num = reduce(proiz, numbers)
# print(num)


# Задача 1

"""
Сгенерировать числа в листе от 1-100. С помощью мэп возвести их в квадрат (Новый лист). Потом через фильтр полученные значения из мэп, должны получить числа которые без остатка делятся на 3 и на 5 (должно делится на оба числа). Потом через reduce получить сумму всего полученных из 3.
"""


numbers = list(range(1, 101))
def squares(x): # Возводит в квадрат
    return x**2


new_numbers = list(map(squares, numbers))


def divide(x):  # Выбирает числа которые делятся на 3 и 5
    if x % 3 == 0 and x % 5 == 0:
        return x

result = list(filter(divide, new_numbers))
print(result)

from functools import reduce

def last(a, b):     # Делает сумму чисел
    return a + b


final = reduce(last, result)
print(final)
