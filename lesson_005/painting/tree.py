# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

x = 1000
y = 30
root_point = sd.get_point(x, y)
angle = 90

def draw_simetric_branches(point = root_point, angle = angle, length=100):
    if length < 10:
        return

    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    vector.draw()

    next_point = vector.end_point
    delta = 30
    length *= 0.75

    next_angle = angle - delta
    draw_branches(next_point, next_angle, length)

    next_angle = angle + delta
    draw_branches(next_point, next_angle, length)


def draw_branches(point, angle, length=100):
    if length < 10:
        return

    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    vector.draw()

    next_point = vector.end_point

    delta = 30
    delta_deviation = delta * 0.4
    delta += sd.random_number(-delta_deviation, delta_deviation)

    length = length * 0.75
    length_deviation = round(length * 0.2)
    length += sd.random_number(0, length_deviation)

    next_angle = round(angle + delta)
    draw_branches(next_point, next_angle, length)

    next_angle = round(angle - delta)
    draw_branches(next_point, next_angle, length)


if __name__ == '__main__':
    root_point = sd.get_point(1000, 30)
    draw_simetric_branches(point=root_point, angle=90, length=100)

    root_point = sd.get_point(500, 30)
    draw_branches(point=root_point, angle=90, length=100)
