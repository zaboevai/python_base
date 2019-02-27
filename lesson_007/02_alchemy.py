# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self):
        self.name = 'Water'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            substance = Storm()
        elif isinstance(other, Fire):
            substance = Steam()
        elif isinstance(other, Earth):
            substance = Dirt()
        elif isinstance(other, Iron):
            substance = Rust()
        else:
            substance = None

        return substance


class Fire:

    def __init__(self):
        self.name = 'Fire'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            substance = Lightning()
        elif isinstance(other, Water):
            substance = Steam()
        elif isinstance(other, Earth):
            substance = Lava()
        elif isinstance(other, Iron):
            substance = Ingot()
        else:
            substance = None

        return substance


class Air:

    def __init__(self):
        self.name = 'Air'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            substance = Dust()
        elif isinstance(other, Fire):
            substance = Lightning()
        elif isinstance(other, Earth):
            substance = Dust()
        else:
            substance = None

        return substance


class Earth:
    def __init__(self):
        self.name = 'Earth'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            substance = Dirt()
        elif isinstance(other, Fire):
            substance = Lava()
        elif isinstance(other, Air):
            substance = Dust()
        elif other == Iron():
            substance = Ore()
        else:
            substance = None

        return substance


class Steam:
    name = 'Steam'

    def __str__(self):
        return self.name


class Dirt:
    name = 'Dirt'

    def __str__(self):
        return self.name


class Storm:
    name = 'Storm'

    def __str__(self):
        return self.name


class Lightning:
    name = 'Lightning'

    def __str__(self):
        return self.name


class Dust:
    name = 'Dust'

    def __str__(self):
        return self.name


class Lava:
    name = 'Lava'

    def __str__(self):
        return self.name


class Iron:
    def __init__(self):
        self.name = 'Iron'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            substance = Rust()
        elif isinstance(other, Fire):
            substance = Ingot()
        elif isinstance(other, Earth):
            substance = Ore()
        else:
            substance = None

        return substance


class Rust:
    """ржавчина"""
    name = 'Rust'

    def __str__(self):
        return self.name


class Ingot:
    """слиток"""
    name = 'Ingot'

    def __str__(self):
        return self.name


class Ore:
    """руда"""
    name = 'Ore'

    def __str__(self):
        return self.name


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())

print('=====')
print(Fire(), '+', Dust(), '=', Fire() + Dust())
print(Earth(), '+', Fire(), '=', Earth() + Fire())

print('=====')
print(Iron(), '+', Fire(), '=', Iron() + Fire())
print(Iron(), '+', Water(), '=', Iron() + Water())
print(Iron(), '+', Earth(), '=', Iron() + Earth())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

# Зачет!