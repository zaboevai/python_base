# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger
from pprint import pprint

from my_burger import take_bun, take_chop, take_cucumber, take_tomato, take_mayonnaise, take_ketchup, take_chease


def cook_burger():

    print('\nРецепт двойного чизбургера: \n')

    take_bun()
    take_chop()
    take_chease()
    take_chop()
    take_chease()
    take_cucumber()
    take_tomato()
    take_mayonnaise()
    take_ketchup()
    take_bun()


def cook_my_burger():

    print('\nРецепт любимого бургера: \n ')
    take_bun()
    take_mayonnaise()
    take_chop()
    take_chease()
    take_cucumber()
    take_tomato()
    take_ketchup()
    take_bun()


cook_burger()
cook_my_burger()
