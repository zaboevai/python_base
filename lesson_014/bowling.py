import logging
from abc import ABC, abstractmethod


class BowlingError(Exception):
    pass


class WrongGameLengthError(BowlingError):
    pass


class MaxFrameError(BowlingError):
    pass


class BowlingGame:

    def __init__(self, game_result, need_log=False):

        if not game_result:
            raise AttributeError('Не указаны результаты игры!')

        self.frame = 1
        self.total_score = 0
        self.throw_score = 0
        self.game_result = game_result
        self.throw = None
        self.need_log = need_log


    def change_throw(self, throw_):
        self.throw = throw_

    def calculate_result(self):

        if self.need_log:
            logging.basicConfig(level=logging.DEBUG, filename='bowling.log')
            logging.info(f' !!! NEW GAME !!!')
            logging.info(f' < {self.game_result} >')

        if len(self.game_result.replace('X', '')) % 2 == 1:
            if self.need_log:
                logging.debug('Ошибка! Введены не полные результаты')
            raise WrongGameLengthError('Введены не полные результаты')

        for throw_symbol in self.game_result:

            if self.frame > 10:
                raise MaxFrameError(f'Превышено кол-во фреймов на символе "{throw_symbol}" !')

            if not self.throw:
                self.change_throw(FirstThrow())

            self.throw_score = self.throw.process(symbol=throw_symbol)
            self.print_frame_results(throw_symbol)

            if isinstance(self.throw, FirstThrow):
                first_hit = self.throw_score
                self.change_throw(SecondThrow())
                if first_hit == 20:
                    self.change_throw(FirstThrow())
                    self.total_score += first_hit
                    self.frame += 1
            else:
                second_hit = self.throw_score
                if second_hit == 15:
                    first_hit = 0
                self.change_throw(FirstThrow())
                self.total_score += (first_hit + second_hit)
                self.frame += 1

        if self.need_log:
            logging.info(f' TOTAL SCORE < {self.total_score} >')
            logging.info(f' !!! END GAME !!!')

        return self.total_score

    def print_frame_results(self, throw_symbol):
        if self.need_log:
            if self.total_score > 0 and isinstance(self.throw, FirstThrow):
                print(f' Итого: {self.total_score}')
                logging.info(f' Итого: {self.total_score}')
            print(f' FRAME_{self.frame} {self.throw} - "{throw_symbol}" -> {self.throw_score}')
            logging.info(f' FRAME_{self.frame} {self.throw} - "{throw_symbol}" -> {self.throw_score}')

    def next(self):
        self.throw.next()


class Throw(ABC):

    def process(self, symbol):

        if symbol == 'X':
            return self.strike()
        elif symbol == '/':
            return self.spare()
        elif symbol == '-':
            return 0
        elif symbol in map(str,(nom for nom in range(1, 10))):
            return int(symbol)
        else:
            raise ValueError(f'Введен неверный символ "{symbol}"')

    @abstractmethod
    def strike(self):
        pass

    @abstractmethod
    def spare(self):
        pass


class FirstThrow(Throw):

    def strike(self):
        return 20

    def spare(self):
        pass

    def __str__(self):
        return self.__class__.__name__


class SecondThrow(Throw):

    def strike(self):
        pass

    def spare(self):
        return 15

    def __str__(self):
        return self.__class__.__name__


if __name__ == '__main__':
    try:
        game = BowlingGame(game_result='1/55X', need_log=False)
        print(game.calculate_result())
    except (BowlingError, BaseException) as exc:
        raise exc
