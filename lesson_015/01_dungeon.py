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
# если изначально не писать число в виде строки - теряется точность!

import datetime
import json
import os
import re
import time
from decimal import Decimal

# TODO
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
class GameCore:
    def __init__(self):
        self.is_end_game = False

    def end_game(self, _=None) -> (Decimal, int):
        self.is_end_game = True
        return 0, 0


class GameObject:
    time_pattern = r'tm\d{1,}'

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.is_end_game = False

    def get_time(self, obj):
        exp = re.search(self.time_pattern, obj)
        return Decimal(exp.group(0)[2:]) if exp else 0

    @property
    def time(self):
        return self.get_time(self.name)


class Creature(GameObject):
    exp_pattern = r'exp\d{0,}'

    def __init__(self, name):
        super().__init__(name)
        self.is_alive = True

    def get_exp(self, obj):
        exp = re.search(self.exp_pattern, obj)
        return Decimal(exp.group(0)[3:]) if exp else 0

    @property
    def exp(self):
        return self.get_exp(self.name)


class User(Creature):
    user_game_actions = {
        'attack': {'action_name': 'Атаковать монстра',
                   'action_targets': [],
                   'action': None,
                   'action_error_text': 'Монстров не видно !'},

        'move': {'action_name': 'Перейти в другую локацию',
                 'action_targets': [],
                 'action': None,
                 'action_error_text': 'Пещер не найдено !'},

        'exit': {'action_name': 'Сдаться и выйти из игры',
                 'action_targets': [],
                 'action': None,
                 'action_error_text': 'Ха ха... Ты не справился! Все деревни будут ограблены !'}
    }

    def __init__(self, name):
        super().__init__(name)
        self.map = None
        User.user_game_actions['attack']['action'] = self.attack_monster
        User.user_game_actions['move']['action'] = self.go_to_location

    @staticmethod
    def attack_monster(monster) -> (Decimal, int):
        if not monster:
            return 0, 0
        _time, exp = monster.kill()
        return _time, exp

    def set_map(self, map):
        self.map = map

    def get_map(self):
        return self.map

    def set_user_action(self, action_name, targets):
        self.user_game_actions[action_name]['action'] = targets

    def set_user_action_targets(self, action_name, targets):
        self.user_game_actions[action_name]['action_targets'] = targets

    def go_to_location(self, location) -> (Decimal, int):
        if not location:
            return 0, 0

        if location != self.map.current_location:
            for num, available_location in enumerate(self.map.rpg_map[self.map.current_location.name]):
                if isinstance(available_location, dict) and available_location.get(location.name, None):
                    self.map.rpg_map = {location.name: available_location.get(location.name, None)}
                    break

        _time, exp = self.get_time(location.name), 0
        return _time, exp


class Monster(Creature):

    def __init__(self, name):
        super().__init__(name)

    def kill(self) -> (Decimal, int):
        self.is_alive = False
        return self.time, self.exp

    def __str__(self):
        return f'{self.name} ({"alive" if self.is_alive else "dead"})'


class Map:

    def __init__(self, path_map):
        self.path_map = path_map
        self.rpg_map = {}

        self.current_location = None

    def open_map(self) -> None:
        with open(file=self.path_map, mode='r') as f:
            self.rpg_map = json.load(f)

    @staticmethod  # если этот метод работает с данными объекта зачем делать его статическим?...
    def _parse_map(game_map: dict) -> (str, tuple):
        for location, next_locations in game_map.items():
            return location, next_locations

    @staticmethod
    def _get_object_names(objects: list) -> list:
        object_names = []
        for object in objects:
            if isinstance(object, dict):
                object_names.extend([object_name for object_name in object])
            elif isinstance(object, list):
                object_names.extend(object)
            else:
                object_names.append(object)
        return object_names

    def create_new_location(self):
        current_location_name, map_objects = self._parse_map(game_map=self.rpg_map)
        if not self.current_location or self.current_location.name != current_location_name:
            object_names = self._get_object_names(objects=map_objects)
            self.current_location = Location(name=current_location_name)
            self.current_location.create_location_objects(object_names=object_names)


class Location(GameObject):
    patterns = {'cave': r'\w{,8}_\w{0,2}_\w{,2}(\d.\d+)',
                'creature': r'\w{,4}\d{,}_\w{3}\d{,3}_\w{,2}\d+',
                'hatch': r'\w{,5}_\w{,2}(\d.\d+)'}

    def __init__(self, name):
        super().__init__(name)
        self.available_location = {}
        self.available_monsters = {}
        self.location_objects = []
        self.object_names = []

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def _create_monsters(monster_name: list):
        return Monster(name=monster_name)

    @staticmethod
    def _create_location(location_name: list):
        return Location(name=location_name)

    def identify_object(self, object_name: str) -> str:
        if not object_name:
            return ''

        for name, pattern in self.patterns.items():
            res = re.match(pattern, object_name)
            if res:
                return name
        return ''

    def get_location_names(self, object_names):
        return [object_name for object_name in object_names if self.identify_object(object_name) in ('cave', 'hatch')]

    def get_monster_names(self, object_names):
        return [object_name for object_name in object_names if self.identify_object(object_name) == 'creature']

    def create_location_objects(self, object_names):
        self.create_monsters(self.get_monster_names(object_names))
        self.create_locations(self.get_location_names(object_names))

    def create_monsters(self, monster_names):
        monsters = [self._create_monsters(monster_name) for monster_name in monster_names]
        self.available_monsters = {self.name: monsters}

    def create_locations(self, location_names):
        locations = [self._create_location(location_name) for location_name in location_names]
        self.available_location = {self.name: locations}

    def get_alive_monster_count(self):
        return len([monster.name for monster in
                    self.available_monsters[self.name] if monster.is_alive])

    def get_location_monster(self, name):
        for monster in self.available_monsters[self.name]:
            if monster.name == name and monster.is_alive:
                return monster

    def get_available_monsters(self) -> list:
        return [monster for monster in
                self.available_monsters[self.name]]

    def get_alive_available_monsters(self) -> list:
        return [monster for monster in
                self.available_monsters[self.name] if monster.is_alive]

    def get_available_location(self) -> list:
        return [location for location in
                self.available_location[self.name]]


class GameDungeon(GameCore):

    HATCH_EXP_NEEDED = 280
    REMAINING_TIME = '123456.0987654321'

    def __init__(self, game_map: Map, user: User):
        super().__init__()

        self.user = user
        self.user.set_user_action('exit', self.end_game)

        self.map = game_map

        self.user_choice = None
        self.remaining_time_dec = Decimal(GameDungeon.REMAINING_TIME)
        self.user_total_time = 0

        self.is_exit_game = False
        self.is_win_game = False
        self.user_exp = 0

    def win_game(self, _=None) -> (Decimal, int):
        if self.user_exp >= GameDungeon.HATCH_EXP_NEEDED:
            self.is_win_game = True
        else:
            print('Недостаточно опыта чтобы открыть люк !')
            if self.map.current_location.get_alive_monster_count() == 0:
                self.is_end_game = True

        return 0, 0

    def show_game_state_info(self) -> None:
        print(f'Вы находитесь в {self.map.current_location.name}')
        print(f'У вас {self.user_exp} опыта и осталось {self.remaining_time_dec} секунд до наводнения')
        print(f'Прошло времени: {self.user_total_time}')
        print('')
        print('Внутри Вы видите:')
        _list = self.map.current_location.get_available_monsters()
        _list.extend(self.map.current_location.get_available_location())
        [print(f'- {way}') for way in _list]

    def game_checks(self):

        if self.is_exit_game:
            print('Спасибо за игру.')
            return False

        if self.remaining_time_dec <= 0:
            print('Время истекло !')
            self.is_end_game = True

        if self.is_end_game:
            print('О нееет вода поднимается !')
            print('Буль буль буль... вы уходите на дно !')
            print('Вжжжух.')
            print('Мамин амулет творит чудеса.')
            choice = input('Желаете воскреснуть ? (y/n)')
            if choice in ('Y', 'y', 'Д', 'д'):
                self.is_end_game = False
                return False
            else:
                self.is_exit_game = True
                return False
        elif self.is_win_game:
            print('Молодец! Ты выбрался из пещеры!')
            time.sleep(1)
            self.is_exit_game = True
            return False
        return True

    @staticmethod
    def ask_user(ask_text: str, choice_list: dict) -> int:
        while True:
            available_choices = [num + 1 for num in range(len(choice_list))]

            print(ask_text)

            [print(f'{num + 1}. {action.get("action_name")}') for num, action in enumerate(choice_list.values())]
            choice = input('')
            os.system('cls' if os.name == 'nt' else 'clear')

            if choice.isalpha() or choice not in map(str, available_choices):
                print(f'!!! ВНИМАНИЕ !!! Введено "{choice}", доступные варианты {available_choices}.')
                continue

            return int(choice)

    def ask_user_about_target(self, targets: dict) -> any:

        user_choice = None

        if not targets:
            return user_choice

        user_answer = self.ask_user('Доступные цели:', targets)
        for num, target in enumerate(targets.values()):
            if num + 1 == user_answer:
                user_choice = target.get("action_name")
                print(f'Вы выбрали "{user_choice}"')

        return user_choice

    def run_user_actions(self) -> (Decimal, int):

        action_time, action_exp = 0, 0

        choice = self.ask_user('Выберите действие:', self.user.user_game_actions)

        for num, action in enumerate(self.user.user_game_actions.values()):
            if choice == num + 1:

                action_targets_func = action.get('action_targets', None)
                action_targets = None

                if action_targets_func:
                    action_targets = {num + 1: {'action_name': record} for num, record in
                                      enumerate(action_targets_func())}

                if not action_targets:
                    print(action.get('action_error_text'))

                user_target_answer = self.ask_user_about_target(action_targets)

                if user_target_answer and self.map.current_location.identify_object(user_target_answer.name) == 'hatch':
                    action_time, action_exp = self.win_game()
                    break
                elif not user_target_answer and choice == 2:
                    action_time, action_exp = self.end_game()
                    break

                user_action_func = action.get('action')

                if user_action_func:
                    action_time, action_exp = user_action_func(user_target_answer)
                break

        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        return action_time, action_exp

    def run(self):

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            if not self.game_checks():
                break

            self.map.open_map()

            if not self.user.get_map():
                self.user.set_map(self.map)

            while True:

                os.system('cls' if os.name == 'nt' else 'clear')

                if not self.game_checks():
                    break

                begin_time = datetime.datetime.now()

                self.map.create_new_location()

                self.map = self.user.get_map()
                self.user.set_user_action_targets('attack', self.map.current_location.get_alive_available_monsters)
                self.user.set_user_action_targets('move', self.map.current_location.get_available_location)

                self.user.go_to_location(self.map.current_location)

                self.show_game_state_info()

                print('')

                action_time, action_exp = self.run_user_actions()

                # TODO вроде время на обдумывания хода не надо было учитывать
                end_time = datetime.datetime.now()
                delta_time = end_time - begin_time
                delta_time = Decimal(delta_time.seconds + (delta_time.microseconds / 1000000))

                self.remaining_time_dec -= delta_time + action_time
                self.user_total_time += delta_time + action_time
                self.user_exp += action_exp

# Учитывая время и опыт, не забывайте о точности вычислений!


if __name__ == '__main__':
    game_user = User(name='User')
    rpg_map = Map(path_map='rpg.json')
    game = GameDungeon(game_map=rpg_map, user=game_user)
    game.run()
