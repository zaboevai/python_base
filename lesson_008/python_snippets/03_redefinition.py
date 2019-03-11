# -*- coding: utf-8 -*-

# Переопределение атрибутов объекта и класса
# - используется если у дочернего класса отличные свойства


class Cat:
    has_tail = True
    woolliness = 20  # https://goo.gl/V2NcBf

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} {} хвост есть?  {}, пушистость - {}'.format(
            self.__class__.__name__, self.name, self.has_tail, self.woolliness)


class Bobtail(Cat):
    has_tail = False


class Sphinx(Cat):
    woolliness = 1


murzik = Bobtail(name='Мурзик')
sonya = Sphinx(name='Соня')
print(murzik)
print(sonya)


# Переопределение методов
# - используется если у порожденного класса должно отличаться поведение
class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class WarRobot(Robot):

    def operate(self):
        print('Робот охраняет военный обьект')


class VacuumCleaningRobot(Robot):

    def operate(self):
        print('Робот пылесосит пол')


r2d2 = WarRobot(model='R2D2')
print(r2d2)
r2d2.operate()

roomba = VacuumCleaningRobot(model='roomba M505')
print(roomba)
roomba.operate()

