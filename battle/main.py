'''
Created on Jan 2, 2018

@author: Eric
'''

from classes.game import Person, bcolors


magic = [{"name": "Fire", "cost": 10, "dmg": 60}, 
         {"name": "Thunder", "cost": 15, "dmg": 80},
         {"name": "Ice", "cost": 10, "dmg": 60},
         {"name": "Snakes", "cost": 5, "dmg": 30},
         {"name": "Prismatic", "cost": 20, "dmg": 100},
         ]

player = Person(460, 65, 60, 35, magic)
enemy = Person(1000, 65, 25, 35, magic)

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!!!" + bcolors.ENDC)
print ("=======================")

running = True

while running:
    player.get_action()
    choice = input("What would you like to do?")
    index = int(choice) - 1
    if index == 0:
        dmg = int(player.generate_damage())
        enemy.take_damage(dmg)
        print("You hit the enemy for" , str(dmg) + ". Enemy HP =" , enemy.get_hp())
        
    enemy_choice = 1
    dmg = int(enemy.generate_damage())
    player.take_damage(dmg)
    print("The enemy hits you for", str(dmg) + ". Your HP = ", player.get_hp())
    
    
        