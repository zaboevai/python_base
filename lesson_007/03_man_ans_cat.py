# -*- coding: utf-8 -*-

from random import randint, choice
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:
    # TODO Делать дом атрибутом класса не правильно, потому что гипотетически
    # TODO может быть создано несколько экземпляров класса Man и все эти люди должны
    # TODO жить в разных домах.
    # TODO Необходимо сделать house атрибутом экземпляра класса (как было
    # TODO раньше) и просто производить его инициализацию в init, а не через setter
    house = None

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.money = 100
        self.cats = []

    def __str__(self):
        return 'Я - {}, сытость {}, денег осталось {}, {}'.format(self.name,
                                                                  self.fullness,
                                                                  self.money,
                                                                  'у меня есть котики: '+', '.join(self.cats)
                                                                  if self.cats else 'мечтаю завести котиков')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='magenta')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.money += 150
        self.fullness -= 10

    def clean_house(self):
        cprint('{} почистил дом'.format(self.name), color='magenta')
        self.house.mud -= 100
        self.fullness -= 20

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='magenta')
        self.fullness -= 10

    def shopping(self):

        if self.house.food <= 10 and self.money >= 50:
            self.money -= 50
            self.house.food += 50
            cprint('{} сходил в магазин себе за едой'.format(self.name), color='magenta')

        cat_food_need = len(self.cats) * 50

        if self.cats and self.house.cat_food <= len(self.cats) * 10:
            if cat_food_need <= self.money:
                self.house.cat_food += cat_food_need
                self.money -= cat_food_need
                cprint('{} сходил в магазин за едой кошкам'.format(self.name), color='magenta')
            elif cat_food_need >= self.money:
                self.house.cat_food += self.money
                self.money = 0
                cprint('{} сходил в магазин за едой кошкам на последние деньги'.format(self.name), color='magenta')

        self.fullness -= 10

    def move_in_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='magenta')

    def pick_a_cat(self, cat):
        self.cats.append(cat.name)
        self.fullness -= 5
        cprint('{} подобрал котика {} в дом'.format(self.name, cat.name), color='magenta')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.money < 100:
            self.work()
        elif self.house.food <= 10 or (self.cats and self.house.cat_food <= len(self.cats) * 10):
            self.shopping()
        elif self.fullness > 20 and self.house.mud >= 100:
            self.clean_house()
        elif dice == 1:
            self.watch_mtv()
        elif dice == 2:
            self.eat()
        else:
            self.work()


class House:

    def __init__(self):
        self.food = 50
        self.mud = 20
        self.cat_food = 0

    def __str__(self):
        return 'В доме еды осталось {}, кошачьей еды {}, грязи {}'.format(self.food,
                                                                          self.cat_food,
                                                                          self.mud)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = randint(1, 6) * 10
        self.house = None

    def __str__(self):
        return 'Я котик - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):

        if self.house:
            if self.house.cat_food > 0:
                self.fullness += 20
                self.house.cat_food -= 10
                cprint('Котик {} покушал, сытость {}'.format(self.name, self.fullness), color='cyan')
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.fullness -= 10
                cprint('Уличный котик {} НЕ поймал мышь, сытость {}'.format(self.name, self.fullness), color='yellow')
            else:
                self.fullness += 20
                cprint('Уличный котик {} поймал мышь, сытость {}'.format(self.name, self.fullness), color='yellow')

    def play(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint('Котик {} поиграл, сытость {}'.format(self.name, self.fullness), color='cyan')

    def sleep(self):
        if self.house:
            self.fullness -= 10
            self.house.mud += 5
            cprint('Котик {} поспал, сытость {}'.format(self.name, self.fullness), color='cyan')
        else:
            self.fullness -= 10
            cprint('Уличный котик {} спит, сытость {}'.format(self.name, self.fullness), color='yellow')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.mud += 5
        cprint('Котик {} драл обои, сытость {}'.format(self.name, self.fullness), color='cyan')

    def settle_in_house(self, house):
        self.house = house
        cprint('Котик {} переехал в дом'.format(self.name, self.fullness), color='cyan')

    def feces(self):
        self.house.mud += 20
        self.fullness -= 10
        cprint('Котик {} нагадил, сытость {}'.format(self.name, self.fullness), color='cyan')

    def act(self):
        dice = randint(1, 6)
        if self.fullness < 0:
            cprint('Котик {} сдох'.format(self.name), color='red')
        elif self.fullness <= 10:
            self.eat()
        elif self.house and dice == 1:
            self.play()
        elif self.house and dice == 2:
            self.feces()
        elif self.house and dice == 3:
            self.tear_wallpaper()
        else:
            self.sleep()


sweet_home = House()
print(sweet_home)
man = Man('Кузьма')
print(man)

street_cats = [Cat('Барсик'),
               Cat('Рыжик'),
               Cat('Пончик'),
               Cat('Адольф'),
               Cat('Матильда'),
               ]

home_cats = []

for cat in street_cats:
    print(cat)

man.move_in_house(sweet_home)

for day in map(str, range(1, 366)):
    cprint('=== день '+day+' ===', color='red')

    man.act()
    print(man)

    if man.money // (len(man.cats) + 1) >= 200:
        if len(street_cats) > 0:
            some_cat = choice(street_cats)
            home_cats.append(some_cat)
            man.pick_a_cat(some_cat)
            some_cat.settle_in_house(sweet_home)
            street_cats.remove(some_cat)

    for cat in street_cats:
        cat.act()

    for cat in home_cats:
        cat.act()

    print(sweet_home)


cprint('**********************', color='magenta')
cprint('Итоги года:', color='magenta')

for cat in home_cats:
    cprint(cat, color='magenta')

for cat in street_cats:
    cprint(cat, color='magenta')

cprint(man, color='magenta')
cprint('**********************', color='magenta')


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
