from lib.mobs.mob import Mob
from lib.weapons.weapon import Weapon
from lib.consumables.potion import Potion

class Goblin(Mob):
    def __init__(self, name="Goblin") -> None:
        super().__init__(name)

        # Adding custom weapons to the drop table
        self.dropTable.append(Weapon("Dagger", 10))
        # self.dropTable.append(Weapon("Knife", 1))
        # self.dropTable.append(Weapon("Machine Gun", 10))
        # self.dropTable.append(Weapon("Nuke", 10000000000))
        self.dropTable.append(Potion())

        self.spawnDrops()