'''
Created on Jan 4, 2018

@author: Eric
'''
import random


class Spell:
    '''
    Class for all magic
    '''


    def __init__(self, name, cost, dmg, magic_type):
        '''
        Constructor
        '''
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.magic_type = magic_type
        
    def generate_magic_damage(self):
        mgl = self.dmg - int((self.dmg *0.1))
        mgh = self.dmg + int((self.dmg *0.1))
        return random.randrange(mgl, mgh)
    

        