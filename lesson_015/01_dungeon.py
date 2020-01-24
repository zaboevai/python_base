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


class Core:

    time_pattern = r'tm\d{1,}'
    exp_pattern = r'exp\d{0,}'

    def __init__(self):
        self.is_end_game = False
        self.is_exit_game = False
        self.is_win_game = False
        self.user_exp = 0

    def get_exp(self, obj):
        exp = re.search(self.exp_pattern, obj)
        return Decimal(exp.group(0)[3:]) if exp else 0

    def get_time(self, obj):
        exp = re.search(self.time_pattern, obj)
        return Decimal(exp.group(0)[2:]) if exp else 0

    def end_game(self, _=None) -> (Decimal, int):
        self.is_end_game = True
        return 0, 0


class Monster(Core):

    def __init__(self, name, is_alive=True):
        super().__init__()
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


class Location(Core):
    patterns = {'cave': r'\w{,8}_\w{0,2}_\w{,2}(\d.\d+)',
                'creature': r'\w{,4}\d{,}_\w{3}\d{,3}_\w{,2}\d+',
                'hatch': r'\w{,5}_\w{,2}(\d.\d+)'}

    def __init__(self, path_map):
        super().__init__()
        self.path_map = path_map
        self.rpg_map = {}

        self.available_location = {}
        self.location_objects = []

        self.current_location = None
        self.object_names = []

        self.available_monsters = {}

    def open_map(self) -> None:
        with open(file=self.path_map, mode='r') as f:
            self.rpg_map = json.load(f)

    @staticmethod
    def _create_monsters(monster_names: list) -> list:
        return [Monster(name=monster_name) for monster_name in monster_names]

    def get_monster_names(self, object_names):
        return [object_name for object_name in object_names if self._identify_object(object_name) == 'creature']

    def create_location_monsters(self, location, monster_names):
        if not self.available_monsters.get(location):
            self.available_monsters = {location: self._create_monsters(monster_names)}

    # @staticmethod
    # def _convert_to_user_choice_format(func):
    #     _list = func()
    #     return {num + 1: {'action_name': record} for num, record in enumerate(_list)} if _list else None

    def get_alive_monster_names(self) -> list:
        return [monster.name for monster in
                self.available_monsters[self.current_location] if monster.is_alive]

    def get_location_names(self) -> list:
        return [location for location in self.object_names if
                self._identify_object(location) in ('cave', 'hatch')]

    def _get_alive_monster_count(self):
        return len([monster.name for monster in
                    self.available_monsters[self.current_location] if monster.is_alive])

    def get_location_monster(self, name):
        for monster in self.available_monsters[self.current_location]:
            if monster.name == name and monster.is_alive:
                return monster

    @staticmethod
    def _get_object_names(objects: list) -> list:
        action_names = []
        for action in objects:
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

    def _identify_object(self, action: str) -> str:
        if not action:
            return ''

        for name, pattern in self.patterns.items():
            res = re.match(pattern, action)
            if res:
                return name
        return ''

    def attack_monster(self, name: str) -> (Decimal, int):
        if not name:
            return 0, 0
        monster = self.get_location_monster(name)
        _time, exp = monster.kill_monster()
        return _time, exp

    def change_location(self, next_location: str) -> (Decimal, int):

        if not next_location:
            return self.end_game()

        for num, available_action in enumerate(self.location_objects):
            if isinstance(available_action, dict) and available_action.get(next_location, None):
                next_location_num = num
                self.rpg_map = self.location_objects[next_location_num]

        _time, exp = self.get_time(next_location), 0
        return _time, exp


class GameDungeon(Location):
    HATCH_EXP_NEEDED = 280
    REMAINING_TIME = '123456.0987654321'

    user_game_actions = {
        1: {'action_name': 'Атаковать монстра',
            'action_targets': Location.get_alive_monster_names,
            'action': Location.attack_monster,
            'action_error_text': 'Монстров не видно !'},

        2: {'action_name': 'Перейти в другую локацию',
            'action_targets': Location.get_location_names,
            'action': Location.change_location,
            'action_error_text': 'Пещер не найдено !'},

        3: {'action_name': 'Сдаться и выйти из игры',
            'action_targets': None,
            'action': Location.end_game,
            'action_error_text': 'Ха ха слабак !'}
    }

    def __init__(self, path_map, user):
        super().__init__(path_map)
        self.user = user
        self.user_choice = None
        self.remaining_time_dec = Decimal(GameDungeon.REMAINING_TIME)
        self.user_total_time = 0

    def show_game_state_info(self) -> None:
        print(f'Вы находитесь в {self.current_location}')
        print(f'У вас {self.user_exp} опыта и осталось {self.remaining_time_dec} секунд до наводнения')
        print(f'Прошло времени: {self.user_total_time}')
        print('')
        print('Внутри Вы видите:')

        [print(f'- {way}') for way in self.object_names]

    def win_game(self, _=None) -> (Decimal, int):
        if self.user_exp >= GameDungeon.HATCH_EXP_NEEDED:
            self.is_win_game = True
        else:
            print('Недостаточно опыта чтобы открыть люк !')
            if self._get_alive_monster_count() == 0:
                self.is_end_game = True

        return 0, 0

    def game_checks(self):

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

            [print(f'{num}. {action.get("action_name")}') for num, action in choice_list.items()]
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

    def user_action(self) -> (Decimal, int):

        action_time, action_exp = 0, 0

        choice = self.ask_user('Выберите действие:', GameDungeon.user_game_actions)

        for num, action in GameDungeon.user_game_actions.items():
            if choice == num:

                action_targets_func = action.get('action_targets', None)
                action_targets = None

                if action_targets_func:
                    action_targets = {num + 1: {'action_name': record} for num, record in enumerate(self.action_targets_func())}

                if not action_targets:
                    print(action.get('action_error_text'))

                user_target_answer = self.ask_user_about_target(action_targets)

                if self._identify_object(user_target_answer) == 'hatch':
                    self.win_game()
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

            if self.is_exit_game:
                print('Спасибо за игру.')
                break

            self.open_map()
            total_time, total_exp = Decimal(), Decimal()

            while True:

                os.system('cls' if os.name == 'nt' else 'clear')

                if not self.game_checks():
                    break

                begin_time = datetime.datetime.now()

                self.prepare_location(self.rpg_map)

                self.show_game_state_info()

                print('')

                action_time, action_exp = self.user_action()

                end_time = datetime.datetime.now()
                delta_time = end_time - begin_time
                delta_time = Decimal(delta_time.seconds + (delta_time.microseconds / 1000000))

                self.remaining_time_dec -= delta_time + action_time
                self.user_total_time += delta_time + action_time
                self.user_exp += action_exp

    def prepare_location(self, game_map):
        self.current_location, self.location_objects = self._parse_map(game_map=game_map)
        self.object_names = self._get_object_names(objects=self.location_objects)
        monster_names = self.get_monster_names(object_names=self.object_names)
        self.create_location_monsters(location=self.current_location, monster_names=monster_names)


# Учитывая время и опыт, не забывайте о точности вычислений!


class User:

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    game_user = User(name='User')
    game = GameDungeon(path_map='rpg.json', user=game_user)
    game.run()
