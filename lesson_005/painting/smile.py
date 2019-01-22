# -*- coding: utf-8 -*-

import simple_draw as sd

# sd.resolution = (800, 800)
SMILE_SIZE = 40
SMILE_COLOR = sd.COLOR_YELLOW
OCULUS_COLOR = sd.COLOR_WHITE
BEARD_COLOR = sd.COLOR_BLACK

eyeball_radius = round(SMILE_SIZE * 0.3)
eye_radius = round(SMILE_SIZE * 0.1)
oculus_radius = eyeball_radius + 1

def blink_eye(left_eye_point, right_eye_point, blink_time = 0):

    if right_eye_point:
        sd.circle(center_position=right_eye_point, radius=eyeball_radius, color=SMILE_COLOR, width=0)
        sd.circle(center_position=right_eye_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)
        sd.sleep(blink_time)
        # sd.circle(center_position=right_eye_point, radius=eyeball_radius, color=OCULUS_COLOR, width=0)
        # sd.circle(center_position=right_eye_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)
        # sd.circle(center_position=right_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)



    if left_eye_point:
        sd.circle(center_position=left_eye_point, radius=eyeball_radius, color=SMILE_COLOR, width=0)
        sd.circle(center_position=left_eye_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)
        # sd.sleep(blink_time)
        # sd.circle(center_position=left_eye_point, radius=eyeball_radius, color=OCULUS_COLOR, width=0)
        # sd.circle(center_position=left_eye_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)
        # sd.circle(center_position=left_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)




def draw_smile(x, y, game_tick = 0):

    # рисуем лицо
    face_point = sd.get_point(x=x, y=y)
    sd.circle(center_position=face_point, radius=SMILE_SIZE, color=SMILE_COLOR, width=0)

    # рисуем глаза

    oculus_distance = eyeball_radius * 1.3
    right_oculus_point = sd.get_point(x=x+oculus_distance, y=y+oculus_distance)
    left_oculus_point = sd.get_point(x=x-oculus_distance, y=y+oculus_distance)

    sd.circle(center_position=right_oculus_point, radius=eyeball_radius, color=OCULUS_COLOR, width=0)
    sd.circle(center_position=left_oculus_point, radius=eyeball_radius, color=OCULUS_COLOR, width=0)


    right_eye_point = sd.get_point(x=x+oculus_distance, y=y+oculus_distance)
    left_eye_point = sd.get_point(x=x-oculus_distance, y=y+oculus_distance)

    sd.circle(center_position=right_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)
    sd.circle(center_position=left_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)


    # рисуем очки
    sd.circle(center_position=right_oculus_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)
    sd.circle(center_position=left_oculus_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)

    # рисуем душки очков
    # центральная часть
    point1 = sd.get_point(round(right_oculus_point.x - SMILE_SIZE / 4), right_oculus_point.y)
    point2 = sd.get_point(round(left_oculus_point.x + SMILE_SIZE / 4), left_oculus_point.y)
    sd.line(point1, point2, sd.COLOR_DARK_ORANGE, width=3)

    # левая часть
    point1 = sd.get_point(left_oculus_point.x-oculus_radius, left_oculus_point.y)
    point2 = sd.get_point(left_oculus_point.x-oculus_radius*2, left_oculus_point.y)
    sd.line(point1, point2, sd.COLOR_DARK_ORANGE, width=3)

    # правая часть
    point1 = sd.get_point(right_oculus_point.x+oculus_radius, right_oculus_point.y)
    point2 = sd.get_point(right_oculus_point.x+oculus_radius*2, right_oculus_point.y)
    sd.line(point1, point2, sd.COLOR_DARK_ORANGE, width=3)

    # рисуем бороду
    step = SMILE_SIZE // 10
    beard_step = 0
    beard_y_pos = y
    beard_length = (SMILE_SIZE - round(SMILE_SIZE * (3 / 7)))

    for i in range(x - SMILE_SIZE, x + SMILE_SIZE + 1, step):

        if i <= x:
            beard_step += step
        else:
            beard_step -= step

        point_start = sd.get_point(i, beard_y_pos)
        point_end = sd.get_point(i, beard_y_pos-beard_length-beard_step)
        sd.line(point_start, point_end, BEARD_COLOR, width=step)

    # рисуем улыбку
    step = SMILE_SIZE // 10
    smile_step = SMILE_SIZE // 10
    smile_y_pos = y-5
    smile_length = (SMILE_SIZE - round(SMILE_SIZE * (6 / 7)))

    for i in range(x-smile_length, x+smile_length+1, step):

        if i <= x:
            smile_step += step
        else:
            smile_step -= step

        point_start = sd.get_point(i, smile_y_pos-smile_length)
        point_end = sd.get_point(i, smile_y_pos-smile_length-smile_step)
        sd.line(point_start, point_end, sd.COLOR_RED, width=step)

    if 30 < game_tick < 35:
        blink_eye(left_eye_point, right_eye_point)



if __name__ == '__main__':
    # рисуем смайлы
    for _ in range(10):
        rnd_point = sd.random_point()
        draw_smile(rnd_point.x, rnd_point.y, SMILE_COLOR)

    sd.pause()
