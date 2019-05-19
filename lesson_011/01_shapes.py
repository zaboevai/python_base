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


def create_polygon(n):

    def polygon(start_point, angle, length):
        vector = start_point
        side_count = n
        angle_step = 360 / side_count
        step = angle_step
        for side in range(side_count):
            if side == 0:
                vector = sd.get_vector(start_point=vector, angle=angle, length=length + 3)
            elif side == side_count - 1:
                sd.line(vector.end_point, start_point)
                break
            else:
                vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length)
                step += angle_step
            vector.draw()

    return polygon


polygon = create_polygon(n=9)
polygon(start_point=sd.get_point(200, 50), angle=0, length=100)

sd.pause()

# Зачет!
