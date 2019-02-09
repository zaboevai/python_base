#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 800)

# высота с которой будут падать снежинки

# кол-во снежинок
snowflakes_count = 1

tick = 0

snowflake_size = {'min': 5, 'max': 15}

snowflakes = {}
down_snowflakes = {}

ground = 50
# speed = 0

surface_list = (sd.get_point(101, 211), sd.get_point(301, 411), sd.get_point(501, 211))
down_num = 0


def draw_snowflake(surface_point_list, falling=False):
    global snowflakes, down_num

    y = sd.resolution[1] + 50

    if not falling:
        speed = sd.random_number(0, 3)
    else:
        speed = 0

    if falling and snowflakes_count > len(snowflakes):
        # заполняем словарь с параметрами снежинок
        for i in range(snowflakes_count):
            # y = sd.resolution[1] + 50
            snowflakes[i] = \
                {'length': sd.random_number(snowflake_size['min'], snowflake_size['max']),
                 'x': sd.random_number(-300, sd.resolution[0]),
                 'y': y,
                 'factor_a': sd.random_number(1, 10) / 10,
                 'factor_b': sd.random_number(1, 10) / 10,
                 'factor_c': sd.random_number(1, 120)
                 }

    for snowflake_num, snowflake_parameter in snowflakes.items():

        start_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
        sd.snowflake(center=start_point,
                     length=snowflake_parameter['length'],
                     color=sd.background_color,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])

        snowflake_parameter['x'] += sd.random_number(-1, 5)

        snowflake_parameter['y'] -= snowflake_size['max'] + 1 - snowflake_parameter['length'] + speed

        next_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
        sd.snowflake(center=next_point,
                     length=snowflake_parameter['length'],
                     color=sd.COLOR_WHITE,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])

        # снежинки падают на крышу и на землю
        # TODO подумать как можно это оптимизировать, сделать более читаемым
        if (
            (
             (snowflake_parameter['x'] - surface_point_list[0].x + 10
              > snowflake_parameter['y'] - surface_point_list[0].y
                and surface_point_list[0].x <= snowflake_parameter['x'] <= surface_point_list[1].x
              ) or
             (surface_point_list[2].x - snowflake_parameter['x'] + 10
              > snowflake_parameter['y'] - surface_point_list[0].y
                and surface_point_list[1].x <= snowflake_parameter['x'] <= surface_point_list[2].x
             )
            ) or snowflake_parameter['y'] < ground
           ):

            down_snowflakes[down_num] = {'length': snowflake_parameter['length'],
                                         'x': snowflake_parameter['x'],
                                         'y': snowflake_parameter['y'],
                                         'factor_a': snowflake_parameter['factor_a'],
                                         'factor_b': snowflake_parameter['factor_b'],
                                         'factor_c': snowflake_parameter['factor_c']
                                         }
            down_num += len(down_snowflakes) + 1

            # print(len(down_snowflakes))
            # print(len(snowflakes))
            if falling:
                snowflake_parameter['y'] = y
                snowflake_parameter['length'] = sd.random_number(snowflake_size['min'], snowflake_size['max'])
                snowflake_parameter['x'] = sd.random_number(-300, sd.resolution[0])




            # print('down_snowflakes', len(down_snowflakes), down_snowflakes)
            # print('snowflakes', len(snowflakes), snowflakes)
    # удаление снежинок из словаря
    # snowflakes = {k: v for k, v in snowflakes.items() if k not in down_snowflakes}

    for num, parameter in down_snowflakes.items():
        # print('snowflakes', len(down_snowflakes), down_snowflakes)
        sd.snowflake(center=sd.get_point(parameter['x'], parameter['y']),
                     length=parameter['length'],
                     color=sd.COLOR_WHITE,
                     factor_a=parameter['factor_a'],
                     factor_b=parameter['factor_b'],
                     factor_c=parameter['factor_c'])

        # if not falling:
        #     sd.snowflake(center=sd.get_point(parameter['x'], parameter['y']),
        #                  length=parameter['length'],
        #                  color=sd.background_color,
        #                  factor_a=parameter['factor_a'],
        #                  factor_b=parameter['factor_b'],
        #                  factor_c=parameter['factor_c'])
    if not falling:
        down_snowflakes.clear()


if __name__ == '__main__':

    snowflakes_count = 100
    falling = True

    while True:

        tick += 1

        sd.start_drawing()

        sd.line(surface_list[0], surface_list[1])
        sd.line(surface_list[1], surface_list[2])

        draw_snowflake(surface_list, falling)

        if tick % 100 == 0:
            sd.clear_screen()

        if tick == 100:
            falling = False

        sd.finish_drawing()

        # удаление снежинок из словаря
        # snowflakes = {k: v for k, v in snowflakes.items() if k not in down_snowflakes}
        sd.sleep(0.05)
        if sd.user_want_exit():
            break
