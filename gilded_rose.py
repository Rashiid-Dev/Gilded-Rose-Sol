# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            item.update()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Generic_depriciate(Item):
    def __init__(self, name, sell_in, quality, degrading_value=1):
        super().__init__(name, sell_in, quality)
        self.degrading_value = degrading_value

    def update(self):
        self.sell_in -= 1

        if self.sell_in < 0:
            self.quality -= 2 * self.degrading_value
        else:
             self.quality -= 1 * self.degrading_value
        if self.quality < 0:
            self.quality = 0

class Cheese_appriciate(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in -= 1

        if self.sell_in < 0:
            self.quality += 2 
        else:
             self.quality += 1 
        
        if self.quality >= 50:
            self.quality = 50

class Pass_appriciate(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.sell_in -= 1

        if self.sell_in >= 10:
            self.quality += 1
        elif self.sell_in < 10 and self.sell_in >= 5:
            self.quality += 2
        elif self.sell_in <= 5 and self.sell_in >= 0:
            self.quality += 3
        elif self.sell_in < 0:
            self.quality = 0
        
        if self.quality > 50:
            self.quality = 50

class Fixed(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update(self):
        pass