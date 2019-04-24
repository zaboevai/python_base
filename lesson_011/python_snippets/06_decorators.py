# -*- coding: utf-8 -*-

# Декораторы - это просто.

# Предположим есть функция с тяжеловесными вычислениями:
# найти количество цифр в произведении 5000-х степеней чисел


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


# и нам надо засечь время выполнения функции
import time
started_at = time.time()
result = digits(3141, 5926, 2718, 2818)
print(result)
ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'Функция работала {elapsed} секунд(ы)')


# Вообще, учет времени выполнения - достаточно типичная ситуация, и хочется сделать функцию-помощника
#
# Напишем функцию высшего порядка, на вход которой передается другая функция и параметры с которыми надо её вызвать
def time_track(func, *args, **kwargs):
    started_at = time.time()

    result = func(*args, **kwargs)

    ended_at = time.time()
    elapsed = round(ended_at - started_at, 4)
    print(f'Функция работала {elapsed} секунд(ы)')
    return result


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


result = time_track(digits, 3141, 5926, 2718, 2818)
print(result)


# Но можно пойти еще глубже - пусть time_track еще и возвращает функцию.
# Функцию, которая заместит оригинальную func.
def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


timed_digits = time_track(digits)
result = timed_digits(3141, 5926, 2718, 2818)
print(result)

# а можно вообще сделать так
digits = time_track(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)
# и теперь digits - почти та же функция, но не та. Она отдекорирована функцией time_track
# за счет *args, **kwargs внутренняя surrogate принимает все параметры
# и тут же передает их в декорируемую функцию


# в пайтон есть синтаксический сахар для декораторов. выглядит он так
@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))

# Это аналог digits = time_track(digits)

# Минусы декораторов:
#  - затруднена отладка
#  - нужно делать определенные действия, что бы сохранить аттрибуты декорерируемой функции (см functools.wraps)
