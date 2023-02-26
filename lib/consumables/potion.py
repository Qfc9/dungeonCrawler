from lib.consumables.comsumable import Consumable
from lib.hero import Hero

class Potion(Consumable):
    def __init__(self):
        super().__init__("Potion")

        self.heath = 20

    def consume(self, player: Hero):
        player.heal(self.heath)