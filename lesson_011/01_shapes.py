# -*- coding: utf-8 -*-

import simple_draw as sd
from lesson_004 import shapes


# На основе вашего кода из решения lesson_004/shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    if n == 3:
        return shapes.draw_triangle
    elif n == 4:
        return shapes.draw_quadrate
    elif n == 5:
        return shapes.draw_pentagon
    elif n == 6:
        return shapes.draw_hexagon
    else:
        return shapes.draw_hexagon


draw_triangle = get_polygon(n=4)
print(draw_triangle)
draw_triangle(start_point=sd.get_point(150, 150), angle=13, length=200)

sd.pause()
