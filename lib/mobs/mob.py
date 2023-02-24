from lib.fightable import Fightable
from lib.inventory import Inventory
from lib.weapons.weapon import Weapon
import random

class Mob(Fightable):
    def __init__(self):
        super().__init__()
        self.inventory = Inventory()
        self.inventory.add(Weapon("Rusty Sword", 5))

        self.dropTable = []

    def spawnDrops(self):
        itemIdx = random.randint(0, len(self.dropTable))

        self.inventory.add(self.dropTable[itemIdx])
