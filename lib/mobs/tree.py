from lib.mobs.mob import Mob
from lib.weapons.weapon import Weapon

# New tree boss
class TreeBoss(Mob):
    # allowing for a name to be set, but the default name is Cedar
    def __init__(self, name="Cedar") -> None:
        # Passing the name and the health to the parent class Mob
        super().__init__(name=name, health=50)

        # Adding custom weapons to the drop table
        self.dropTable.append(Weapon("Tree Branch", 10))
        self.dropTable.append(Weapon("Leaf", -1))

        self.spawnDrops()

class SunBoss(Mob):
    def __init__(self, name="Scorch"):
        super().__init__(name=name, health=60)

        self.dropTable.append(Weapon("Solar flare", 100))
        self.dropTable.append(Weapon("Skin cancer", -10))
       

        self.spawnDrops()

class MoonBoss(Mob):
    def __init__(self, name="Dark Death"):
        super().__init__(name=name, health=70)

        self.dropTable.append(Weapon("Iron sword", 50))
        self.dropTable.append(Weapon("Titanium", 70))
       

        self.spawnDrops()