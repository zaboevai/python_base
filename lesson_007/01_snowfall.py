# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    snowflake_size = {'min': 5, 'max': 20}
    snowflakes = {}
    down_snowflakes = []
    y = 600

    def __init__(self, count=1):
        self.create_snowflakes(count)

    def create_snowflakes(self, snowflakes_count=1):

        for i in range(snowflakes_count):
            self.snowflakes[i] = {
                'length': sd.random_number(self.snowflake_size['min'], self.snowflake_size['max']),
                'x': sd.random_number(0, sd.resolution[0]),
                'y': self.y,
                'factor_a': sd.random_number(1, 10) / 10,
                'factor_b': sd.random_number(1, 10) / 10,
                'factor_c': sd.random_number(1, 120)
                }

    def clear_previous_picture(self, color=sd.background_color):
        self.draw(color)

    def move(self):
        for snowflake_num, snowflake_parameter in self.snowflakes.items():
            snowflake_parameter['x'] += sd.random_number(0, 2)
            snowflake_parameter['y'] -= self.snowflake_size['max'] + 1 - snowflake_parameter['length']

    def draw(self, color=sd.COLOR_WHITE):
        for snowflake_num, snowflake_parameter in self.snowflakes.items():
            start_point = sd.get_point(x=snowflake_parameter['x'], y=snowflake_parameter['y'])
            sd.snowflake(center=start_point,
                         length=snowflake_parameter['length'],
                         color=color,
                         factor_a=snowflake_parameter['factor_a'],
                         factor_b=snowflake_parameter['factor_b'],
                         factor_c=snowflake_parameter['factor_c'])

    def can_fall(self):
        for snowflake_num, snowflake_parameter in self.snowflakes.items():
            if snowflake_parameter['y'] <= 0:
                self.down_snowflakes.append(snowflake_num)
        return self.down_snowflakes

    def append_snowflakes(self, fallen_flakes):
        for num in fallen_flakes:
            self.snowflakes[num] = {
                                    'length': sd.random_number(self.snowflake_size['min'], self.snowflake_size['max']),
                                    'x': sd.random_number(0, sd.resolution[0]),
                                    'y': self.y,
                                    'factor_a': sd.random_number(1, 10) / 10,
                                    'factor_b': sd.random_number(1, 10) / 10,
                                    'factor_c': sd.random_number(1, 120)
                                    }
        self.down_snowflakes.clear()


flake = Snowflake(count=10)

while True:
    sd.start_drawing()

    flake.clear_previous_picture()
    flake.move()
    flake.draw()

    falling_snowflakes = flake.can_fall()

    if falling_snowflakes:
        flake.append_snowflakes(falling_snowflakes)

    sd.sleep(0.05)
    sd.finish_drawing()

    if sd.user_want_exit():
        break
