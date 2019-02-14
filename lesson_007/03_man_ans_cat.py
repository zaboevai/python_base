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

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = []

    def __str__(self):
        return 'Я - {}, сытость {}, у меня есть кошка {}'.format(self.name,
                                                                 self.fullness,
                                                                 ', '.join(self.cat) if self.cat else 'в "мечтах"')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='magenta')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.house.money += 50
        self.fullness -= 10

    def clean_house(self):
        cprint('{} почистил дом'.format(self.name), color='magenta')
        self.house.mud = 0
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='magenta')
        self.fullness -= 10

    def shopping(self):
        # TODO переделать покупку еды
        # TODO покупать еду кошкам исходя из их кол-ва
        money_need = 0
        if self.house.cat_food <= 10:
            money_need += 50
        elif self.house.food <= 10:
            money_need += 50

        if self.house.money >= money_need:
            if self.house.food <= 10:
                self.house.money -= 50
                self.house.food += 50
                cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            elif self.house.cat_food <= 10:
                self.house.cat_food += 50
                self.house.money -= 50
                cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')

            self.fullness -= 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='magenta')

    def pick_a_cat(self, cat):
        self.cat.append(cat.name)
        self.fullness -= 5
        cprint('{} подобрал котика {} в дом'.format(self.name, cat.name), color='magenta')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 100:
            self.work()
        elif self.house.food < 10 or self.house.cat_food < 10:
            self.shopping()
        elif self.house.mud > 50:
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
        self.money = 100
        self.mud = 20
        self.cat_food = 0

    def __str__(self):
        return 'В доме еды осталось {}, кошачьей еды {}, денег осталось {}, грязи {}'.format(self.food,
                                                                                             self.cat_food,
                                                                                             self.money,
                                                                                             self.mud)

class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = randint(1, 6) * 10
        self.house = None

    def __str__(self):
        return 'Я котик - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        cprint('Котик {} покушал'.format(self.name), color='cyan')
        self.fullness += 20
        self.house.cat_food -= 10

    def play(self):
        cprint('Котик {} поиграл'.format(self.name), color='cyan')
        self.fullness -= 10
        self.house.mud += 5

    def sleep(self):
        cprint('Котик {} поспал'.format(self.name), color='cyan')
        self.fullness -= 10
        self.house.mud += 5

    def tear_wallpaper(self):
        cprint('Котик {} драл обои'.format(self.name), color='cyan')
        self.fullness -= 10
        self.house.mud += 5

    def settle_in_the_house(self, house):
        cprint('Котик {} переехал в дом'.format(self.name), color='cyan')
        self.house = house

    def feces(self):
        self.house.mud += 20
        cprint('Котик {} нагадил'.format(self.name), color='cyan')

    def act(self):
        dice = randint(1, 6)
        if self.house:
            if self.fullness < 0:
                cprint('Котик {} сдох'.format(self.name), color='red')
            elif self.fullness <= 10 and self.house.cat_food > 0:
                self.eat()
            elif dice == 1:
                self.play()
            elif dice == 2:
                self.feces
            elif dice == 3:
                self.tear_wallpaper
            else:
                self.sleep()
        else:
            if self.fullness < 0:
                cprint('Котик {} сдох'.format(self.name), color='red')
            elif self.fullness <= 30:
                dice = randint(1, 6)
                if dice == 1:
                    cprint('Котик {} не поймал мышь'.format(self.name), color='yellow')
                    self.fullness -= 10
                else:
                    cprint('Котик {} поймал мышь'.format(self.name), color='yellow')
                    self.fullness += 20
            else:
                cprint('Котик {} ходит бродит'.format(self.name), color='yellow')
                self.fullness -= 10


sweet_home = House()
print(sweet_home)
man = Man('Кузьма')
print(man)

street_cats = [Cat('Барсик'),
               Cat('Рыжик'),
               Cat('Пончик'),
               Cat('Адольф'),
               Cat('Матильда'), ]

home_cats = []

for cat in street_cats:
    print(cat)

man.go_to_the_house(sweet_home)

for day in map(str, range(1, 366)):
    cprint('=== день '+day+' ===', color='red')

    # print(sweet_home)
    man.act()
    print(man)

    if man.house.money // (len(man.cat) if len(man.cat) != 0 else 1) >= 300:
        if len(street_cats) > 0:
            some_cat = choice(street_cats)
            home_cats.append(some_cat)
            man.pick_a_cat(some_cat)
            some_cat.settle_in_the_house(sweet_home)
            street_cats.remove(some_cat)

    for cat in street_cats:
        cat.act()

    for cat in home_cats:
        cat.act()

        # print(cat)
    print(sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
