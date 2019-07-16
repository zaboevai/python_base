# -*- coding: utf-8 -*-
import unittest

from family import House, Wife


class WifeTest(unittest.TestCase):

    def setUp(self):
        self.sweet_home = House()
        self.anna = Wife(name='Анна Петровна', house=self.sweet_home)

    def test_act_with_shopping(self):
        self.sweet_home.food = 0
        self.anna.fullness = 30
        self.anna.act()
        self.assertEqual(self.anna.fullness, 20)
        self.assertEqual(self.sweet_home.food, 100)

    def test_act_with_buy_fur_coat(self):
        self.sweet_home.food = 100
        self.sweet_home.dirt = 0
        self.sweet_home.money = 1000
        self.anna.happiness = 10
        self.anna.act()
        self.assertEqual(self.anna.fullness, 20)
        self.assertEqual(self.anna.happiness, 70)
        self.assertEqual(self.sweet_home.money, 650)


if __name__ == '__main__':
    unittest.main()

