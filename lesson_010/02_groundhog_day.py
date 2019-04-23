# -*- coding: utf-8 -*-
import random
# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.

ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    my_exceptions = (IamGodError('IamGod - Карма не растет'),
                     DrunkError('Drunk - Карма не растет'),
                     CarCrashError('CarCrash - Карма не растет'),
                     GluttonyError('Gluttony - Карма не растет') ,
                     DepressionError('Depression - Карма не растет'),
                     SuicideError('Suicide - Карма не растет'),)

    if random.randint(1, 13) == 13:
        raise random.choice(my_exceptions)
    return random.randint(1, 7)


with open('02_error.log', mode='w') as file:
    while True:
        try:
            carma += one_day()
            if carma >= ENLIGHTENMENT_CARMA_LEVEL:
                print(carma)
                break
        except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
            error = f'Ошибка: {exc.__class__.__name__} {exc.args}'
            print(error)
            file.write(error)
            file.write('\n')

# https://goo.gl/JnsDqu

# Зачет!
