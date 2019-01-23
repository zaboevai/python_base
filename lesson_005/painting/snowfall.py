#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 800)

# высота с которой будут падать снежинки

# кол-во снежинок
snowflakes_count = 20

snowflake_size = {'min': 5, 'max': 10}
snowflakes = {}

ground = 50

surface_list = (sd.get_point(101, 211), sd.get_point(301, 411), sd.get_point(501, 211))


def draw_snowflake(surface_point_list):

    background_color = sd.background_color
    y = sd.resolution[1] + 50

    for snowflake_num, snowflake_parameter in snowflakes.items():

        start_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
        sd.snowflake(center=start_point,
                     length=snowflake_parameter['length'],
                     color=background_color,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])

        snowflake_parameter['x'] += sd.random_number(-2, 2)
        snowflake_parameter['y'] -= snowflake_size['max'] + 1 - snowflake_parameter['length']

        next_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
        sd.snowflake(center=next_point,
                     length=snowflake_parameter['length'],
                     color=sd.COLOR_WHITE,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])

        if ((snowflake_parameter['x'] - surface_point_list[0].x + 10 > snowflake_parameter['y'] - surface_point_list[0].y and \
            surface_point_list[0].x <= snowflake_parameter['x'] <= surface_point_list[1].x) or \
            (surface_point_list[2].x - snowflake_parameter['x'] + 10 > snowflake_parameter['y'] - surface_point_list[0].y and \
            surface_point_list[1].x <= snowflake_parameter['x'] <= surface_point_list[2].x)) or \
            snowflake_parameter['y'] < 50:

            snowflake_parameter['y'] = y
            snowflake_parameter['length'] = sd.random_number(snowflake_size['min'], snowflake_size['max'])
            snowflake_parameter['x'] = sd.random_number(0, sd.resolution[0])


if __name__ == '__main__':

    # заполняем словарь с параметрами снежинок
    for i in range(snowflakes_count):
        y = sd.resolution[1] + 50
        snowflakes[i] = \
            {'length': sd.random_number(snowflake_size['min'], snowflake_size['max']),
             'x': sd.random_number(0, sd.resolution[0]),
             'y': y,
             'factor_a': sd.random_number(1, 10) / 10,
             'factor_b': sd.random_number(1, 10) / 10,
             'factor_c': sd.random_number(1, 120)
             }

    while True:

        sd.start_drawing()
        sd.line(surface_list[0], surface_list[1])
        sd.line(surface_list[1], surface_list[2])
        draw_snowflake(surface_list)
        sd.finish_drawing()

        # sd.sleep(0.1)

        if sd.user_want_exit():
            break
