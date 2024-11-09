import numpy as np
import dice

class Weapon():
    def __init__(self, name, dmg, dmgType, range, weight = 0, cost = 0, thrown = False, proficiency = "simple"):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.dmgType = dmgType
        self.weight = weight
        self.range = range
        self.thrown = thrown
        self.proficiency = proficiency

    def dealDmg(self):
        result = 0
        for i in range(0, self.dmg[0]):
            result += dice.d(self.dmg[1])
        return result

class FirearmWeapon(Weapon):
    pass
