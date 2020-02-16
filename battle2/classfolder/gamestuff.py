'''

    Python RPG
    November 25, 2019
    Second RPG game

Utility and Person Classes file
'''

import random
from magic import Spell


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.df = df
        self.magic = magic
        self.actions = {"Magic", "Attack"}

    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("Actions:")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        print("Magic:")
        i = 0
        for spell in self.magic:
            print(str(i) + ":", spell.name, "(Cost:", str(spell.cost) + ")")
            i+=1













