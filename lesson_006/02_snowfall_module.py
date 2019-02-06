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
from snowfall import create_snowflakes, \
                     draw_snowflakes, \
                     move_snowflakes, \
                     remove_snowflakes, \
                     check_down_snowflakes, \
                     num_remove_snowflake

snowflakes_count = 5
create_snowflakes(snowflakes_count)

while True:

    sd.start_drawing()
    draw_snowflakes(sd.background_color)
    move_snowflakes()
    draw_snowflakes(sd.COLOR_WHITE)

    # print(len(num_remove_snowflake))
    if check_down_snowflakes():
        # print(len(num_remove_snowflake))
        remove_snowflakes(num_remove_snowflake)
        create_snowflakes(len(num_remove_snowflake))
        num_remove_snowflake = []
    sd.sleep(0.05)
    sd.finish_drawing()

    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)    #
    if sd.user_want_exit():
        break

sd.pause()
