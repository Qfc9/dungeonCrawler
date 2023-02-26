from lib.fightable import Fightable
from lib.inventory import Inventory
from lib.weapons.weapon import Weapon
import random

class Mob(Fightable):
    # Allowing for a name and health to be set, the defaults are 
    # I need a name, and 50
    def __init__(self, name="I need a name", health=10):
        # Passing the health value to the parent class, Fightable
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
