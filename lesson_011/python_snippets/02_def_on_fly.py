# -*- coding: utf-8 -*-


# Еще функции можно определять "на лету"
from pprint import pprint


def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        raise Exception('Я могу сделать умножители только на 2 или 3!')

    return multiplier


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_2 = get_multiplier_v1(2)
by_3 = get_multiplier_v1(3)
result = map(by_2, my_numbers)
print(list(result))
result = map(by_3, my_numbers)
print(list(result))
# get_multiplier_v1 - функция высшего порядка, она возвращает функции


# Но зачем ограничивать только двойкой и тройкой?
def get_multiplier_v2(n):

    def multiplier(x):
        return x * n

    return multiplier


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_5 = get_multiplier_v2(5)
print(by_5(x=42))

result = map(by_5, my_numbers)
print(list(result))

by_100 = get_multiplier_v2(100)
result = map(by_100, my_numbers)
print(list(result))


# Обратите внимание что параметр n для  внутренней функции multiplier
# задается вовне самой функции.
# Это так называемое "замыкание" - обьект функции хранит у себя все
# _необходимые_ему_ переменные в области видидимости, точнее ссылки на них.
def matrix(some_list):

    def multiply_column(x):
        res = []
        for element in some_list:
            res.append(element * x)
        return res

    return multiply_column


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
matrix_on_my_numbers = matrix(my_numbers)

they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
result = map(matrix_on_my_numbers, they_numbers)
pprint(list(result))

my_numbers.extend([10, 20, 30])
result = map(matrix_on_my_numbers, they_numbers)
pprint(list(result))

# Старайтесь как можно меньше использовать изменяемые обьекты внутри функций-на-лету,
# как и глобальные переменные - это приводит к неожиданным последствиям :(
# Замыкать обьекты, созданные в области видимости окружающей функции можно.

###
# Иногда нам нужны простые одноразовые функции, для которых def слишком жирно.
# Для этого есть lambda
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(lambda x: x + 10, my_numbers)
print(list(result))

my_func = lambda x: x + 10
print(my_func(x=42))
print(type(my_func))

# Лямбда форма может принимать как несколько параметров, так и не одного
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
result = map(lambda x, y: x + y, my_numbers, they_numbers)
print(list(result))

# Лямбда форма функции имеет ограниченное применение:
#  - Она создается в процессе выполнения кода (а не при компиляции) и может просадить быстродействие
#  - Она плохо сериализуется - могут быть проблемы в крупных фреймворках
#  - Не пытайтесь записать в лямбду сложное выражение: если там более 3-5 операторов - пора сделать def


###
# Еще один способ сделать функции на лету - создание обьекта, который можно вызывать
class Multiplier:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        # если есть такой метод у класса - то его обьект можно "вызывать" как функцию
        return x * self.n


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_100500 = Multiplier(n=100500)
result = by_100500(x=42)
print(result)

result = map(by_100500, my_numbers)
print(list(result))
