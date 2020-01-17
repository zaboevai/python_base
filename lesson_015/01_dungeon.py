# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет только две локации и не будет мобов
# (то есть в коренном json-объекте содержится список, содержащий только два json-объекта и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import datetime
import json
import os
import re
import time
from decimal import Decimal, getcontext

remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']

patterns = {'location': r'\w{,8}_\w{0,2}_\w{,2}(\d.\d+)',
            'creature': r'\w{,4}_\w{3}\d{,3}_\w{,2}\d+',
            'hatch': r'\w{,5}_\w{,2}(\d.\d+)'}


getcontext().prec = 12





def get_exp(way):
    _, exp, _ = way.split('_')
    return str(exp).replace('exp', '')


def get_time(way):
    *_, time = way.split('_')
    return str(time).replace('tm', '')





class Monster:

    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_live = is_alive

    def __str__(self):
        return f'{self.name} ({"alive" if self.is_live else "dead"})'


class GameDungeon:

    def __init__(self, path_map):
        self.path_map = path_map
        self.rpg_map = None

        self.next_location = None
        self.current_location = None
        self.is_end_game = False

        self.available_monsters = {}
        self.available_location = {}
        self.available_actions = ()

    def open_map(self):
        with open(file=self.path_map, mode='r') as f:
            self.rpg_map = json.load(f)

    def show_state_info(self, location: str, remaining_time: str, total_time: str, next_ways: list):
        print(f'Вы находитесь в {location}')
        print(f'У вас 0 опыта и осталось {remaining_time} секунд до наводнения')
        print(f'Прошло времени: {total_time}')
        print('')
        print('Внутри Вы видите:')

        [print(f'- {way}') for way in next_ways]

    def get_monsters(self, actions: list) -> list:
        return [action for action in actions if self.identify_action(action) == 'creature']

    def create_monsters(self, monsters: list) -> list:
        return [Monster(name=monster_name) for monster_name in monsters]

    def get_locations(self, ways):
        return [way for way in ways if self.identify_action(way) in ('location', 'hatch')]

    def get_ways_names(self, ways):
        next_ways = []
        for way in ways:
            if isinstance(way, dict):
                for way in way:
                    next_ways.append(way)
            elif isinstance(way, list):
                next_ways.extend(way)
            else:
                next_ways.append(way)
        return next_ways

    def get_current_location_info(self, game_map):
        for location, next_locations in game_map.items():
            return location, next_locations

    def identify_action(self, way):
        if not way:
            return

        for name, pattern in patterns.items():
            res = re.match(pattern, way)
            if res:
                return name

    def change_location(self, next_location):

        # cur_map = self.rpg_map
        # current_location, next_locations = self.get_current_location_info(self.rpg_map)

        if next_location:
            next_location_num = ''

            for num, way in enumerate(self.available_actions):
                if isinstance(way, str) and way == next_location:
                    next_location_num = int(num)
                elif isinstance(way, dict) and way.get(next_location, None):
                    next_location_num = int(num)
                elif isinstance(way, list) and next_location in way:
                    next_location_num = int(num)

            if next_location_num != '':
                self.rpg_map = self.available_actions[next_location_num]
                if self.identify_action(next_location) == 'hatch':
                    print(self.rpg_map[next_location])
                    self.is_end_game = True
                # else:
                #     current_location, self.available_actions = self.get_current_location_info(self.rpg_map)

        # next_ways = get_ways_names(next_locations)

        # return  current_location, next_ways

    def get_user_choice(self, choice_text, choice_list: list or tuple) -> chr:

        avalible_choices = [num + 1 for num in range(len(choice_list))]

        print(choice_text)
        [print(f'{num + 1}. {action}') for num, action in enumerate(choice_list)]
        choice = input('')
        os.system('cls' if os.name == 'nt' else 'clear')

        if choice.isalpha() or choice not in map(str, avalible_choices):
            print(f'!!! ВНИМАНИЕ !!! Введено "{choice}", доступные варианты {avalible_choices}.')
            time.sleep(1)
            return
        else:
            return int(choice)

    def user_action(self):

        next_location = None

        user_actions = ('Атаковать монстра',
                        'Перейти в другую локацию',
                        'Сдаться и выйти из игры')

        choice = self.get_user_choice('Выберите действие:', user_actions)

        if choice == 3:
            self.is_end_game = True
        elif choice == 2:
            if self.available_location:
                choice = self.get_user_choice('Доступные локации:', self.available_location)
                if choice:
                    for num, way in enumerate(self.available_location):
                        if num + 1 == choice:
                            next_location = way
                            print(f'Вы выбрали переход в локацию "{next_location}"')
            else:
                print('ТУПИК')
                self.is_end_game = True

        elif choice == 1:
            alive_monsters = [monster for monster in
                              self.available_monsters[self.current_location] if monster.is_live]

            if alive_monsters:
                choice = self.get_user_choice('Доступные монстры:', alive_monsters)
                if choice:
                    for num, monster in enumerate(alive_monsters):
                        if num + 1 == choice:
                            monster.is_live = False
                            print(f'Вы выбрали атаку на монстра "{monster.name}"')
            else:
                print('Нет доступных монстров')

        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        return next_location

    def run(self):

        self.open_map()

        remaining_time_dec = Decimal(remaining_time)
        total_time = Decimal()

        while True:

            if self.is_end_game:
                break

            begin_time = datetime.datetime.now()

            self.current_location, self.available_actions = self.get_current_location_info(self.rpg_map)

            # self.available_actions = self.get_ways_names(self.available_actions)

            if not self.available_monsters.get(self.current_location):
                monsters = self.get_monsters(self.get_ways_names(self.available_actions))
                self.available_monsters = {self.current_location: self.create_monsters(monsters)}

            self.available_location = self.get_locations(self.get_ways_names(self.available_actions))

            self.show_state_info(self.current_location, remaining_time_dec, total_time, self.get_ways_names(self.available_actions))

            print('')

            self.next_location = self.user_action()

            self.change_location(self.next_location)

            os.system('cls' if os.name == 'nt' else 'clear')

            end_time = datetime.datetime.now()
            delta_time = end_time - begin_time

            delta_time = Decimal(delta_time.seconds + (delta_time.microseconds / 1000000))
            remaining_time_dec -= delta_time
            total_time += delta_time

        print(self.current_location)
        [print(m) for m in self.available_monsters[self.current_location]]
        print('YOU LOOSE !')

    # os.system('cls' if os.name == 'nt' else 'clear')

    # for way_name in way_names:
    #
    #     identify = identify_way(way_name)
    #     print(way_name)
    #     if identify:
    #         if identify == 'creature':
    #             print(get_exp(way_name))
    #
    #         print(get_time(way_name))

    # Учитывая время и опыт, не забывайте о точности вычислений!


if __name__ == '__main__':
    game = GameDungeon(path_map='rpg.json')
    game.run()
