# -*- coding: utf-8 -*-

# Создать пакет, в котором собрать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Каждую функцию разместить в своем модуле. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.


import simple_draw as sd
from painting import smile as pt_smile, \
                     snowfall as pt_snowfall, \
                     wall as pt_wall, \
                     tree as pt_tree, \
                     rainbow as pt_rainbow

sd.resolution = (1200, 800)

pt_wall.wall_size = (200, 200)
pt_snowfall.snowflakes_count = 100

# заполняем словарь с параметрами снежинок
for i in range(pt_snowfall.snowflakes_count):
    y = sd.resolution[1] + 50
    pt_snowfall.snowflakes[i] = \
        {'length': sd.random_number(pt_snowfall.snowflake_size['min'], pt_snowfall.snowflake_size['max']),
         'x': sd.random_number(0, sd.resolution[0]),
         'y': y,
         'factor_a': sd.random_number(1, 10) / 10,
         'factor_b': sd.random_number(1, 10) / 10,
         'factor_c': sd.random_number(1, 120)
         }

tick = 0
root_point = sd.get_point(1000, 30)

while True:

    tick += 1
    sd.start_drawing()

    pt_snowfall.draw_snowflake()

    pt_rainbow.draw_rainbow(x=100, y=-50, radius=700, width=6, game_tick=tick)

    pt_wall.draw_wall(pos_x=400, pos_y=30)

    pt_tree.root_color = sd.background_color
    pt_tree.draw_simetric_branches(point=root_point, angle=90, length=70)

    pt_tree.root_color = sd.COLOR_DARK_ORANGE
    pt_tree.draw_simetric_branches(point=root_point, angle=90, length=70)

    pt_smile.draw_smile(500, 130, tick)

    sd.sleep(0.07)
    sd.finish_drawing()

    if tick >= 60:
            tick = 0

    if sd.user_want_exit():
        break
