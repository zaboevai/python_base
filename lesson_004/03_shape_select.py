# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


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

figures = {1: 'треугольник',
           2: 'квадрат',
           3: 'пятиугольник',
           4: 'шестиугольник'}

while True:

    print('Возможные фигуры:')
    for num, name in figures.items():
        print('    ', num, ':', name.lower())

    figure = input('Укажите номер фигуры: ')

    if figure.isdigit() and int(figure) in figures:
        figure = int(figure)

        print('Возможные цвета:')
        for num, name in colors.items():
            print('    ', num, ':', name[0].lower())

        color = input('Укажите номер цвета: ')

        if color.isdigit() and int(color) in colors:

            color = int(color)
            point = sd.get_point(300, 300)
            if figure == 1:
                draw_triangle(start_point=point, angle=20, length=100, color=colors[color][1])
            elif figure == 2:
                draw_quadrate(start_point=point, angle=20, length=100, color=colors[color][1])
            elif figure == 3:
                draw_pentagon(start_point=point, angle=20, length=100, color=colors[color][1])
            elif figure == 4:
                draw_hexagon(start_point=point, angle=20, length=100, color=colors[color][1])

            break
        else:
            print('\n    Ошибка!: Неверно указан номер фигуры.\n')
    else:
        print('\n    Ошибка!: Неверно указан номер фигуры.\n')

sd.pause()

# Зачет!