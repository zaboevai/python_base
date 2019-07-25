import logging


class BowlingError(Exception):
    pass


class WrongGameLengthError(BowlingError):
    pass


class MaxFrameError(BowlingError):
    pass


class CalculateResult:

    def __init__(self, game_result, need_log=False):

        if not game_result:
            raise AttributeError('Не указаны результаты игры!')

        self.frame = 1
        self.total_score = 0
        self.game_result = game_result
        self.state = None
        self.need_log = need_log

        if need_log:
            logging.basicConfig(level=logging.DEBUG, filename='bowling.log')
            logging.info(f' !!! NEW GAME !!! results < {self.game_result} >')

        if len(self.game_result.replace('X', '')) % 2 == 1:  # TODO по условию геймов должно быть ровно 10
            if need_log:
                logging.debug('Ошибка! Введены не полные результаты')
            raise WrongGameLengthError('Введены не полные результаты')

    def change_state(self, state_):
        self.state = state_
        self.state.calculate = self

    def run(self):
        for hit_score in self.game_result:
            self.hit_score = hit_score

            if not self.state:
                self.change_state(FirstHit())

            self.state.next()
        if self.need_log:
            logging.info(f' !!! END GAME !!! TOTAL SCORE < {self.total_score} >')
        return self.total_score

    def next(self):
        self.state.next()


class State:
    first_hit_score = 0
    second_hit_score = 0
    HIT = 'HIT'
    MISS = 'MISS'
    SPARE = 'SPARE'
    STRIKE = 'STRIKE'

    @property
    def calculate(self):
        return self._calculate

    @calculate.setter
    def calculate(self, calculate):
        self._calculate = calculate

    def next(self):
        pass


class NeedCheck(State):

    def next(self):

        MAX_FRAME = 10
        if MAX_FRAME < self.calculate.frame:  # TODO по условию геймов должно быть ровно 10
            if self.calculate.need_log:
                logging.debug('Ошибка! Превышено кол-во фреймов')
            raise MaxFrameError('Превышено кол-во фреймов')

        elif self.calculate.hit_score not in ('X', '/', '-') and not self.calculate.hit_score.isdigit():
            if self.calculate.need_log:
                logging.debug(
                    f'Ошибка! Введен неверный символ <{self.calculate.hit_score}>. (допустимы только "цифры, X, /, -")')
            raise ValueError(
                f'Ошибка! Введен неверный символ <{self.calculate.hit_score}>. (допустимы только "цифры, X, /, -")')
        return


class FirstHit(State):

    def next(self):
        self.calculate.change_state(NeedCheck())
        self.calculate.state.next()

        if isinstance(self.calculate.state, NeedCheck):

            if self.calculate.need_log:
                logging.info(f' FRAME_{self.calculate.frame}')

            self.calculate.change_state(FirstHit())
            State.first_hit_score = 0

            if self.calculate.hit_score == 'X':
                State.first_hit_score = 20
                self.calculate.total_score += State.first_hit_score
                if self.calculate.need_log:
                    logging.info(f'\t first  hit -> {State.STRIKE} - {State.first_hit_score}')
                    logging.info(f' FRAME_{self.calculate.frame} SCORE -> {self.calculate.total_score}')
                self.calculate.frame += 1

            elif self.calculate.hit_score.isdigit():
                State.first_hit_score = int(self.calculate.hit_score)
                self.calculate.change_state(SecondHit())
                if self.calculate.need_log:
                    logging.info(f'\t first  hit -> {State.HIT} - {State.first_hit_score}')

            elif self.calculate.hit_score == '-':
                self.calculate.change_state(SecondHit())
                if self.calculate.need_log:
                    logging.info(f'\t first  hit -> {State.MISS} - {State.first_hit_score}')

            return


class SecondHit(State):

    def next(self):
        self.calculate.change_state(NeedCheck())
        self.calculate.state.next()

        if isinstance(self.calculate.state, NeedCheck):

            self.calculate.change_state(SecondHit())
            State.second_hit_score = 0

            if self.calculate.hit_score == '/':
                State.first_hit_score = 0
                State.second_hit_score = 15
                if self.calculate.need_log:
                    logging.info(f'\t second hit -> {State.SPARE} - {State.second_hit_score}')

            elif self.calculate.hit_score.isdigit():
                State.second_hit_score = int(self.calculate.hit_score)
                if self.calculate.need_log:
                    logging.info(f'\t second hit -> {State.HIT} - {State.second_hit_score}')

            elif self.calculate.hit_score == '-':
                State.second_hit_score = 0
                if self.calculate.need_log:
                    logging.info(f'\t second hit -> {State.MISS} - {State.second_hit_score}')

            self.calculate.total_score += State.first_hit_score
            self.calculate.total_score += State.second_hit_score

            if self.calculate.need_log:
                logging.info(f' FRAME_{self.calculate.frame} SCORE -> {self.calculate.total_score}')

            self.calculate.frame += 1
            self.calculate.change_state(FirstHit())

            return

# TODO логика получилась слишком сложной и избыточной, Предлагаю пойти след путем:
#  Основной класс игры который посимвольно обходит сроку с результатом и отдает текущий символ текущему броску
#  для посчета очков по символу. Базовый класс бросок. В нем шаблоный метод который принимает символ,
#  сравнивает с возможными "-.*1-9" и вызывает обработчик соответсвующего символа.
#  Конретные обработчики реализованы в наследниках - первый или второй бросок.
#  Основной класс игры получив очки по символу - решает в какое бросок переключаться и посчитывает кол-во фреймов и общую сумму.
#  Ну и не забываем остальные проверки, которые нужны по условию.
#  Если необходимо в основном классе игры можно запоминать предыдущее значение очков.


if __name__ == '__main__':
    try:
        calc = CalculateResult(game_result='X4/34--', need_log=False)
        print(calc.run())
    except (BowlingError, BaseException) as exc:
        raise exc
