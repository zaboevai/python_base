# -*- coding: utf-8 -*-

import simple_draw as sd
from painting import wall as pt_wall

building_start_point = sd.get_point(x=300, y=10)
building_size = (480, 240)
pt_wall.wall_size = building_size

roof_point_list = [sd.get_point
                   (building_start_point.x+1,
                    building_start_point.y+1 + building_size[1]),

                   sd.get_point
                   (building_start_point.x+1 + building_size[0] // 2,
                    building_start_point.y+1 + building_size[1] + building_size[1]),

                   sd.get_point
                   (building_start_point.x+1 + building_size[0],
                    building_start_point.y+1 + building_size[1]),
                   ]


def draw_ground():
    # рисуем землю
    sd.rectangle(sd.get_point(0, 0), sd.get_point(sd.resolution[0], 40), sd.COLOR_WHITE)
    sd.rectangle(sd.get_point(0, 0), sd.get_point(sd.resolution[0], 30), sd.COLOR_DARK_ORANGE)


def draw_house():

    # рисуем стену здания
    pt_wall.draw_wall(pos_x=building_start_point.x, pos_y=building_start_point.y)

    # рисуем крышу здания
    sd.polygon(point_list=roof_point_list, color=sd.COLOR_DARK_GREEN, width=0)
    sd.polygon(point_list=roof_point_list, color=sd.COLOR_BLACK, width=1)

    # рисуем окно на крыше
    sd.circle(sd.get_point(building_start_point.x+1 + building_size[0]//2,
                           building_start_point.y + 1 + building_size[1] + building_size[1] // 2),
              30, color=sd.COLOR_DARK_YELLOW, width=0)

    sd.circle(sd.get_point(building_start_point.x+1 + building_size[0]//2,
                           building_start_point.y + 1 + building_size[1] + building_size[1] // 2),
              30, color=sd.COLOR_BLACK, width=1)

    # рисуем окно здания
    x_step = building_size[0] // 4
    y_step = building_size[1] // 5

    sd.rectangle(sd.get_point(building_start_point.x+1 + x_step, building_start_point.y+1 + y_step),
                 sd.get_point(building_start_point.x+1 + building_size[0] - x_step,
                              building_start_point.y+1 + building_size[1] - y_step),
                 color=sd.COLOR_DARK_YELLOW, width=0)

    sd.rectangle(sd.get_point(building_start_point.x+1 + x_step, building_start_point.y+1 + y_step),
                 sd.get_point(building_start_point.x+1 + building_size[0] - x_step,
                              building_start_point.y+1 + building_size[1] - y_step),
                 color=sd.COLOR_BLACK, width=3)

    return roof_point_list