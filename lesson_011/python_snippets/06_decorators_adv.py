# -*- coding: utf-8 -*-
import time


# Для тех, у кого голова еще не закружилась - можно пойти еще глубже.
#
# Напишем функцию, которая принимает параметры и возвращает декоратор


def get_time_track(precision):
    def time_track(func):
        # практически тот же самый time_track, за исключением точности вывода времени
        def surrogate(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)  # отличия в этой строке
            print(f'Функция работала {elapsed} секунд(ы)')
            return result
        return surrogate
    return time_track


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


time_track_precision_6 = get_time_track(precision=6)
digits = time_track_precision_6(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)


# Синтаксический сахар нам поможет сделать все компактно
@get_time_track(precision=6)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


result = digits(3141, 5926, 2718, 2818)
print(result)


# Да, get_time_track - монстр с тремя -головами- уровнями сложности...
# Давайте разберем что происходит.
def get_time_track(precision):
    print('получили точность, с которой надо выводить результат')
    print('начинаем создавать декоратор')
    def time_track(func):
        print(f'декоратор принял на вход функцию, которую надо отдекорировать - {func}')
        print('начинает создавать функцию-обертку')
        def surrogate(*args, **kwargs):
            print('мы в функции-обертке, которая заместит реальную функиию func')
            print('засекаем время')
            started_at = time.time()
            print('запускаем реальную функцию с переданными в функию-обертку параметрами и запоминаем результат')
            result = func(*args, **kwargs)
            print('определяем затраченное время и выводим его')
            ended_at = time.time()
            print(f'вот тут-то и пригодится precision (== {precision}) - он запомнился в замыкании surrogate')
            elapsed = round(ended_at - started_at, precision)
            print(f'Функция работала {elapsed} секунд(ы)')
            print('возвращаем результат, который вернула реальная функция')
            return result
        print('декоратор создал фунцию-обертку и возвращает её')
        return surrogate
    print('декоратор создан и пора его вернуть')
    return time_track


@get_time_track(precision=6)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


result = digits(3141, 5926, 2718, 2818)
print(result)

# Писать и отлаживать декораторы с параметрами сложно. Но увлекательно.

