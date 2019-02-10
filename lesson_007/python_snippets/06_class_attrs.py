# -*- coding: utf-8 -*-

# Аттрибуты могут иметь не только объекты, но и их классы

from random import randint, choice


# посчитаем леммингов
class Lemming:
    pass


total_lemmings = 0
lemming_1 = Lemming()
total_lemmings += 1
lemming_2 = Lemming()
total_lemmings += 1
lemming_3 = Lemming()
total_lemmings += 1

family = []
family_size = randint(16, 32)
while len(family) < family_size:
    new_lemming = Lemming()
    family.append(new_lemming)
    total_lemmings += 1
print(total_lemmings)


# пусть сам класс следит за количеством своих объектов
class Lemming:
    # можно определять атрибуты на уровне класса, тогда они "привязаны" к классу
    total = 0

    def __init__(self):
        # обращаться - через именование класса
        Lemming.total += 1


family = []
family_size = randint(16, 32)
while len(family) < family_size:
    new_lemming = Lemming()
    family.append(new_lemming)
print(Lemming.total)


# или даже
burrow = []
burrow_depth = randint(90, 100)
while len(burrow) < burrow_depth:
    family = []
    family_size = randint(16, 32)
    while len(family) < family_size:
        new_lemming = Lemming()
        family.append(new_lemming)
    burrow.append(family)
print(Lemming.total)
print(burrow)


# в аттрибутах класса допустимо любое выражение пайтона
class Lemming:
    total, names = 0, ['Peter', 'Anna', 'Nik', 'Sofi', 'Den', 'Lora', 'Bred', ]
    names_count = len(names)
    some_text = 'Варкалось, хливкие шорьки пырялись по наве...'
    some_var = some_text + names[-1]

    def __init__(self):
        Lemming.total += 1
        self.name = choice(Lemming.names)

    def __str__(self):
        return 'Lemming ' + self.name

    def check_class_attrs(self):
        print('Lemming.total', Lemming.total)
        print('Lemming.names', Lemming.names)
        print('Lemming.names_count', Lemming.names_count)
        print('Lemming.some_text', Lemming.some_text)
        print('Lemming.some_var', Lemming.some_var)


new_lemming = Lemming()
print('Lemming.total', Lemming.total)
print('Lemming.names', Lemming.names)
print('Lemming.names_count', Lemming.names_count)
print('Lemming.some_text', Lemming.some_text)
print('Lemming.some_var', Lemming.some_var)
new_lemming.check_class_attrs()

