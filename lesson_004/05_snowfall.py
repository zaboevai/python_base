# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

sd.resolution = (1200, 800)

y = 700
x = 0
snowflakes = {}
snowflake_size = {'min': 5, 'max': 20}

for i in range(N):
    snowflakes[i] = {'length': sd.random_number(snowflake_size['min'], snowflake_size['max']),
                     'x': sd.random_number(0, sd.resolution[0]),
                     'y': y,
                     'a': sd.random_number(1, 10)/10,
                     'b': sd.random_number(1, 10)/10,
                     'c': sd.random_number(1, 120)
                     }

while True:

    sd.start_drawing()

    for num, parameter in snowflakes.items():

        point = sd.get_point(parameter['x'], parameter['y'])
        sd.snowflake(center=point,
                     length=parameter['length'],
                     color=sd.background_color,
                     factor_a=parameter['a'],
                     factor_b=parameter['b'],
                     factor_c=parameter['c'])

        parameter['x'] += sd.random_number(0, 2)


        parameter['y'] -= snowflake_size['max'] + 1 - parameter['length']

        next_point = sd.get_point(parameter['x'], parameter['y'])
        sd.snowflake(center=next_point,
                     length=parameter['length'],
                     color=sd.COLOR_WHITE,
                     factor_a=parameter['a'],
                     factor_b=parameter['b'],
                     factor_c=parameter['c'])

        if parameter['y'] < 50:
            parameter['y'] = y
            parameter['length'] = sd.random_number(snowflake_size['min'], snowflake_size['max'])
            parameter['x'] = sd.random_number(0, sd.resolution[0])

    sd.finish_drawing()

    sd.sleep(0.1)

    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


