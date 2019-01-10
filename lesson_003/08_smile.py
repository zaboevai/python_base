# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
sd.resolution = (800, 800)
smile_size = 50

def draw_smile(x, y, color):

    face_point = sd.get_point(x=x, y=y)

    sd.circle(center_position=face_point, radius=smile_size, color=color, width=0)

    oculus_radius = round(smile_size * 0.25)
    oculus_distance = oculus_radius * 1.4
    right_oculus_point = sd.get_point(x=x+oculus_distance, y=y+oculus_distance)
    left_oculus_point = sd.get_point(x=x-oculus_distance, y=y+oculus_distance)

    sd.circle(center_position=right_oculus_point, radius=oculus_radius, color=sd.COLOR_DARK_GREEN, width=0)
    sd.circle(center_position=left_oculus_point, radius=oculus_radius, color=sd.COLOR_DARK_GREEN, width=0)
    print(left_oculus_point, right_oculus_point)

    right_oculus_point.x = round(right_oculus_point.x - smile_size/6)
    left_oculus_point.x = round(left_oculus_point.x + smile_size/6)

    print(left_oculus_point, right_oculus_point)
    sd.line(left_oculus_point, right_oculus_point, sd.COLOR_BLACK, width=3)

    eye_radius = round(smile_size * 0.1)
    right_eye_point = sd.get_point(x=x+oculus_distance, y=y+oculus_distance)
    left_eye_point = sd.get_point(x=x-oculus_distance, y=y+oculus_distance)


    sd.circle(center_position=right_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)
    sd.circle(center_position=left_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)


    step = smile_size // 20
    beard_step = 0
    beard_y_pos = y - (smile_size -round(smile_size * (6/7)))
    beard_length = (smile_size -round(smile_size * (5/7)))
    print(beard_length)

    for i in range(x-smile_size, x+smile_size+1, step):

        if i <= x:
            beard_step += step
        else:
            beard_step -= step

        point_start = sd.get_point(i, beard_y_pos)
        point_end = sd.get_point(i, beard_y_pos-beard_length-beard_step)
        sd.line(point_start, point_end, sd.COLOR_BLACK, width=step)

    step = smile_size // 10
    smile_step = smile_size // 20
    smile_y_pos = y - (smile_size - round(smile_size * (6 / 7)))
    smile_length = (smile_size - round(smile_size * (5/7)))
    print(beard_length)

    for i in range(x-smile_length, x+smile_length+1, step):

        if i <= x:
            smile_step += step
        else:
            smile_step -= step

        point_start = sd.get_point(i, smile_y_pos-smile_length)
        point_end = sd.get_point(i, smile_y_pos-smile_length-smile_step)
        sd.line(point_start, point_end, sd.COLOR_RED, width=step)


for _ in range(10):
    rnd_point = sd.random_point()
    draw_smile(rnd_point.x, rnd_point.y, sd.COLOR_YELLOW)
# draw_smile(400, 400, sd.COLOR_YELLOW)

sd.pause()
