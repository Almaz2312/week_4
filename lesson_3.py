"""
-- args. -- kwargs
"""

# def many_args(*abc, **name):     # одна * это аргс, две * это кваргс
#     if name:
#         print(name)   # принтует кваргс, т.к у name две *
#     if abc:
#         print(abc)    # принтует аргс, т.к у abc одна *
#     else:
#         print("args not found")
#
#
# many_args(1, 3, [12, 7], l=1, name='Almaz')   # выведет сначала кваргс, потом аргс изза if else condition


# def test(*xs):
#     if xs:
#         for i in xs:
#             for y in i:
#                 return y
#     else:
#         return "args не было передано"
#
#
# namus = [1, 2, 3, 4, 5]
# print(test(namus))


# def get_age(*args, **kwargs):
#     gte_30 = []
#     lte_30 = []
#     if kwargs:
#         for i in kwargs.values():     # Значения кваргов(словарей) итерирует
#             if i >= 30:
#                 gte_30.append(i)
#             else:
#                 lte_30.append(i)
#
#     gte_30 = list(set(gte_30))
#     lte_30 = list(set(lte_30))
#     return f'gte_30 : {gte_30}. lte_30 : {lte_30}'
#
#
# print(get_age(nazi=30, nodira=18, samat=29))


# def func(*args):
#     print(args)
#
#
# func(1, 2, 3, 'abc', 'ase', [1, 2, 3], {1: 'b', 2: 'r'}, ('q', 'b'))

# def greet(*args):
#     # print('Hello', name)    # Нельзя через +, т.к в том случае должно быть string. Можно через "," или f                            строку
#     for names in args:
#         print('Hello ' + names + '!')
#
# greet('Ermek', 'Bael')


# def greet(*args):
#     for name in args:
#         print('Hello ' + name + '!', end=' ')   # Добавили end, чтобы в одну строку поздоровался
#
# greet('Bael', 'Nodira')


# def func(child1, child3, child2):
#     print(child2)
#
#
# func(child2='Asan', child1='Beka', child3='Arslan')     # В принт указали ключи, поэтому сработало

# def func(child1=None, child2=None, child3=None):
#     print(child1)
#     print(child3)
#     print(child2)
#
#
# func(child1='Asan')


# def my_func(*args, **kwargs):
#     print(kwargs)
#
# my_func(child2='Asan', child1='Asan')

# def my_func(*args, **kwargs):
#     print(args, kwargs)
#
#
# my_func(1,2,3,4, child2='Asan')

# fruits = ['apple', 'pineapple', 'banana']
# def test(*args):
#     print(args)
#
#
# test(*fruits)       # * Вытаскивает значения из списка. Обернёт их в кортеж без квадратных скобок


d1 = {'name' : 'Asan', 'age': 12}
def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(**d1)      # Без ** будет аргс, в({}). С одной * будет аргс без {}. С ** будет кваргс