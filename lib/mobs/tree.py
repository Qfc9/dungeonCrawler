from lib.mobs.mob import Mob
from lib.weapons.weapon import Weapon

class TreeBoss(Mob):
    def __init__(self, name="Cedar") -> None:
        super().__init__(name=name, health=50)

        # Adding custom weapons to the drop table
        self.dropTable.append(Weapon("Tree Branch", 10))
        self.dropTable.append(Weapon("Leaf", -1))

        self.spawnDrops()