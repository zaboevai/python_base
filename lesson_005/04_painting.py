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

# import painting.snowfall as pt_snowfall
# import painting.wall as pt_wall

sd.resolution = (1200, 800)

# pt_wall.draw_wall(100, 100)

# pt_tree.x = 300
# pt_tree.y = 30
#
# root_point = sd.get_point(300, 30)
# pt_tree.draw_simetric_branches(point=root_point, length=50)
#
# pt_rainbow.draw_line_rainbow(0, 1200)

while True:
    sd.start_drawing()

    pt_rainbow.draw_rainbow(x=100, y=-50, radius=700, width=6)

    pt_snowfall.y = 700
    pt_snowfall.draw_snowflake()

    sd.finish_drawing()
    sd.sleep(0.1)
#

#
    pt_smile.draw_smile(100, 100)
#
# pt_snowfall.sleep = sd.sleep(0.1)
#
