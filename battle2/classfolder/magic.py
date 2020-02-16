"""

    Python RPG
    November 25, 2019
    Second RPG game

Magic Classes file
"""
import random


class Spell:
    def __init__(self, name, cost, dmg, kind):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.kind = kind

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)






