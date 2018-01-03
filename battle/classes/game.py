'''
Created on Jan 2, 2018

@author: Eric
'''

import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]
        
    def generate_damage(self):
        return(random.randrange(self.atkl, self.atkh))
    
    def generate_magic_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5 
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)
    
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
        
    def get_magic_cost(self, i):
        return self.magic[i] ["cost"]
        
    def get_magic_name(self, i):
        return self.magic[i] ["name"]
    
    def get_action(self):
        i=1
        print("Actions:")
        for item in self.actions:
            print(str(i), ":", item)
            i+= 1
        
    def get_magic(self):   
        i=1
        print("Spells:")
        for spell in self.magic:
            print(str(i), ":", str(spell["name"]), "(cost", str(spell["cost"]) + ")")
            i+= 1
            
    
            