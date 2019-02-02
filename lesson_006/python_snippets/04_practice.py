# -*- coding: utf-8 -*-


# Ним — математическая игра, в которой два игрока по очереди берут предметы,
# разложенные на несколько кучек. За один ход может быть взято любое количество предметов
# (большее нуля) из одной кучки. Выигрывает игрок, взявший последний предмет.
# В классическом варианте игры число кучек равняется трём.

# Составить модуль, реализующий функциональность игры.
# Функции управления игрой
#  разложить_камни()
#  взять_из_кучи(NN, KK)
#  положение_камней() - возвращает список [XX, YY, ZZ, ...] - текущее расположение камней
#  есть_конец_игры() - возвращает True если больше ходов сделать нельзя
#
#
# В текущем модуле (lesson_006/python_snippets/04_practice.py) реализовать логику работы с пользователем:
#  начало игры,
#  вывод расположения камней
#  ввод первым игроком хода - позицию и кол-во камней
#  вывод расположения камней
#  ввод вторым игроком хода - позицию и кол-во камней
#  вывод расположения камней

from nim_engine import put_stones, get_bunches, is_gameover, take_from_bunch
from termcolor import cprint, colored

put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color='green')
    cprint(get_bunches(), color='green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока {}'.format(user_number), color=user_color)
    pos = input(colored('Откуда берем?', color=user_color))
    qua = input(colored('Сколько берем?', color=user_color))
    step_successed = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход!', color='red')
    if is_gameover():
        break

cprint('Выйграл игрок номер {}'.format(user_number), color='red')