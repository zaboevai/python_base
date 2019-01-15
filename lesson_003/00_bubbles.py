# -*- coding: utf-8 -*-
import random
import time

import simple_draw as sd

sd.resolution = (1200, 600)

def draw_circle(position , radius=50, step = 0, color=sd.COLOR_GREEN, width=2):
    # TODO Эта функция рисует круг, а не пузырек
    sd.circle(center_position=position, radius=radius+step, width=width, color=color)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
step = 0
for y in range(3):
    circle_position = sd.get_point(600, 300)
    sd.circle(center_position=circle_position, radius=100+step, width=1)
    step += 5

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

circle_position = sd.get_point(600, 300)
draw_circle(position=circle_position, radius=50, color=sd.COLOR_DARK_RED, width=10)

# Нарисовать 10 пузырьков в ряд

for x in range(100, 1001, 100):
    circle_position = sd.get_point(x, 500)
    draw_circle(position=circle_position, radius=50, color=sd.COLOR_DARK_RED)

# # Нарисовать три ряда по 10 пузырьков

for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        circle_position = sd.get_point(x, y)
        draw_circle(position=circle_position, radius=50)


# # Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    circle_position = sd.random_point()
    step = random.randint(1, 100)
    time.sleep(0.1)
    draw_circle(position=circle_position, radius=50, step=step, color=sd.random_color(), width=0)

sd.pause()


