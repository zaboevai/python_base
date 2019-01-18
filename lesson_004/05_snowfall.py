# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 200

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

for i in range(N):
    snowflakes[i] = {'length': sd.random_number(5, 20),
                     'x': sd.random_number(0, 1100),
                     'y': y
                     }

while True:

    sd.start_drawing()

    for num, parametr in snowflakes.items():

        point = sd.get_point(parametr['x'], parametr['y'])
        sd.snowflake(center=point, length=parametr['length'], color=sd.background_color)

        parametr['x'] += sd.random_number(-5, 5) + parametr['length']
        parametr['y'] -= sd.random_number(5, 20) - parametr['length']

        next_point = sd.get_point(parametr['x'], parametr['y'])
        sd.snowflake(center=next_point, length=parametr['length'], color=sd.COLOR_WHITE)

        if parametr['y'] < 50:
            parametr['y'] = y
            parametr['length'] = sd.random_number(5, 10)
            parametr['x'] = sd.random_number(0, 1100)

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


