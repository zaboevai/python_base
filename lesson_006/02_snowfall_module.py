# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
#    нарисовать_снежинки_цветом(color=sd.background_color)
#    сдвинуть_снежинки()
#    нарисовать_снежинки_цветом(color)
#    если есть номера_достигших_низа_экрана() то
#        удалить_снежинки(номера)
#        создать_снежинки(count)

from snowfall import create_snowflakes, \
                     draw_snowflakes, \
                     move_snowflakes, \
                     remove_snowflakes, \
                     get_down_snowflakes

snowflakes_count = 5

create_snowflakes(snowflakes_count=snowflakes_count)

while True:

    sd.start_drawing()
    draw_snowflakes(color=sd.background_color)
    move_snowflakes()
    draw_snowflakes(color=sd.COLOR_WHITE)

    down_snowflakes = get_down_snowflakes()

    if len(down_snowflakes) > 0:
        remove_snowflakes(num_snowflake=down_snowflakes)
        create_snowflakes(snowflakes_count=len(down_snowflakes))

    sd.sleep(0.05)
    sd.finish_drawing()

    if sd.user_want_exit():
        break

# Зачет!