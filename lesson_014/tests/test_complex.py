import unittest
from bowling import CalculateResult, WrongGameLengthError, BowlingError


class BowlingTest(unittest.TestCase):

    def test_check_func_symbols(self):
        try:
            calculate = CalculateResult(game_result='1s2/')
            result = calculate.run()
        except ValueError as exc:
            self.assertEqual(exc.__class__, ValueError, 'Проверка на допустимые символы не работает !!!')  # TODO  посмотрите на self.assertRaises()

    def test_check_func_length(self):
        try:
            calculate = CalculateResult(game_result='132')
            result = calculate.run()
        except WrongGameLengthError as exc:
            self.assertEqual(exc.__class__, WrongGameLengthError, 'Проверка на полноту результатов не работает !!!')

    def test_functional_geme_calc(self):
        calculate = CalculateResult(game_result='X4/34--')
        result = calculate.run()
        self.assertEqual(result, 42, 'Не верно производятся расчеты партии !')

    def test_functional_strike(self):
        calculate = CalculateResult(game_result='X')
        result = calculate.run()
        self.assertEqual(result, 20, 'Не верно рассчитываются очки за страйк !')

    def test_functional_spair(self):
        calculate = CalculateResult(game_result='4/')
        result = calculate.run()
        self.assertEqual(result, 15, 'Не верно рассчитываются очки за спайр !')

    def test_functional_2_miss(self):
        calculate = CalculateResult(game_result='--')
        result = calculate.run()
        self.assertEqual(result, 0, 'Не верно рассчитываются очки за 2 миса !')

    def test_functional_2_hit(self):
        calculate = CalculateResult(game_result='12')
        result = calculate.run()
        self.assertEqual(result, 3, 'Не верно рассчитываются очки за 2 попадания 2 бросками !')


if __name__ == '__main__':
    unittest.main()