# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    print("OMGHAI!")
    items = [
        Generic_depriciate(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Cheese_appriciate(name="Aged Brie", sell_in=2, quality=0),
        Generic_depriciate(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Fixed(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Fixed(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Pass_appriciate(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Pass_appriciate(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Pass_appriciate(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Generic_depriciate(name="Conjured Mana Cake", sell_in=3, quality=6, degrading_value=2),  # <-- :O
    ]

    days = 30
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
