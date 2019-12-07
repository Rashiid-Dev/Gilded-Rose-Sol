# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase): 
    def test_name(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)

    def test_quality(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_sell_in(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
