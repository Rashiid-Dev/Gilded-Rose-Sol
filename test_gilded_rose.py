# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, Generic_depriciate

class GildedRoseTest(unittest.TestCase): 
    def test_name(self):
        items = [Generic_depriciate("Conjured Mana Cake", 3, 6, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)

    def test_quality(self):
        items = [Generic_depriciate("Conjured Mana Cake", 3, 6, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_sell_in(self):
        items = [Generic_depriciate("Conjured Mana Cake", 3, 6, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)

    def test_sellin_day2(self):
        items = [Generic_depriciate("Conjured Mana Cake", 1, 2, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    
    def test_sellin_day3(self):
        items = [Generic_depriciate("Conjured Mana Cake", 0, 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
