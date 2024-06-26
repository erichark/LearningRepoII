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
        self.actions = {"Attack", "Magic"}

    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def take_healing(self, meds):
        self.hp += meds
        if self.hp > self.maxhp:
            self.hp = self.maxhp
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
        i = 0
        print("Actions:")
        for item in self.actions:
            print(str(i+1) + ":", item)
            i += 1

    def choose_magic(self):
        print("Magic:")
        i = 0
        for spell in self.magic:
            print(str(i+1) + ":", spell.name, "(Cost:", str(spell.cost) + ")")
            i += 1

    def enemy_choose_action(self):
        # TODO turn into list comprehension?

        '''[ expression for item in list if conditional ]
        for item in list:
            if conditional:

                expression
        https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
        '''
        number = random.randrange(1,3)
        # first, let's see if enemy has enough magic points to heal and if enemy needs healing.

        # find the highest magic points needed for healing to ensure you can cast it
        mp_needed = 0
        # [mp_needed = spell.cost for spell in self.magic if spell.kind == "white" and spell.cost > mp_needed]
        for spell in self.magic:
            if spell.kind == "white" and spell.cost > mp_needed:
                mp_needed = spell.cost

        # Check if the enemy has enough damage to need healing
        if self.get_hp() < (.33 * self.get_max_hp()) and self.get_mp() > mp_needed:
            action = "white_magic"
            return action
        elif number == 1 and self.get_mp() > 15:
            return "black_magic"
        else:
            action = "physical"
            return action

    def enemy_choose_magic(self, magic_type):

        running = True
        while running:
            spell_index = random.randrange(0,4)
            if self.magic[spell_index].kind == magic_type:
                return spell_index
                running = false
            else:
                continue

"""
    def displayInventory (inventory):
        print("Inventory:")
        totNum = 0
        for item, number in inventory.items():
            print(f"{number}: \t {item}")
            totNum = totNum + number
        print(f"Total Number of Items = {totNum}")


    def addToInventory(inventory, addedItems):

        for item in addedItems:
            inventory.setdefault(item, 0)
            inventory[item] = (inventory[item] + 1)
        return inventory

# TODO - use left and right justify functions to create a pretty printer that prints spells, actions, inventory, etc. 
See Justifying Text with the rjust(), ljust(), and center() Methods https://automatetheboringstuff.com/2e/chapter6/

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

maxLen = 0
for i in range(len(tableData)):
    for t in range(len(tableData[i])):
        if len(tableData[i][t]) > maxLen:
            maxLen = len(tableData[i][t])

print("This is my organized table!")
maxLen = maxLen + 2
for i in range(len(tableData)):
    formattedString = ''
    for t in range(len(tableData[i])):
        formattedString = formattedString + tableData[i][t].ljust(maxLen)
    print(formattedString)
    
    
"""







