import unittest
from bowling import Game, InputValueError, MaxFrameError, StrikeError, SpareError


class BowlingTest(unittest.TestCase):

    def test_check_func_atr_error(self):
        with self.assertRaises(AttributeError):
            game = Game(game_result='')
            result = game.calculate_result()

    def test_check_func_atr2_error(self):
        with self.assertRaises(AttributeError):
            game = Game(game_result='X47')
            result = game.calculate_result()

    def test_check_func_max_frame_error(self):
        with self.assertRaises(MaxFrameError):
            game = Game(game_result='XXXXXXXXXXX')
            result = game.calculate_result()

    def test_check_func_symbols(self):
        with self.assertRaises(InputValueError):
            game = Game(game_result='1s2/')
            result = game.calculate_result()

    def test_check_func_spare_error(self):
        with self.assertRaises(SpareError):
            game = Game(game_result='/1')
            result = game.calculate_result()

    def test_check_func_strike_error(self):
        with self.assertRaises(StrikeError):
            game = Game(game_result='2X')
            result = game.calculate_result()

    def test_functional_game_calc(self):
        game = Game(game_result='X4/34--')
        result = game.calculate_result()
        self.assertEqual(result, 42, 'Не верно производятся расчеты партии !')

    def test_functional_strike(self):
        game = Game(game_result='X')
        result = game.calculate_result()
        self.assertEqual(result, 20, 'Не верно рассчитываются очки за страйк !')

    def test_functional_spare(self):
        game = Game(game_result='4/')
        result = game.calculate_result()
        self.assertEqual(result, 15, 'Не верно рассчитываются очки за спайр !')

    def test_functional_2_miss(self):
        game = Game(game_result='--')
        result = game.calculate_result()
        self.assertEqual(result, 0, 'Не верно рассчитываются очки за 2 миса !')

    def test_functional_2_hit(self):
        game = Game(game_result='12')
        result = game.calculate_result()
        self.assertEqual(result, 3, 'Не верно рассчитываются очки за 2 попадания 2 бросками !')


if __name__ == '__main__':
    unittest.main()