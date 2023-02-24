from lib.mobs.mob import Mob
from lib.weapons.weapon import Weapon

class Goblin(Mob):
    def __init__(self) -> None:
        super().__init__()

        self.dropTable.append(Weapon("Dagger", 2))
        self.dropTable.append(Weapon("Knife", 1))
        self.dropTable.append(Weapon("Machine Gun", 10))
        self.dropTable.append(Weapon("Nuke", 10000000000))

        self.spawnDrops()