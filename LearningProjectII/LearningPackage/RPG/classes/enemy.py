'''
Created on Jan 2, 2018

@author: Eric
'''

class Enemy2:
    '''
    classdocs
    '''

    def __init__(self, hp, mp):
        '''
        Constructor
        '''
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        
    def get_hp(self):
        return(self.hp)
    
    