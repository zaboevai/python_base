# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

x = 1000
y = 30
root_point = sd.get_point(x, y)
root_angle = 90
root_color = (38, 34, 26)


def draw_simetric_branches(point, angle, length=100, set_day=None):

    if length < 10:
        return

    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=5)
    vector.draw(root_color)

    next_point = vector.end_point
    if length < 30:
        if set_day == 'morning':
            sd.circle(next_point, 7, sd.COLOR_DARK_GREEN, width=0)
            sd.circle(next_point, 4, sd.COLOR_GREEN, width=0)
        elif set_day == 'morning':
            sd.circle(next_point, 7, sd.COLOR_DARK_GREEN, width=0)
            sd.circle(next_point, 2, sd.COLOR_WHITE, width=0)
        elif set_day == 'evening':
            sd.circle(next_point, 7, sd.COLOR_DARK_GREEN, width=0)
            sd.circle(next_point, 4, sd.COLOR_GREEN, width=0)
        else:
            sd.circle(next_point, 7, sd.COLOR_WHITE, width=0)

    delta = 30
    length *= 0.75

    next_angle = angle - delta
    draw_simetric_branches(next_point, next_angle, length, set_day)

    next_angle = angle + delta
    draw_simetric_branches(next_point, next_angle, length, set_day)


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
    draw_simetric_branches(point=root_point, angle=root_angle, length=70, set_day=True)

    root_point = sd.get_point(500, 30)
    draw_branches(point=root_point, angle=root_angle, length=50)

    sd.pause()

