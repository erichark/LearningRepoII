'''
Created on Jan 2, 2018

@author: Eric
'''

from classes.game import Person


magic = [{"name": "Fire", "cost": 10, "dmg": 60}, 
         {"name": "Thunder", "cost": 15, "dmg": 80},
         {"name": "Ice", "cost": 10, "dmg": 60},
         {"name": "Snakes", "cost": 5, "dmg": 30},
         {"name": "Prismatic", "cost": 20, "dmg": 100},
         ]

player = Person(460, 65, 60, 35, magic)
enemy = Person(1000, 65, 25, 35, magic)

print("An Enemy Attacks!!!")
print ("=======================")

running = True
#starts the battle
while running:
    player.get_action()
    choice = input("What would you like to do?")
    index = int(choice) - 1
    #if the player chooses to attack, calcs damage and applies to enemy
    if index == 0:
        dmg = int(player.generate_damage())
        enemy.take_damage(dmg)
        print("You hit the enemy for" , str(dmg) + ".")
    #if the player chooses magic, prints magic list and allows player to select
    elif index == 1:
        player.get_magic()
        magic_choice = input("\nSelect a spell:")
        index = int(magic_choice) - 1
        
        cost = player.get_magic_cost(index)
        spell = player.get_magic_name(index)
        player_current_mp = player.get_mp()
        #tests if the player has enough magic points, then applies damage and reduces player magic points
        if player_current_mp >= cost:
            player.reduce_mp(cost)
            dmg = player.generate_magic_damage(index)
            enemy.take_damage(dmg)
            print("You cast", spell, ". You hit the enemy for", str(dmg) + ".")
            
        else:
            print("You don't have enough magic points!")
            continue
        
    #enemy attack and reduce player hit points
    enemy_choice = 1
    dmg = int(enemy.generate_damage())
    player.take_damage(dmg)
    print("The enemy hits you for", str(dmg) + ".")
    
    #print current stats and max stats
    print("\n=========================================")
    print("Enemy HP:", str(enemy.get_hp()) + "/"+ str(enemy.get_max_hp()))
    print("_________________________________________")
    print("Player HP:", str(player.get_hp()) + "/"+ str(player.get_max_hp()))
    print("Player MP:", str(player.get_mp()) + "/"+ str(player.get_max_mp()))
    print("=========================================")
    
    #when anyone's hitpoints get to 0, the other wins and program exits
    if enemy.get_hp() == 0:
        print("You won!")
        running = False
    elif player.get_hp() == 0:
        print("The enemy defeated you!")
        running = False
        
        