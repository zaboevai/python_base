# -*- coding: utf-8 -*-

# Функциональный стиль в программировании


def get_russian_names():
    return ['Ваня', 'Коля', 'Маша', ]


# Имя функции указывает на обьект функции. Обычная переменная.
print(type(get_russian_names))
# можно узнать название функции
print(get_russian_names.__name__)


# Можно переприсваивать
my_func = get_russian_names
print(my_func())
# название останется как при определении
print(my_func.__name__)


# Можно работать как с обычными обьектами
def get_british_names():
    return ['Oliver', 'Jack', 'Harry', ]


name_getters = [get_russian_names, get_british_names]
for name_getter in name_getters:
    print(name_getter())


# И передавать как параметры в другие функции
def print_names(message, name_getter):
    print(message, name_getter())


print_names('Русские имена', get_russian_names)

names = {'Русские имена': get_russian_names, 'Английские имена': get_british_names}

for message, name_getter in names.items():
    print_names(message, name_getter)

# print_names является функцией высшего порядка - она принимает на вход другие функции


# Конечно же функци, _принимающие_ параметры, тоже могут быть переданы через переменную/параметр
# (помните, что переменные суть ярлыки-ссылки на обьекты?)
def adder(*args):
    res = 0
    for number in args:
        res += number
    return res


def multiplier(*args):
    res = 1
    for number in args:
        res *= number
    return res


def process_numbers(numbers, handler):
    result = handler(*numbers)
    print(f'Получилось {result}')


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
process_numbers(numbers=my_numbers, handler=adder)
process_numbers(numbers=my_numbers, handler=multiplier)


# Есть две встроенные функции высшего порядка - map и filter
# Они принимают на вход функцию и произвольную последовательность


# map применяет функцию к каждому элементу последовательности и формирует список результатов
def mul_by_2(x):
    return x * 2


def mul_by_3(x):
    return x * 3


result = map(mul_by_2, my_numbers)
print(result)
print(list(result))
result = map(mul_by_3, my_numbers)
print(list(result))


# filter вычисляет функцию для каждого элемента и добавляет элемент в список результатов,
# если только функция вернула True
def is_odd(x):
    return x % 2


result = filter(is_odd, my_numbers)
print(result)
print(list(result))


# можно совместить - получаются вложенные последовательности обработки
result = map(mul_by_3, filter(is_odd, my_numbers))
print(list(result))

result = sum(map(mul_by_3, filter(is_odd, my_numbers)))
print(result)

# map и filter принимают любые обьекты, по которым можно пройти циклом:
# списки, тьюплы/кортежи, множества, словари
