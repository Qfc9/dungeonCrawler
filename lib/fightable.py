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

    