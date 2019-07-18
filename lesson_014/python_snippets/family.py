# -*- coding: utf-8 -*-

# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


from termcolor import cprint
from random import randint, choice


class House:
    def __init__(self, need_logging=False, log_file=None):
        self.need_logging = need_logging
        self.log_file = log_file
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0

    def log(self, massage, color=None, attrs=None):
        if self.log_file:
            print(massage, file=self.log_file)
        elif self.need_logging:
            cprint(text=massage, color=color, attrs=attrs)

    def day_bar(self, day):
        self.log(f'{day:=^70}', color='yellow', attrs=['bold', 'reverse'])

    def log_house_info(self):
        self.log('В доме: денег {}, человеческой еды {}, кошачьей еды {}, грязи {}'.
                 format(self.money, self.food, self.cat_food, self.dirt), color='cyan')

    def lost_food(self):
        self.food = 0
        self.log('Пропада вcя еда из холодильника!', color='red')

    def lost_money(self):
        self.money = int(self.money / 2)
        self.log('Пропала половина денег!', color='red')

    def incident(self, day, incidents_days):
        what_will_happen = randint(0, 1)
        if day in incidents_days:
            if what_will_happen == 0:
                self.lost_food()
            else:
                self.lost_money()


class Person:
    color = 'grey'
    HUNGRY_LEVEL = 20

    def __init__(self, name, house, need_logging=False, log_file=None):
        self.need_logging = need_logging
        self.log_file = log_file
        self.name = name
        self.house = house
        self.fullness = 30
        self.happiness = 100
        self.totals = {
            'work_days': ['Рабочих дней', 0],
            'game_days': ['Игровых дней', 0],
            'make_money': ['Заработано денег', 0],
            'shopping_days': ['Походов за едой', 0],
            'bought_food': ['Кулено еды', 0],
            'clean_days': ['Дней уборки', 0],
            'cleaned_dirt': ['Вычищено грязи', 0],
            'watch_days': ['Просмотров сериала', 0],
            'bought_fur_coats': ['Куплено шуб', 0],
            'sleeping_days': ['Дней сна', 0],
            'soiling_days': ['Дней, когда драл обои', 0],
            'happiness': ['Всего получено счастья', 0],
            'buy_cat_food_times': ['Походов за кошачьей едой', 0],
            'stroking_cat_times': ['Прикосновений к коту', 0],
            'eating_times': ['Приемов пищи', 0],
            'eaten_food': ['Съеденно еды', 0],
            'spend_money': ['Потрачено денег', 0],
        }

    @property
    def is_dead(self):
        return self.fullness < 0 or self.happiness < 10

    @property
    def is_hungry(self):
        return self.fullness < self.HUNGRY_LEVEL

    # передавать в _свои_ методы _свои_ аттрибуты - очень странно. Лучше так:
    def log(self, massage, color=None, attrs=None):
        if color is None:
            color = self.color
        if self.log_file:
            print(massage, file=self.log_file)
        elif self.need_logging:
            cprint(text=massage, color=color, attrs=attrs)

    def log_totals(self):
        self.log('{}: '.format(self.name), color='yellow')
        for value in self.totals.values():
            if value[1] != 0:
                self.log('\t{} -> {}'.format(value[0], value[1]), color='yellow')


class Man(Person):
    MAN_EATING_POINTS = 30
    CAT_EATING_POINTS_FOR_BUY = 30

    @property
    def is_tired_of_dirt(self):
        return self.house.dirt > 90

    def log_man_info(self):
        self.log('{}: сытость {}, счастье {}'.format(self.name, self.fullness, self.happiness), color='cyan')

    def eat(self):
        if self.house.food > 0:
            if self.house.food >= self.MAN_EATING_POINTS:
                eating_points = self.MAN_EATING_POINTS
                self.log('{} хорошо поел(а)'.format(self.name))
            else:
                eating_points = self.house.food
                self.log('{} немного поел(а)'.format(self.name))
            self.fullness += eating_points
            self.house.food -= eating_points
            self.totals['eaten_food'][1] += eating_points
            self.totals['eating_times'][1] += 1
        else:
            self.fullness -= 10
            self.log('{} нет еды!'.format(self.name), color='red')

    def buy_cat_food(self):
        self.fullness -= 10
        if self.house.money >= self.CAT_EATING_POINTS_FOR_BUY:
            self.house.cat_food += self.CAT_EATING_POINTS_FOR_BUY
            self.house.money -= self.CAT_EATING_POINTS_FOR_BUY
            self.totals['spend_money'][1] += self.CAT_EATING_POINTS_FOR_BUY
            self.totals['buy_cat_food_times'][1] += 1
            self.log('{} купил(а) коту еды'.format(self.name))
        else:
            self.log('{} нет денег на еду для кота!'.format(self.name), color='red')

    def stroking_cat(self):
        self.fullness -= 10
        self.happiness += 5
        self.totals['stroking_cat_times'][1] += 1
        self.log('{} гладил(а) кота'.format(self.name))

    def act(self):
        if self.is_dead:
            self.log('{} умер(ла)!'.format(self.name), color='red')
            return True
        if self.is_hungry:
            self.eat()
            return True


class Husband(Man):
    color = 'blue'
    SALARY = 50
    MONEY_LEVEL_FOR_LIFE = 500
    HAPPINESS_LEVEL_FOR_LIFE = 20

    def work(self):
        self.fullness -= 10
        self.house.money += self.SALARY
        self.totals['make_money'][1] += self.SALARY
        self.totals['work_days'][1] += 1
        self.log('{} сходил на работу'.format(self.name))

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        self.totals['happiness'][1] += 20
        self.totals['game_days'][1] += 1
        self.log('{} играл в Танки'.format(self.name))

    def act(self):
        if self.is_tired_of_dirt:
            self.happiness -= 10
        dice = randint(1, 6)
        if super().act():
            return
        elif self.happiness < self.HAPPINESS_LEVEL_FOR_LIFE:
            self.gaming()
        elif self.house.money < self.MONEY_LEVEL_FOR_LIFE:
            self.work()
        elif self.house.cat_food < self.CAT_EATING_POINTS_FOR_BUY:
            self.buy_cat_food()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.stroking_cat()
        else:
            self.gaming()


class Wife(Man):
    color = 'magenta'
    FOOD_LEVEL_FOR_LIFE = 100
    DIRT_LEVEL_FOR_LIFE = 100
    HAPPINESS_LEVEL_FOR_LIFE = 40

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= self.FOOD_LEVEL_FOR_LIFE:
            self.house.money -= self.FOOD_LEVEL_FOR_LIFE
            self.house.food += self.FOOD_LEVEL_FOR_LIFE
            self.totals['spend_money'][1] += self.FOOD_LEVEL_FOR_LIFE
            self.totals['bought_food'][1] += self.FOOD_LEVEL_FOR_LIFE
            self.totals['shopping_days'][1] += 1
            self.log('{} купила еды'.format(self.name))
        else:
            self.log('{} нет денег на еду!'.format(self.name), color='red')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0
        self.totals['cleaned_dirt'][1] += 100
        self.totals['clean_days'][1] += 1
        self.log('{} убралась в доме'.format(self.name))

    def watch_series(self):
        self.fullness -= 10
        self.totals['watch_days'][1] += 1
        series_mood = randint(0, 1)
        if series_mood == 1:
            self.happiness += 5
            self.totals['happiness'][1] += 5
            self.log('{} смотрела сериал, осталась довольна'.format(self.name))
        else:
            self.happiness -= 5
            self.totals['happiness'][1] -= 5
            self.log('{} смотрела сериал, расстроилась'.format(self.name))

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            self.totals['spend_money'][1] += 350
            self.totals['happiness'][1] += 60
            self.totals['bought_fur_coats'][1] += 1
            self.log('{} купила шубу'.format(self.name))
        else:
            self.log('{} нет денег на шубу!'.format(self.name), color='red')

    def act(self):
        dice = randint(1, 6)
        if super().act():
            return
        elif self.house.food < self.FOOD_LEVEL_FOR_LIFE:
            self.shopping()
        elif self.happiness < self.HAPPINESS_LEVEL_FOR_LIFE:
            self.buy_fur_coat()
        elif self.house.dirt > self.DIRT_LEVEL_FOR_LIFE:
            self.clean_house()
        elif self.house.cat_food < self.CAT_EATING_POINTS_FOR_BUY:
            self.buy_cat_food()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            self.shopping()
        elif dice == 4:
            self.buy_fur_coat()
        elif dice == 5:
            self.stroking_cat()
        else:
            self.watch_series()


class Child(Man):
    color = 'grey'
    MAN_EATING_POINTS = 10

    def sleep(self):
        self.fullness -= 10
        self.totals['sleeping_days'][1] += 1
        self.log('{} спал весь день'.format(self.name))

    def act(self):
        if super().act():
            return
        else:
            self.sleep()


class Cat(Person):
    color = 'white'
    CAT_EATING_POINTS = 10

    def log_cat_info(self):
        self.log('{}: сытость {}'.format(self.name, self.fullness), color='cyan')

    def eat(self):
        if self.house.cat_food > 0:
            if self.house.cat_food >= self.CAT_EATING_POINTS:
                eating_points = self.CAT_EATING_POINTS
                self.log('{} хорошо поел'.format(self.name))
            else:
                eating_points = self.house.cat_food
                self.log('{} немного поел'.format(self.name))
            self.fullness += eating_points * 2
            self.house.cat_food -= eating_points
            self.totals['eaten_food'][1] += eating_points
            self.totals['eating_times'][1] += 1
        else:
            self.fullness -= 10
            self.log('{} нет еды!'.format(self.name))

    def sleep(self):
        self.fullness -= 10
        self.totals['sleeping_days'][1] += 1
        self.log('{} спал весь день'.format(self.name))

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 5
        self.totals['soiling_days'][1] += 1
        self.log('{} драл обои'.format(self.name))

    def act(self):
        if self.is_dead:
            self.log('{} умер!'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.is_hungry:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice in [2, 3]:
            self.sleep()
        else:
            self.soil()

def emulate_life(num_cats, need_logging=False):
    home = House(need_logging=True)
    vasya = Husband(name='Вася', house=home, need_logging=need_logging)
    vasya.SALARY = 250
    masha = Wife(name='Маша', house=home, need_logging=need_logging)
    kolya = Child(name='Коля', house=home, need_logging=need_logging)
    cat_names = [ 'Мурзик', 'Барсик', 'Борис',
                  'Альфа', 'Бета', 'Гамма', 'Эпсилон',
                  'Ньютон', 'Эйнштейнн', 'Паскаль', ]
    cats = [Cat(name=choice(cat_names), house=home, need_logging=need_logging)
            for _ in range(num_cats)]

    somebody_is_dead = False
    for day in range(1, 366):
        home.day_bar(day)
        vasya.act()
        masha.act()
        kolya.act()
        if vasya.is_dead or masha.is_dead or kolya.is_dead:
            somebody_is_dead = True
        for cat in cats:
            cat.act()
            if cat.is_dead:
                somebody_is_dead = True
        if somebody_is_dead:
            home.log('Труп в квартире', color='red')
            break
        vasya.log_man_info()
        masha.log_man_info()
        kolya.log_man_info()
        for cat in cats:
            cat.log_cat_info()
        home.log_house_info()

    if not somebody_is_dead:
        vasya.log_totals()
        masha.log_totals()
        kolya.log_totals()
        for cat in cats:
            cat.log_totals()


if __name__ == '__main__':
    emulate_life(num_cats=2, need_logging=True)