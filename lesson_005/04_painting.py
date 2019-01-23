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
                     rainbow as pt_rainbow, \
                     shapes as pt_shapes


sd.resolution = (1200, 800)

pt_snowfall.snowflakes_count = 50

# заполняем словарь с параметрами снежинок
for i in range(pt_snowfall.snowflakes_count):
    y = sd.resolution[1] + 50
    pt_snowfall.snowflakes[i] = \
        {'length': sd.random_number(pt_snowfall.snowflake_size['min'], pt_snowfall.snowflake_size['max']),
         'x': sd.random_number(-100, sd.resolution[0]-100),
         'y': y,
         'factor_a': sd.random_number(1, 10) / 10,
         'factor_b': sd.random_number(1, 10) / 10,
         'factor_c': sd.random_number(1, 120)
         }

tick = 0

root_point = sd.get_point(950, 30)

building_size = (400, 200)
building_start_point = sd.get_point(x=100, y=10)

# building_roof_point = {'point1', sd.get_point(building_start_point.x+1 + x_step, building_start_point.y+1 + y_step),
#                        'point2', sd.get_point(),
#                        'point3', sd.get_point(),
#                        }

pt_wall.wall_size = building_size

roof_point_list = (sd.get_point
                   (building_start_point.x+1,
                    building_start_point.y+1 + building_size[1]),

                   sd.get_point
                   (building_start_point.x+1 + building_size[0] // 2,
                    building_start_point.y+1 + building_size[1] + building_size[1]),

                   sd.get_point
                   (building_start_point.x+1 + building_size[0],
                    building_start_point.y+1 + building_size[1]),

                   )
background_color = sd.COLOR_BLACK
sd.background_color = background_color

set_day = False


while True:

    tick += 1
    sd.start_drawing()

    if set_day:
        background_color = sd.COLOR_CYAN
        sd.background_color = background_color
        pt_snowfall.background_color = background_color
    else:
        background_color = sd.COLOR_BLACK
        sd.background_color = background_color
        pt_snowfall.background_color = background_color

    # for i in range(30):
    #     point =  sd.random_point()
    #     sd.circle(point, 2, sd.COLOR_WHITE, 0)

    sd.rectangle(sd.get_point(0, 0), sd.get_point(sd.resolution[0], 40), sd.COLOR_DARK_ORANGE)

    pt_wall.draw_wall(pos_x=building_start_point.x, pos_y=building_start_point.y)

    sd.polygon(point_list=roof_point_list, color=sd.COLOR_DARK_GREEN, width=0)
    sd.polygon(point_list=roof_point_list, color=sd.COLOR_BLACK, width=1)

    if set_day == False:
        pt_snowfall.draw_snowflake(roof_point_list)
    else:
        pt_rainbow.draw_rainbow(x=550, y=100, radius=700, width=6, game_tick=tick)

    sd.circle(sd.get_point(building_start_point.x+1 + building_size[0]//2,
                           building_start_point.y + 1 + building_size[1] + building_size[1] // 4),
              30, color=sd.COLOR_DARK_YELLOW, width=0)

    sd.circle(sd.get_point(building_start_point.x+1 + building_size[0]//2,
                           building_start_point.y + 1 + building_size[1] + building_size[1] // 4),
              30, color=sd.COLOR_BLACK, width=1)


    x_step = building_size[0] // 4
    y_step = building_size[1] // 4

    sd.rectangle(sd.get_point(building_start_point.x+1 + x_step, building_start_point.y+1 + y_step),
                 sd.get_point(building_start_point.x+1 + building_size[0] - x_step,
                              building_start_point.y+1 + building_size[1] - y_step),
                 color=sd.COLOR_DARK_YELLOW, width=0)

    sd.rectangle(sd.get_point(building_start_point.x+1 + x_step, building_start_point.y+1 + y_step),
                 sd.get_point(building_start_point.x+1 + building_size[0] - x_step,
                              building_start_point.y+1 + building_size[1] - y_step),
                 color=sd.COLOR_BLACK, width=3)

    # pt_tree.root_color = sd.background_color
    # pt_tree.draw_simetric_branches(point=root_point, angle=90, length=100)

    pt_tree.root_color = sd.COLOR_DARK_ORANGE
    pt_tree.draw_simetric_branches(point=root_point, angle=90, length=100, set_day=set_day)

    pt_smile.draw_smile(building_start_point.x + 1 + building_size[0] // 2,
                        building_start_point.y + 1 + building_size[1] // 2,
                        tick)

    # sd.sleep(0.05)
    sd.finish_drawing()

    if tick >= 600:
        tick = 0

    # if tick >= 300:
    #     if tick == 300:
    #         sd.clear_screen()
    #     set_day = True
    # else:
    #     if tick == 0:
    #         sd.clear_screen()
    #     set_day = False

    if sd.user_want_exit():
        break
