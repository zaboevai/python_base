# -*- coding: utf-8 -*-

# Наследование применяется там, где можно выделить общие свойство/поведение обьектов класса.
# Например, домашние животные. Они все имеют 4 ноги и хвост. Но кричат по разному...


class Pet:
    """ Домашнее животное """
    legs = 4
    has_tail = True

    def inspect(self):
        print('Всего ног:', self.legs)
        print('Хвост присутствует -', 'да' if self.has_tail else 'нет')


class Cat(Pet):
    """ Кошка - является Домашним Животным """

    def sound(self):
        print('Мяу!')


class Dog(Pet):
    """ Собака - является Домашним Животным """

    def sound(self):
        print('Гав!')


class Hamster(Pet):
    """ Хомячок - является Домашним Животным """

    def sound(self):
        print('Ццццццц!')  # https://goo.gl/KXoj21


print("Котик")
my_pet = Cat()
my_pet.inspect()
my_pet.sound()

print("Собачка")
my_pet = Dog()
my_pet.inspect()
my_pet.sound()

print("Хомячок")
my_pet = Hamster()
my_pet.inspect()
my_pet.sound()


# Полезные встроенные аттрибуты
class Pet:
    """ Домашнее животное """
    legs = 4
    has_tail = True

    def __init__(self, name):
        self.name = name

    def inspect(self):
        print(self.__class__.__name__, self.name)  # ссылка на класс обьекта и далее на имя класса
        print('  Всего ног:', self.legs)
        print('  Хвост присутствует -', 'да' if self.has_tail else 'нет')
        print(self.__dict__)  # подкапотный словарь атрибутов и методов


pet = Pet(name="Кузя")
print(pet.__class__ is Pet)


# Порядок поиска атрибутов объекта:
#   сам обьект
#   класс
#   родительский класс

class Pet:
    """ Домашнее животное """
    legs = 4
    has_tail = True

    def inspect(self):
        print('Всего ног:', self.legs)
        print('Хвост присутствует -', 'да' if self.has_tail else 'нет')


class Cat(Pet):
    """ Кошка - является Домашним Животным """

    def sound(self):
        print('Мяу!')


class Bobtail(Cat):
    """ Бобтейл - является Кошкой """
    has_tail = False


print("Бобтейл")
my_pet = Bobtail()
# my_pet.legs = 5
my_pet.inspect()
my_pet.sound()


# Еще пример наследования, чуть более абстрактный - класс-роль "Может летать"
class CanFly:

    def __init__(self):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        pass

    def fly(self):
        pass

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
        return '{} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity)


class Butterfly(CanFly):

    def take_off(self):
        self.altitude = 1

    def fly(self):
        self.velocity = 0.1


class Aircraft(CanFly):

    def take_off(self):
        self.velocity = 300
        self.altitude = 1000

    def fly(self):
        self.velocity = 800


class Missile(CanFly):

    def take_off(self):
        self.velocity = 1000
        self.altitude = 10000

    def land_on(self):
        self.altitude = 0
        self.destroy_enemy_base()

    def destroy_enemy_base(self):
        print('БА-БАХ!')


butterfly = Butterfly()
print(butterfly)
butterfly.take_off()
print(butterfly)
butterfly.fly()
print(butterfly)
butterfly.land_on()
print(butterfly)

missile = Missile()
print(missile)
missile.take_off()
print(missile)
missile.fly()
print(missile)
missile.land_on()
print(missile)

