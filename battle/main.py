'''
Created on Jan 2, 2018

@author: Eric
'''

from classes.game import Person
from classes.magic import Spell


#instantiate spells
    #Black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 20, 200, "black")
blizzard = Spell("Blizzard", 15, 150, "black")
meteor = Spell("Meteor", 8, 80, "black")
quake = Spell("Quake", 12, 120, "black")

    #white magic
cure = Spell("Cure", 10, 100, "white")
heal = Spell("Heal", 20, 200, "white")


#instantiate people
player = Person(460, 65, 60, 35, [fire, thunder, meteor, quake, cure])
enemy = Person(1000, 65, 25, 35, [])

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
        spell = player.magic[int(index)]
        magic_dmg = spell.generate_magic_damage()
        player_current_mp = player.get_mp()
        
        
        #tests if the player has enough magic points, then applies damage and reduces player magic points
        if player_current_mp >= spell.cost:
            player.reduce_mp(spell.cost)
            dmg = spell.generate_magic_damage()
            if spell.magic_type == "white":
                player.heal(dmg)
                print("You cast", str(spell.name), ". You are healed for", str(dmg)+".")
            elif spell.magic_type == "black":
                enemy.take_damage(dmg)
                print("You cast", str(spell.name), ". You hit the enemy for", str(dmg) + ".")
            
            
            
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
        
        