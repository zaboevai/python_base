import unittest

from bowling import check_game_result, get_score, WrongSymbolsError, WrongGameLengthError


class BowlingTest(unittest.TestCase):

    def test_check_func_symbols(self):
        try:
            result = check_game_result(game_result='123/а')
        except WrongSymbolsError as exc:
            self.assertEqual(exc.__class__, WrongSymbolsError, 'Проверка на допустимые символы не работает !!!')

    def test_check_func_length(self):
        try:
            result = check_game_result(game_result='132')
        except WrongGameLengthError as exc:
            self.assertEqual(exc.__class__, WrongGameLengthError, 'Проверка на полноту результатов не работает !!!')

    def test_functional_geme_calc(self):
        result = get_score(game_result='Х4/34--')
        self.assertEqual(result, 42, 'Не верно производятся расчеты партии !')

    def test_functional_strike(self):
        result = get_score(game_result='Х')
        self.assertEqual(result, 20, 'Не верно рассчитываются очки за страйк !')

    def test_functional_spair(self):
        result = get_score(game_result='4/')
        self.assertEqual(result, 15, 'Не верно рассчитываются очки за спайр !')

    def test_functional_2_miss(self):
        result = get_score(game_result='--')
        self.assertEqual(result, 0, 'Не верно рассчитываются очки за 2 миса !')

    def test_functional_2_hit(self):
        result = get_score(game_result='12')
        self.assertEqual(result, 3, 'Не верно рассчитываются очки за 2 попадания 2 бросками !')

if __name__ == '__main__':
    unittest.main()