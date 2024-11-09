import numpy as np
class Creature():
    def setStats(self, rawStats):
        stats = {
            "str": rawStats[0], 
            "dex" : rawStats[1], 
            "con" : rawStats[2], 
            "int" : rawStats[3], 
            "wis" : rawStats[4], 
            "cha" : rawStats[5]}
        modifier = {}
        for key in stats.keys():
            modifier[key] = (stats.get(key) - 10) // 2
        return stats, modifier
    
    def setSavingThrows(self, proficiencies):
        savingThrows = {}
        for key in self.stats.keys():
            savingThrows[key] = (self.stats.get(key) - 10) // 2
            for x in proficiencies:
                if x == key:
                    savingThrows[key] += self.proficiencyBonus
        return savingThrows
    
    def setSkills(self, proficiencies):
        skillsDir = {
            "str" : ["athletics"],
            "dex" : ["acrobatics", "sleight of hand", "stealth"],
            "wis" : ["animal handling", "insight", "medicine", "perception", "survival"],
            "int" : ["arcana", "history", "investigation", "nature", "religion"],
            "cha" : ["deception", "intimidation", "performance","persuasion"]
        }
        skills = {}
        for statType in skillsDir.keys():
            for skill in skillsDir.get(statType):
                skills[skill] = self.bonus[statType]
                for proficiency in proficiencies:
                    if skill == proficiency:
                        skills[skill] += self.proficiencyBonus
        return skills

    def setPassivePerception(self):
        return 10 + self.bonus["wis"] + self.proficiencyBonus

    def __init__(self, name, proficiencyBonus, armorClass, hitPoints, stats, skillProficiency = [], savingThrowProficiency = []):
        self.armorClass = armorClass
        self.name = name
        self.hitPoints = hitPoints
        self.proficiencyBonus = proficiencyBonus
        self.stats, self.modifier = self.setStats(stats)
        self.savingThrows = self.setSavingThrows(savingThrowProficiency)
        self.skills = self.setSkills(skillProficiency)
        self.passivePerception = self.setPassivePerception()

JoeBiden = Creature("Joe Biden", 3, 15, 2000, [12,13,5,9, 20,16], savingThrowProficiency=["str", "con"], skillProficiency = ["sleight of hand", "insight"])

print(JoeBiden.skills)