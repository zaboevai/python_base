#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

calc_dist = lambda x1,y1,x2,y2: round(((x1-x2)**2+(y1-y2)**2)**0.5, 2)

# TODO Вычисления правильнные, но в данной работе пока нельзя использовать
# TODO циклы, на первых этапах нужно все делать вручную
for key in sites:
    temp_dict = {}
    for key2 in sites:
        if key != key2:
            x1, y1, x2, y2 = sites[key][0], sites[key][1], sites[key2][0], sites[key2][1]
            temp_dict[key2] = calc_dist(x1, y1, x2, y2)

             'Paris': {'Moscow': round(((sites['Paris'][0] - sites['Moscow'][0]) ** 2
                                        + (sites['Paris'][1] - sites['Moscow'][1]) ** 2) ** 0.5
                                       , 2),

                       'London': round(((sites['Paris'][0] - sites['London'][0]) ** 2
                                        + (sites['Paris'][1] - sites['London'][1]) ** 2) ** 0.5
                                       , 2),
                       }
             }

print(distances)



