# -*- coding: utf-8 -*-

import simple_draw as sd

vector_end_point_list = []

def draw_figure(start_point, side_count, angle, length):
    vector = start_point
    angle_step = 360 / side_count
    step = angle_step
    vector_end_point_list.clear()
    for side in range(side_count):
        if side == 0:
            vector = sd.get_vector(start_point=vector, angle=angle, length=length+3)
        elif side == side_count-1:
            sd.line(vector.end_point, start_point)
            break
        else:
            vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length)
            step += angle_step
        vector_end_point_list.append(vector.end_point)
        vector.draw()
    return vector_end_point_list

def draw_triangle(start_point, angle=0, length=100):
    side = 3
    return draw_figure(start_point=start_point, side_count=side, angle=angle, length=length)


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
    point = sd.get_point(400, 400)
    vector_end_point_list = draw_triangle(start_point=point, angle=0, length=100)
    print(vector_end_point_list[0].x, vector_end_point_list[0].y)
    print(vector_end_point_list[1].x, vector_end_point_list[1].y)
    print(vector_end_point_list[2].x, vector_end_point_list[2].y)
    # point = sd.get_point(100, 400)
    # draw_quadrate(start_point=point, angle=20, length=100)
    #
    # point = sd.get_point(400, 100)
    # draw_pentagon(start_point=point, angle=20, length=100)
    #
    # point = sd.get_point(100, 100)
    # draw_hexagon(start_point=point, angle=20, length=100)
