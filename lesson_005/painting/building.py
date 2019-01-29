# -*- coding: utf-8 -*-

import simple_draw as sd


wall_size = (400, 400)
# sd.resolution = wall_size
# sd.background_color = sd.COLOR_DARK_ORANGE

# размер кирпича
brick_sizer_x = 40
brick_sizer_y = 20

half_brick = brick_sizer_x // 2

def draw_wall(pos_x=0, pos_y=0):

    brick_x_count = wall_size[0] // brick_sizer_x  # sd.resolution[0] // x
    brick_y_count = wall_size[1] // brick_sizer_y  # sd.resolution[1] // y

    start_x = pos_x
    start_y = pos_y

    for brick_y in range(brick_y_count):

        end_x = start_x + brick_sizer_x
        end_y = start_y + brick_sizer_y

        # определяем кол-во кирпичей в ряду
        if brick_y % 2 == 1:
            x_count += 1
        else:
            x_count = brick_x_count

        for brick_x in range(x_count):

            if brick_y % 2 == 1:
                if brick_x == 0:
                    start_position = sd.get_point(start_x, start_y)
                    end_position = sd.get_point(end_x-half_brick, end_y)
                elif brick_x == x_count-1:
                    start_position = sd.get_point(start_x-half_brick, start_y)
                    end_position = sd.get_point(end_x - brick_sizer_x, end_y)
                else:
                    start_position = sd.get_point(start_x-half_brick, start_y)
                    end_position = sd.get_point(end_x-half_brick, end_y)
            else:
                start_position = sd.get_point(start_x, start_y)
                end_position = sd.get_point(end_x, end_y)

            sd.rectangle(left_bottom=start_position, right_top=end_position, color=sd.COLOR_DARK_ORANGE, width=0)
            sd.rectangle(left_bottom=start_position, right_top=end_position, color=sd.COLOR_BLACK, width=1)

            # двигаем кирпич по x
            start_x += brick_sizer_x
            end_x += brick_sizer_x

            # sd.sleep(0.03)

        # возвращаем по х в исходное положение
        start_x = pos_x
        end_x = brick_sizer_x

        # двигаем кирпич по y
        start_y = end_y
        end_y += brick_sizer_y

    # sd.pause()


# draw_wall(100, 100)