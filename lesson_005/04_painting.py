#!/usr/bin/env python
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

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.


import simple_draw as sd
from painting import smile as pt_smile, \
                     snowfall as pt_snowfall, \
                     building as pt_building, \
                     tree as pt_tree, \
                     rainbow as pt_rainbow, \
                     sun as pt_sun


sd.resolution = (1200, 800)

global background_color
background_color = sd.COLOR_BLACK
sd.background_color = background_color

pt_snowfall.snowflakes_count = 100
snow_falling = True
snowflakes = {}
snowflakes_remove = {}

part_of_day = ''

tick = 0

sun_start_point = (-100, -100)

pt_building.building_start_point = sd.get_point(x=300, y=10)
pt_building.building_size = (480, 240)

pt_building.roof_point_list = [sd.get_point
                               (pt_building.building_start_point.x+1,
                                pt_building.building_start_point.y+1 + pt_building.building_size[1]),

                               sd.get_point
                               (pt_building.building_start_point.x+1 + pt_building.building_size[0] // 2,
                                pt_building.building_start_point.y+1 + pt_building.building_size[1] + pt_building.building_size[1]),

                               sd.get_point
                               (pt_building.building_start_point.x+1 + pt_building.building_size[0],
                                pt_building.building_start_point.y+1 + pt_building.building_size[1]),
                               ]

root_point = ((sd.get_point(950, 20),  pt_building.building_size [1] / 2 - sd.random_number(10, 30)),
              (sd.get_point(200, 10),  pt_building.building_size [1] / 2 - sd.random_number(10, 30)))


def change_part_day():
    global part_of_day, background_color

    if tick in (0, 200):
        background_color = (109, 147, 176)
        part_of_day = 'morning'
        snow_falling = True
        sun_color = sd.COLOR_ORANGE

    elif tick in (201, 400):
        background_color = (109, 147, 171)
        part_of_day = 'afternoon'

    elif tick in (401, 600):
        background_color = sd.COLOR_DARK_BLUE
        part_of_day = 'evening'
    elif tick in (601, 800):
        background_color = sd.COLOR_BLACK
        part_of_day = 'night'

    if sd.background_color != background_color:
        sd.background_color = background_color
        pt_snowfall.background_color = background_color
        sd.clear_screen()


step: int = 0
size_step = 0

sun_point = sd.get_point(sun_start_point[0], sun_start_point[1])
sun_next_point = sun_point

while True:

    if tick >= 800:
        tick = 0

    sd.start_drawing()

    change_part_day()

    # print(part_of_day)

    # параметры смены дня
    if part_of_day == 'morning':
        snow_falling = True
        sun_color = sd.COLOR_ORANGE

    elif part_of_day == 'afternoon':

        sun_color = sd.COLOR_YELLOW
        if tick < 380:
            snow_falling = False
        else:
            snow_falling = True
    elif part_of_day == 'evening':
        sun_next_point = sd.get_point(-500, -500)

    elif part_of_day == 'night':
        sun_next_point = sd.get_point(-500, -500)

    if part_of_day == 'morning' and tick % 5 == 0:
        size_step += 4

    # отображение солнца
    sun_next_point = pt_sun.draw_sun(start_point=sun_next_point, radius=250, length=400, rays_count=36,
                                     move_step=5, size_step=size_step, color=sun_color)

    # отображение радуги
    if part_of_day == 'afternoon':
        pt_rainbow.draw_rainbow(x=500, y=-100, radius=500, width=10, game_tick=tick, )

    # отображение снегопада
    pt_snowfall.draw_snowflake(pt_building.roof_point_list, falling=snow_falling)

    # удаление снежинок из словаря
    snowflakes = {k: v for k, v in snowflakes.items() if k not in snowflakes_remove}

    # отображение земли
    pt_building.draw_ground()

    # отображение 1 дерева
    pt_tree.draw_simetric_branches(point=root_point[1][0], angle=90, length=root_point[1][1], set_day=part_of_day)

    # отображение здания
    pt_building.draw_house()

    # отображение смайлика
    pt_smile.draw_smile(pt_building.building_start_point.x + 1 + pt_building.building_size[0] // 2,
                        pt_building.building_start_point.y + 1 + pt_building.building_size[1] // 2,
                        tick)

    # отображение 2 дерева
    pt_tree.draw_simetric_branches(point=root_point[0][0], angle=90, length=root_point[0][1], set_day=part_of_day)

    sd.sleep(0.03)
    tick += 1
    sd.finish_drawing()

    if sd.user_want_exit():
        break
