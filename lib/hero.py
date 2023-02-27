from lib.fightable import Fightable
from lib.inventory import Inventory
from lib.weapons.weapon import Weapon

class Hero(Fightable):
    def __init__(self):
        super().__init__(health=20)

        # creating a inventory for the hero
        self.inventory = Inventory()
        # adding a weapon to the inventory
        self.inventory.add(Weapon("Rusty Sword", 5))
        # retrieving that weapon we just put in
        self.primaryWeapon: Weapon = self.inventory.takeOut(0)

    def switchWeapon(self, inventoryIdx):
        self.inventory.add(self.primaryWeapon)
        self.primaryWeapon = self.inventory.takeOut(inventoryIdx)

    def attack(self):
        if self.primaryWeapon:
            return self.baseAtk + self.primaryWeapon.dmg
        
        return self.baseAtk
    
    def heal(self, healAmount):
        if (self.curHealth + healAmount) > self.maxHealth:
            self.curHealth = self.maxHealth
        else:
            self.curHealth += healAmount