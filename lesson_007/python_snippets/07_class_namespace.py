# -*- coding: utf-8 -*-

from random import randint, choice


# К атрибутам класса можно обратится и через объект
class Lemming:
    names = ['Peter', 'Anna', 'Nik', 'Sofi', 'Den', 'Lora', 'Bred', ]
    tail_length = 20

    def __init__(self):
        self.name = choice(Lemming.names)

    def __str__(self):
        return 'Lemming ' + self.name + ' with tail ' + str(self.tail_length)


print(Lemming.tail_length)

new_lemming = Lemming()
print(new_lemming.tail_length)
print(new_lemming)


# Атрибут объекта перекрывает атрибут класса
class Lemming:
    names = ['Peter', 'Anna', 'Nik', 'Sofi', 'Denn', 'Lora', 'Bred', ]
    tail_length = 20

    def __init__(self):
        self.tail_length = randint(15, 25)
        self.name = choice(Lemming.names)

    def __str__(self):
        return 'Lemming ' + self.name + ' with tail ' + str(self.tail_length)


print(Lemming.tail_length)

new_lemming = Lemming()
print(new_lemming.tail_length)
print(new_lemming)


# типичная ошибка
class Lemming:
    names = ['Peter', 'Anna', 'Nik', 'Sofi', 'Denn', 'Lora', 'Bred', ]
    total = 0
    tail_length = 20

    def __init__(self):
        self.tail_length = randint(15, 25)
        self.name = choice(Lemming.names)
        self.total = self.total + 1

    def __str__(self):
        return 'Lemming ' + self.name + ' with tail ' + str(self.tail_length)


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
print(len(burrow))


# А что с обычными переменными? все так же как для функций


class SomeClass:

    def method_one(self):
        # x = 23
        print('method_one', x)

    def method_two(self):
        # x = 34
        def func_one():
            # x = 56
            print('func_one', x)
        func_one()
        print('method_two', x)


x = 12
obj = SomeClass()
obj.method_one()
obj.method_two()
print('global', x)
