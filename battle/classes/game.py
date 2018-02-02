'''
Created on Jan 2, 2018

@author: Eric
'''

import random
from classes.magic import Spell


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Item"]
        self.items = items
        self.name = name
        
    def generate_damage(self):
        return(random.randrange(self.atkl, self.atkh))
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self,dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
            
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
          
    def get_action(self):
        i=1
        print("\n\n" + self.name + "'s Turn!!")
        print("Actions:")
        for item in self.actions:
            print(str(i), ":", item)
            i+= 1
    def choose_target(self, enemies):
        i=1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "        Target:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() > 0:
                print("        " + str(i) + ":" + enemy.name)
                i+= 1
        choice = int(input("    Choose Target:")) - 1 
        return choice
    
        
    def get_magic(self):   
        i=1
        print("\nSpells:")
        print("    0: Return to previous menu")
        for spell in self.magic:
            print("    " + str(i), ":", spell.name, "(cost", str(spell.cost) + ")")
            i+= 1
    
    def get_items(self):   
        i=1
        print("\nItems:")
        print("    0: Return to previous menu")
        for item in self.items:
            print("    " + str(i), ":", item["item"].name, "(desc: ", str(item["item"].description) + ") quantity:", str(item["quantity"]))
            i+= 1   
        
    def get_stats(self):
        hp_ticks = (self.hp / self.maxhp) * 100 / 4
        hp_bar=""
        
        
        while hp_ticks > 0:
            hp_bar+= "X"
            hp_ticks -= 1
        while len(hp_bar)< 25:
            hp_bar+=" "
        
        mp_ticks = (self.mp / self.maxmp) * 100 / 10
        mp_bar=""
        
        while mp_ticks > 0:
            mp_bar+= "X"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar+=" "
            
        hp_len = len(str(self.hp) + "/" + str(self.maxhp))
        
        hp_padding = ""
        
        while hp_len<7:
            hp_padding +=" "
            hp_len +=1
            
            
        formatted_hp = hp_padding + str(self.hp) + "/" + str(self.maxhp)
        
        mp_len = len(str(self.mp) + "/" + str(self.maxmp))
        mp_padding = ""
        
        while mp_len<5:
            mp_padding +=" "
            mp_len +=1
            
            
        formatted_mp = mp_padding + str(self.mp) + "/" + str(self.maxmp)   

        print("                   _________________________              __________")
        print(bcolors.OKBLUE + self.name + "      " +  bcolors.OKGREEN + formatted_hp + bcolors.ENDC +  " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|      " + formatted_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")       
    
      
      
    def get_enemy_stats(self):
        hp_ticks = (self.hp / self.maxhp) * 100 / 4
        hp_bar=""
        
        
        while hp_ticks > 0:
            hp_bar+= "X"
            hp_ticks -= 1
        while len(hp_bar)< 25:
            hp_bar+=" "
        
        mp_ticks = (self.mp / self.maxmp) * 100 / 10
        mp_bar=""
        
        while mp_ticks > 0:
            mp_bar+= "X"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar+=" "
            
        hp_len = len(str(self.hp) + "/" + str(self.maxhp))
        
        hp_padding = ""
        
        while hp_len<9:
            hp_padding +=" "
            hp_len +=1
            
            
        formatted_hp = hp_padding + str(self.hp) + "/" + str(self.maxhp)
        
        mp_len = len(str(self.mp) + "/" + str(self.maxmp))
        mp_padding = ""
        
        while mp_len<5:
            mp_padding +=" "
            mp_len +=1
            
            
        formatted_mp = mp_padding + str(self.mp) + "/" + str(self.maxmp)   

        print("                   _________________________              __________")
        print(bcolors.WARNING + self.name + "   " + bcolors.OKGREEN + formatted_hp + bcolors.ENDC +  " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|      " + formatted_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")       
    
        
        
    def choose_enemy_spell(self):
            magic_choice = random.randrange(0 , len(self.magic))
            chosen_spell = self.magic[magic_choice]
            magic_dmg = chosen_spell.generate_damage() 
            

            if self.mp > chosen_spell.cost:
                self.choose_enemy_spell()
            else:
                return chosen_spell, magic_dmg
                    
                    
                    
                    