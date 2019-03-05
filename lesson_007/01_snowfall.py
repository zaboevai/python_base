# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

sd.resolution = (1200, 800)

class Snowflake:
    y = sd.resolution[1]
    snowflake_size = {'min': 5, 'max': 20}

    def __init__(self):
        self.parameter = self.__create_snowflake__()

    def draw(self, color=sd.COLOR_WHITE):
        start_point = sd.get_point(x=self.parameter['x'], y=self.parameter['y'])
        sd.snowflake(center=start_point,
                     length=self.parameter['length'],
                     color=color,
                     factor_a=self.parameter['factor_a'],
                     factor_b=self.parameter['factor_b'],
                     factor_c=self.parameter['factor_c'])

    def clear(self, color=sd.background_color):
        self.draw(color)

    def move(self):
        self.parameter['x'] += sd.random_number(0, 2)
        self.parameter['y'] -= self.snowflake_size['max'] + 1 - self.parameter['length']

    def __create_snowflake__(self):
        return {
            'length': sd.random_number(self.snowflake_size['min'], self.snowflake_size['max']),
            'x': sd.random_number(0, sd.resolution[0]),
            'y': sd.randint(self.y-100, self.y+100),
            'factor_a': sd.random_number(1, 10) / 10,
            'factor_b': sd.random_number(1, 10) / 10,
            'factor_c': sd.random_number(1, 120)
        }


snowflakes = {}
snowflakes_count = 20

for i in range(snowflakes_count):
    flake = Snowflake()
    snowflakes[i] = flake

while True:
    sd.start_drawing()

    for num, snowflake in snowflakes.items():
        snowflake.clear()
        snowflake.move()
        snowflake.draw()

        if snowflake.parameter['y'] < 0:
            snowflakes[num] = Snowflake()

    sd.sleep(0.05)
    sd.finish_drawing()

    if sd.user_want_exit():
        break
