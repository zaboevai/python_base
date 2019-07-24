class WrongGameLengthError(Exception):
    pass


class MaxFrameError(Exception):
    pass


class CalculateResult:

    def __init__(self, game_result):
        self.frame = 1
        self.total_score = 0
        self.game_result = game_result
        self.state = None
        if len(self.game_result.replace('X', '')) % 2 == 1:
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

    def next(self):
        self.state.next()


class State:
    first_strike_score = 0
    second_strike_score = 0

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
        if MAX_FRAME < self.calculate.frame:
            raise MaxFrameError('Превышено кол-во фреймов')
        elif self.calculate.hit_score not in ('X', '/', '-') and not self.calculate.hit_score.isdigit():
            raise ValueError(
                f'Ошибка! Введен неверный символ <{self.calculate.hit_score}>. (допустимы только "цифры, X, /, -")')

        return True


class FirstHit(State):

    def next(self):
        self.calculate.change_state(NeedCheck())
        self.calculate.state.next()

        if isinstance(self.calculate.state, NeedCheck):
            print('FRAME=', self.calculate.frame)
            self.calculate.change_state(FirstHit())
            State.first_strike_score = 0
            if self.calculate.hit_score == 'X':
                State.first_strike_score = 20
                self.calculate.frame += 1
                self.calculate.total_score += State.first_strike_score
            elif self.calculate.hit_score.isdigit():
                State.first_strike_score = int(self.calculate.hit_score)
                self.calculate.change_state(SecondHit())
            elif self.calculate.hit_score == '-':
                self.calculate.change_state(SecondHit())

            print('\t first_strike_score=', State.first_strike_score)
            print('\t TOTAL=', self.calculate.total_score)

            return True


class SecondHit(State):

    def next(self):
        self.calculate.change_state(NeedCheck())
        self.calculate.state.next()

        if isinstance(self.calculate.state, NeedCheck):
            self.calculate.change_state(SecondHit())
            State.second_strike_score = 0
            if self.calculate.hit_score == '/':
                State.first_strike_score = 0
                State.second_strike_score = 15
            elif self.calculate.hit_score.isdigit():
                State.second_strike_score = int(self.calculate.hit_score)
            elif self.calculate.hit_score == '-':
                State.second_strike_score = 0

            self.calculate.total_score += State.first_strike_score
            self.calculate.total_score += State.second_strike_score
            self.calculate.frame += 1
            self.calculate.change_state(FirstHit())

            print('\t second_strike_score=', State.second_strike_score)

            print('\t TOTAL=', self.calculate.total_score)

            return True


if __name__ == '__main__':
    calc = CalculateResult(game_result='---XX/45892/')
    calc.run()
