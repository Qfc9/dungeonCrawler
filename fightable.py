class Fightable():
    def __init__(self, health=10):
        self.maxHealth = health
        self.curHealth = self.maxHealth

        self.baseDef = 1
        self.baseAtk = 5

    def attack(self):
        return self.baseAtk
    
    def takeDmg(self, damage):
        self.curHealth -= damage

    def isAlive(self):
        if self.curHealth <= 0:
            return False

        return True

# Handling inventories
class Inventory():
    def __init__(self):
        self.contains = []

    # add an item to the self.contains list
    def add(self, newItem):
        if newItem is None:
            return
        self.contains.append(newItem)

    # remove and return item in the self.contains list
    def takeOut(self, idx):
        return self.contains.pop(idx)

# basic weapon class, requires name and dmg
class Weapon():
    def __init__(self, name, dmg, durability=10):
        self.durability = durability
        self.dmg = dmg
        self.name = name

class Hero(Fightable):
    def __init__(self):
        super().__init__(health=20)

        # creating a inventory for the hero
        self.inventory = Inventory()
        # adding a weapon to the inventory
        self.inventory.add(Weapon("Rusty Sword", 5))
        # retrieving that weapon we just put in
        self.primaryWeapon: Weapon = self.inventory.takeOut(0)

    def attack(self):
        if self.primaryWeapon:
            return self.baseAtk + self.primaryWeapon.dmg
        
        return self.baseAtk
    

class Mob(Fightable):
    def __init__(self):
        super().__init__()
        self.inventory = Inventory()
