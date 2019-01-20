# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def draw_figure(start_point, side_count, angle, length, color):
    vector = start_point
    angle_step = 360 / side_count
    step = angle_step
    for side in range(side_count):
        if side == 0:
            vector = sd.get_vector(start_point=vector, angle=angle, length=length + 3)
        elif side == side_count - 1:
            sd.line(vector.end_point, start_point, color=color)
            break
        else:
            vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length)
            step += angle_step
        vector.draw(color=color)


def draw_triangle(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    side = 3
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


def draw_quadrate(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    side = 4
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


def draw_pentagon(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    side = 5
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


def draw_hexagon(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    side = 6
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


colors = {1: ('RED', sd.COLOR_RED),
          2: ('ORANGE', sd.COLOR_ORANGE),
          3: ('YELLOW', sd.COLOR_YELLOW),
          4: ('GREEN', sd.COLOR_GREEN),
          5: ('CYAN', sd.COLOR_CYAN),
          6: ('BLUE', sd.COLOR_BLUE),
          7: ('PURPLE', sd.COLOR_PURPLE)}

print('Возможные цвета:')
for num, name in colors.items():
    print('    ', num, ':', name[0].lower())

while True:
    color = input('Укажите номер цвета: ')
    if color.isdigit():
        color = int(color)
        if color in colors:
            point = sd.get_point(400, 400)
            draw_triangle(start_point=point, angle=20, length=100, color=colors[color][1])

            point = sd.get_point(100, 400)
            draw_quadrate(start_point=point, angle=20, length=100, color=colors[color][1])

            point = sd.get_point(400, 100)
            draw_pentagon(start_point=point, angle=20, length=100, color=colors[color][1])

            point = sd.get_point(100, 100)
            draw_hexagon(start_point=point, angle=20, length=100, color=colors[color][1])
            break
        else:
            print('Ошибка!: Неверно указан номер цвета.')
    else:
        print('Ошибка!: Указана буква.')

sd.pause()

# Зачет!