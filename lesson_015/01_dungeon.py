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

getcontext().prec = 12


def convert_list(func):
    def wrapper(act):
        func_list = func(act)
        return {num + 1: {'action_name': monster} for num, monster in enumerate(func_list)} if func_list else None

    return wrapper


class GameScoreMixin:

    time_pattern = r'tm\d{1,}'
    exp_pattern = r'exp\d{0,}'

    @staticmethod
    def get_exp(obj):
        exp = re.search(GameScoreMixin.exp_pattern, obj)
        return Decimal(exp.group(0)[3:]) if exp else 0

    @staticmethod
    def get_time(obj):
        exp = re.search(GameScoreMixin.time_pattern, obj)
        return Decimal(exp.group(0)[2:]) if exp else 0


class Monster(GameScoreMixin):

    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_alive = is_alive

    @property
    def exp(self):
        return self.get_exp(self.name)

    @property
    def time(self):
        return self.get_time(self.name)

    def kill_monster(self) -> (Decimal, int):
        self.is_alive = False
        return self.time, self.exp

    def __str__(self):
        return f'{self.name} ({"alive" if self.is_alive else "dead"})'


class GameDungeon(GameScoreMixin):
    is_end_game = False
    is_exit_game = False

    patterns = {'location': r'\w{,8}_\w{0,2}_\w{,2}(\d.\d+)',
                'creature': r'\w{,4}\d{,}_\w{3}\d{,3}_\w{,2}\d+',
                'hatch': r'\w{,5}_\w{,2}(\d.\d+)'}

    def __init__(self, path_map):

        self.path_map = path_map
        self.rpg_map = {}

        self.user_choice = None
        self.current_location = None

        self.available_monsters = {}
        self.available_location = {}
        self.available_actions = []
        self.action_names = []

    def open_map(self):
        with open(file=self.path_map, mode='r') as f:
            self.rpg_map = json.load(f)

    def show_game_state_info(self, _remaining_time: str, total_time: str, total_exp) -> None:
        print(f'Вы находитесь в {self.current_location}')
        print(f'У вас {total_exp} опыта и осталось {_remaining_time} секунд до наводнения')
        print(f'Прошло времени: {total_time}')
        print('')
        print('Внутри Вы видите:')

        [print(f'- {way}') for way in self.action_names]

    @staticmethod
    def _create_monsters(monster_names: list) -> list:
        return [Monster(name=monster_name) for monster_name in monster_names]

    @staticmethod
    def _get_action_names(actions: list) -> list:
        action_names = []
        for action in actions:
            if isinstance(action, dict):
                for action_name in action:
                    action_names.append(action_name)
            elif isinstance(action, list):
                action_names.extend(action)
            else:
                action_names.append(action)
        return action_names

    @staticmethod
    def _parse_map(game_map: dict) -> (str, tuple):
        for location, next_locations in game_map.items():
            return location, next_locations

    def _identify_action(self, action: str) -> str:
        if not action:
            return ''

        for name, pattern in self.patterns.items():
            res = re.match(pattern, action)
            if res:
                return name
        return ''

    @convert_list
    def get_available_monsters(self):
        if not self.available_monsters.get(self.current_location):
            monster_names = [action for action in self.action_names if self._identify_action(action) == 'creature']
            self.available_monsters = {self.current_location: self._create_monsters(monster_names)}

        alive_monsters = [monster for monster in
                          self.available_monsters[self.current_location] if monster.is_alive]

        return alive_monsters #{num + 1: {'action_name': monster} for num, monster in enumerate(alive_monsters)}

    @convert_list
    def get_available_locations(self):
        available_locations = [location for location in self.action_names if
                               self._identify_action(location) in ('location', 'hatch')]
        return available_locations #{num + 1: {'action_name': location} for num, location in enumerate(available_locations)}

    def end_game(self, _=None) -> (Decimal, int):
        self.is_end_game = True
        return 0, 0

    def attack_monster(self, monster: Monster) -> (Decimal, int):
        if not monster:
            return 0, 0
        _time, exp = monster.kill_monster()
        return _time, exp

    def change_location(self, next_location: str) -> (Decimal, int):

        if not next_location:
            return self.end_game()

        next_location_num = ''

        for num, available_action in enumerate(self.available_actions):
            if isinstance(available_action, dict) and available_action.get(next_location, None):
                next_location_num = num

        if next_location_num != '':
            self.rpg_map = self.available_actions[next_location_num]

        _time, exp = self.get_time(next_location), 0
        return _time, exp

    @staticmethod
    def get_user_choice(choice_text: str, choice_list: dict) -> int:
        while True:
            avalible_choices = [num + 1 for num in range(len(choice_list))]

            print(choice_text)

            [print(f'{num}. {action.get("action_name")}') for num, action in choice_list.items()]
            choice = input('')
            os.system('cls' if os.name == 'nt' else 'clear')

            if choice.isalpha() or choice not in map(str, avalible_choices):
                print(f'!!! ВНИМАНИЕ !!! Введено "{choice}", доступные варианты {avalible_choices}.')
                continue

            return int(choice)

    def user_action(self) -> (Decimal, int):

        action_time, action_exp = 0, 0

        user_actions = {
            1: {'action_name': 'Атаковать монстра',
                'action_targets': self.get_available_monsters,
                'action': self.attack_monster,
                'action_error_text': 'Монстров не видно !'},

            2: {'action_name': 'Перейти в другую локацию',
                'action_targets': self.get_available_locations,
                'action': self.change_location,
                'action_error_text': 'Пещер не найдено !'},

            3: {'action_name': 'Сдаться и выйти из игры',
                'action_targets': None,
                'action': self.end_game,
                'action_error_text': 'Ха ха слабак !'}
        }

        choice = self.get_user_choice('Выберите действие:', user_actions)

        if choice:
            for num, action in user_actions.items():
                if choice == num:
                    action_targets = action.get('action_targets')

                    if action_targets:
                        action_targets = action_targets()

                    if not action_targets:
                        print(action.get('action_error_text'))

                    user_target_choice = self.get_user_target_choice(action_targets)

                    user_action = action.get('action')
                    action_time, action_exp = user_action(user_target_choice)

        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        return action_time, action_exp

    def get_user_target_choice(self, targets):

        user_choice = None

        if not targets:
            return user_choice

        user_target_num = self.get_user_choice('Доступные цели:', targets)
        for num, target in enumerate(targets.values()):
            if num + 1 == user_target_num:
                print(f'Вы выбрали "{target.get("action_name")}"')
                user_choice = target.get("action_name")

        return user_choice

    def game_checks(self):
        if self.is_end_game:
            print('О нееет вода поднимается !')
            print('Вжжжух.')
            print('Мамин амулет творит чудеса.')
            choice = input('Желаете воскреснуть ? (y/n)')
            if choice in ('Y', 'y', 'Д', 'д'):
                self.is_end_game = False
                return False
            else:
                self.is_exit_game = True
                return False
        return True

    def run(self):

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            if self.is_exit_game:
                print('Спасибо за игру.')
                break

            self.open_map()
            remaining_time_dec = Decimal(remaining_time)
            total_time, total_exp = Decimal(), Decimal()

            while True:

                os.system('cls' if os.name == 'nt' else 'clear')

                if not self.game_checks():
                    break

                begin_time = datetime.datetime.now()

                self.current_location, self.available_actions = self._parse_map(self.rpg_map)

                self.action_names = self._get_action_names(self.available_actions)

                self.show_game_state_info(remaining_time_dec, total_time, total_exp)

                print('')

                action_time, action_exp = self.user_action()

                end_time = datetime.datetime.now()
                delta_time = end_time - begin_time

                delta_time = Decimal(delta_time.seconds + (delta_time.microseconds / 1000000))
                remaining_time_dec -= delta_time + action_time
                total_time += delta_time + action_time
                total_exp += action_exp

# Учитывая время и опыт, не забывайте о точности вычислений!

if __name__ == '__main__':
    game = GameDungeon(path_map='rpg.json')

    game.run()
