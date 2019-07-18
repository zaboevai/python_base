# -*- coding: utf-8 -*-
import unittest

from family import Child, House


class ChildTest(unittest.TestCase):

    def setUp(self):
        self.sweet_home = House()
        self.dasha = Child(name='Даша', house=self.sweet_home)

    def test_sleep(self):
        self.dasha.fullness = 30
        self.dasha.happiness = 100
        self.dasha.sleep()
        self.assertEqual(self.dasha.fullness, 20)
        self.assertEqual(self.dasha.happiness, 100)

    def test_act_full_up(self):
        self.dasha.fullness = 30
        self.dasha.happiness = 100
        self.dasha.act()
        self.assertEqual(self.dasha.fullness, 20)
        self.assertEqual(self.dasha.happiness, 100)

    def test_act_hungry(self):
        self.dasha.fullness = 10
        self.dasha.act()
        self.assertEqual(self.dasha.fullness, 20)


if __name__ == '__main__':
    unittest.main()

