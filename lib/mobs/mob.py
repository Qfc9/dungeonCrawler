from lib.fightable import Fightable
from lib.inventory import Inventory
from lib.weapons.weapon import Weapon
import random

class Mob(Fightable):
    def __init__(self, name="I need a name", health=10):
        super().__init__(health=health)
        self.name = name

        self.inventory = Inventory()
        self.inventory.add(Weapon("Rusty Sword", 5))

        self.dropTable = []

    # will choose an item from the drop table at random to add
    # to the inventory
    def spawnDrops(self):
        # Chooses a random item from the drop table
        itemIdx = random.randint(0, len(self.dropTable) - 1)

        # Adds the item chosen to the inventory
        self.inventory.add(self.dropTable[itemIdx])
