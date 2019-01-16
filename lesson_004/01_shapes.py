# -*- coding: utf-8 -*-

import simple_draw as sd

# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны

# Нарисовать все фигуры
# Выделить общую часть алгоритма рисования в отдельную функцию
# Придумать, как устранить разрыв в начальной точке фигуры

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def draw_figure(start_point, side_count, angle, length):
    vector = start_point
    angle_step = 360 / side_count
    step = angle_step
    for side in range(side_count):
        if side == 0:
            vector = sd.get_vector(start_point=vector, angle=angle, length=length+3)
        elif side == side_count-1:
            sd.line(vector.end_point, start_point)
            break
        else:
            vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length)
            step += angle_step
        vector.draw()


def draw_triangle(start_point, angle=0, length=100):
    side = 3
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length)


def draw_quadrate(start_point, angle=0, length=100):
    side = 4
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length)


def draw_pentagon(start_point, angle=0, length=100):
    side = 5
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length)


def draw_hexagon(start_point, angle=0, length=100):
    side = 6
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length)


point = sd.get_point(400, 400)
draw_triangle(start_point=point, angle=20, length=100)

point = sd.get_point(100, 400)
draw_quadrate(start_point=point, angle=20, length=100)

point = sd.get_point(400, 100)
draw_pentagon(start_point=point, angle=20, length=100)

point = sd.get_point(100, 100)
draw_hexagon(start_point=point, angle=20, length=100)

sd.pause()
