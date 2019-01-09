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
    start_x = pos_x
    start_y = pos_y
    for brick_x in range(brick_x_count):

        start_position = sd.get_point(start_x, start_y)
        end_position = sd.get_point(end_x, end_y)
        sd.rectangle(left_bottom=start_position, right_top=end_position, color=sd.COLOR_BLACK, width=1)
        start_x += 100 - 1
        # start_y += 50
        end_x += 100 - 1
        # print(brick_y, brick_y % 2)
        if brick_y % 2 == 1:
            step = 50
        else:
            step = 0

    start_x = pos_x
    start_y = pos_y
    end_x = pos_x + x
    end_y += y

sd.pause()
