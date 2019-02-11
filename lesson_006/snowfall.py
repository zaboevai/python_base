# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
snowflake_size = {'min': 5, 'max': 20}

_snowflakes = {}
_down_snowflakes = []


def create_snowflakes(snowflakes_count=1):
    new_snowflakes = {}
    y = 700
    len_dict = 0

    for key, value in _snowflakes.items():
        new_snowflakes[len_dict] = value
        len_dict += 1

    for i in range(snowflakes_count):
        new_snowflakes[len_dict + i] = {'length': sd.random_number(snowflake_size['min'], snowflake_size['max']),
                                        'x': sd.random_number(0, sd.resolution[0]),
                                        'y': y,
                                        'factor_a': sd.random_number(1, 10)/10,
                                        'factor_b': sd.random_number(1, 10)/10,
                                        'factor_c': sd.random_number(1, 120)
                                        }

    _snowflakes.update(new_snowflakes)
    _down_snowflakes.clear()


def remove_snowflakes(num_snowflake):
    _new_snowflakes = {k: v for k, v in _snowflakes.items() if k not in num_snowflake}
    _snowflakes.clear()
    _snowflakes.update(_new_snowflakes)


def draw_snowflakes(color=sd.COLOR_WHITE):
    for snowflake_num, snowflake_parameter in _snowflakes.items():
        start_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
        sd.snowflake(center=start_point,
                     length=snowflake_parameter['length'],
                     color=color,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])


def move_snowflakes():
    for snowflake_num, snowflake_parameter in _snowflakes.items():
        snowflake_parameter['x'] += sd.random_number(0, 2)
        snowflake_parameter['y'] -= snowflake_size['max'] + 1 - snowflake_parameter['length']


def get_down_snowflakes():
    for snowflake_num, snowflake_parameter in _snowflakes.items():
        if snowflake_parameter['y'] < 0:
            _down_snowflakes.append(snowflake_num)

    return _down_snowflakes
