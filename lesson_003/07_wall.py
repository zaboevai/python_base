# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# sd.resolution = (900, 900)
sd.background_color = sd.COLOR_DARK_ORANGE

x = 100
y = 50

pos_x = 0
pos_y = 0
# start_x = 50
# end_x = start_x + x
#
# start_y = 50
# end_y = start_y + y


step = x

brick_x_count = sd.resolution[0] // x
brick_y_count = sd.resolution[1] // y

sd.resolution = (800, 800)

start_x = pos_x
start_y = pos_y
end_y = start_y + y
end_x = start_x + x

for brick_y in range(brick_y_count):

    if brick_y % 2 == 1:
        x_count += 1
    else:
        x_count = brick_x_count #sd.resolution[0] // x

    for brick_x in range(x_count):

        # print(brick_y, brick_y % 2)
        if brick_y % 2 == 1:
            print(brick_x, x_count)
            if brick_x == 0: # or brick_x == x_count:
                start_position = sd.get_point(start_x, start_y)
                end_position = sd.get_point(end_x-50, end_y)
            elif brick_x == x_count-1:
                start_position = sd.get_point(start_x-50, start_y)
                end_position = sd.get_point(end_x-100, end_y)
            else:
                start_position = sd.get_point(start_x-50, start_y)
                end_position = sd.get_point(end_x-50, end_y)
        else:
            start_position = sd.get_point(start_x, start_y)
            end_position = sd.get_point(end_x, end_y)


        sd.rectangle(left_bottom=start_position, right_top=end_position, color=sd.COLOR_BLACK, width=1)

        # двигаем кирпич по x
        start_x += x
        end_x += x

        sd.sleep(0.03)

    # возвращаем по х в исходное положение
    start_x = pos_x
    end_x = x

    # двигаем кирпич по y
    start_y = end_y
    end_y += y

sd.pause()
