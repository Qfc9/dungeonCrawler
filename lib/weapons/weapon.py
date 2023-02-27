# basic weapon class, requires name and dmg
class Weapon():
    def __init__(self, name, dmg, durability=10):
        self.durability = durability
        self.dmg = dmg
        self.name = name