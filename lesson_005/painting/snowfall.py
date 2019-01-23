#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 800)

# высота с которой будут падать снежинки

# кол-во снежинок
snowflakes_count = 20

snowflake_size = {'min': 5, 'max': 20}
snowflakes = {}




def draw_snowflake():
    y = sd.resolution[1] + 50
    for snowflake_num, snowflake_parameter in snowflakes.items():

        start_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
        sd.snowflake(center=start_point,
                     length=snowflake_parameter['length'],
                     color=sd.background_color,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])

        snowflake_parameter['x'] += sd.random_number(0, 2)
        snowflake_parameter['y'] -= snowflake_size['max'] + 1 - snowflake_parameter['length']

        next_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
        sd.snowflake(center=next_point,
                     length=snowflake_parameter['length'],
                     color=sd.COLOR_WHITE,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])

        if snowflake_parameter['y'] < 400 and snowflake_parameter['x'] <= 500\
           or snowflake_parameter['y'] < 50 and snowflake_parameter['x'] > 500:

            snowflake_parameter['y'] = y
            snowflake_parameter['length'] = sd.random_number(snowflake_size['min'], snowflake_size['max'])
            snowflake_parameter['x'] = sd.random_number(0, sd.resolution[0])


if __name__ == '__main__':


    while True:

        sd.start_drawing()
        draw_snowflake()
        sd.finish_drawing()

        sd.sleep(0.1)

        if sd.user_want_exit():
            break
