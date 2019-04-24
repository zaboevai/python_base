# -*- coding: utf-8 -*-

# Полезные в практике батарейки пайтона

# Сортировка по ключу - в функцию сортировки списка можно передать функцию от одного параметра.
# что вернет эта функция, то и будет использоваться в качестве ключа для сортировки

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers.sort(key=lambda x: -x)
# keys = [-3, -1, -4, -1, -5, -9, -2, -6]
print(my_numbers)

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers.sort(key=lambda x: -x if x >= 5 else x)
# keys = [3, 1, 4, 1, -5, -9, 2, -6]
print(my_numbers)


# часто используется для сортировки сложных списков
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

my_pairs = list(zip(my_numbers, they_numbers))
print(my_pairs)

my_pairs = [(3, 2), (1, 7), (4, 1), (1, 8), (5, 2), (9, 8), (2, 1), (6, 8)]
print(my_pairs)
my_pairs.sort(key=lambda x: x[0])
# my_pairs.sort() делает почти то же самое - но он сравнивает туплы между собой, а мы - только первый элемент
print(my_pairs)

# а вот сортирвка по второму элементу
my_pairs.sort(key=lambda x: x[1])
print(my_pairs)


# Словарь с умолчательным значением

goods = [
    ['спички', 12],
    ['соль', 34],
    ['крупа', 56],
    ['спички', 78],
    ['соль', 90],
    ['крупа', 100],
]
good_count = {}
for name, quantity in goods:
    if name in good_count:
        good_count[name] += quantity
    else:
        good_count[name] = quantity
print(good_count)
# ... не очень - повторение, условия...

# Можно с ловлей исключений
good_count = {}
for name, quantity in goods:
    try:
        good_count[name] += quantity
    except KeyError:
        good_count[name] = quantity
print(good_count)
# ... но то же не очень красиво

# есть решение лучше! без переплаты и СМС!
from collections import defaultdict

good_count = defaultdict(lambda: 0)
for name, quantity in goods:
    good_count[name] += quantity
# во, так лучше ;)
# defaultdict определяет сам - есть ли такой ключ, если нет, то вызывает функцию, которую ему передали
#
# можно записать проще: так как int() возвращает 0, то
# good_count = defaultdict(int)


good_group = defaultdict(lambda: [])  # defaultdict(list)
for name, quantity in goods:
    good_group[name].append(quantity)
print(good_count)

# вообще библиотека collections содержит много полезного и если о ней зашла речь то вот еще полезность:
# сортированный словарь
from collections import OrderedDict

my_pets = OrderedDict()
my_pets['собака'] = 'Жучка'
my_pets['мышка'] = 'Норушка'
my_pets['кошка'] = 'Мурка'
my_pets['попугай'] = 'Кеша'
my_pets['рыбка'] = 'Геннадий'
my_pets['таракан'] = 'Виссегауд'
my_pets['кролик'] = 'Савелий'
print(my_pets)
for k, v in my_pets.items():
    print(k, v)
# обратите внимание, что ключи выдаются в том порядке, каком мы заносили значения


# Есть еще одна полезная библиотека для функционального программирвания - functools
# Расскажу о функции reduce
from functools import reduce

my_numbers = [1, 2, 3, 4, 5, 6]
print(reduce(lambda x, y: x + y, my_numbers))
# она берет первые два элемента, вычисляет функцию от них, получает результат
# этот результат вместе с третьим элементом подставляет в фкнкцию, получает результат
# этот результат вместе с 4м элементом подставляет в фкнкцию, получает результат
# и т.д.
#  1 + 2 -> 3
#  3 + 3 -> 6
#  6 + 4 -> 10
# 10 + 5 -> 15
# 15 + 6 -> 21

# а вот как можно быстро вычислить факториал числа
n = 10
print(reduce(lambda x, y: x * y, range(1, n + 1)))

# эти библиотеки содержат много других полезных функций - читайте документацию
