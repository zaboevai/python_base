# -*- coding: utf-8 -*-


# Произвольное число параметров
print(1, 2, 3, 4, 5, 56, 6,)


# Произвольное число позиционных параметров
def print_them_all_v1(*args):
    print('print_them_all_v1')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)


print_them_all_v1(2, 'привет', 5.6)

# распаковка
my_favorite_pets = ['lion', 'elephant', 'monkey', 'cat', 'horse']
print_them_all_v1(my_favorite_pets)
print_them_all_v1(*my_favorite_pets)


# Произвольное число именованных параметров
def print_them_all_v2(**kwargs):
    print('print_them_all_v2')
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v2(name='Вася', address='Moscow')

# распаковка
my_friend = {'name': 'Вася', 'address': 'Moscow', 'age': 25}
print_them_all_v2(**my_friend)


# неправильные вызовы
print_them_all_v1(name='Вася', address='Moscow')
print_them_all_v2('Вася', 'Moscow', 25)


# Комбинация
def print_them_all_v3(*args, **kwargs):
    print('print_them_all_v3')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v3('Вася', 'Moscow', 25)
print_them_all_v3(name='Вася', address='Moscow')

print_them_all_v3(1000, 'рублей', name='Вася', address='Moscow')

my_friend = {'name': 'Вася', 'address': 'Moscow'}
print_them_all_v3(1000, 'рублей', **my_friend)


# При создании функции можно указывать как обычные параметры, так и произвольные параметры
def print_them_all_v4(a, b=5, *args, **kwargs):
    print('print_them_all_v4')
    print('a и b:', a, b)
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v4(5, 6, 7, 8, cat='мяу!')
print_them_all_v4(5, b=8, cat='мяу!')
print_them_all_v4(5, cat='мяу!', address='Moscow')


