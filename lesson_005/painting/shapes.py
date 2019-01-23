# -*- coding: utf-8 -*-

import simple_draw as sd


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


if __name__ == '__main__':
    # point = sd.get_point(400, 400)
    # draw_triangle(start_point=point, angle=20, length=100)
    #
    point = sd.get_point(100, 400)
    draw_quadrate(start_point=point, angle=20, length=100)
    #
    # point = sd.get_point(400, 100)
    # draw_pentagon(start_point=point, angle=20, length=100)
    #
    # point = sd.get_point(100, 100)
    # draw_hexagon(start_point=point, angle=20, length=100)
    point_list = (sd.get_point(100, 100),
                  sd.get_point(200, 100),
                  sd.get_point(200, 150),
                  sd.get_point(100, 150),
                  )

    sd.polygon(point_list=point_list, color=sd.COLOR_DARK_ORANGE, width=0)
    sd.pause()
