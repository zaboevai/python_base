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

class NotExpectedPolygon(Exception):
    pass


def get_polygon(n):
    # TODO Необходимо реализовать замыкание, как это сделать показано в
    # TODO "11.10 Практика - функциональный стиль. Часть 1"
    if n == 3:
        # TODO Необходимо использовать универсальную функцию, а не функции
        # TODO основанные на ней.
        # TODO Импортировать функции из урока 4 не нужно
        return shapes.draw_triangle
    elif n == 4:
        return shapes.draw_quadrate
    elif n == 5:
        return shapes.draw_pentagon
    elif n == 6:
        return shapes.draw_hexagon
    else:
        # TODO В данном случае не нужно ограничивать пользователя в выборе
        # TODO фигуры, по этому исключения это лишнее
        raise NotExpectedPolygon(
            f'Ошибка в <{get_polygon.__name__}>: разрешено кол-во сторон для ввода n = (3, 4, 5, 6), введено = <{n}>')


try:
    draw_figure = get_polygon(n=5)
    draw_figure(start_point=sd.get_point(150, 150), angle=13, length=200)
except NotExpectedPolygon as exc:
    print(exc)

sd.pause()
