'''
Created on Jan 2, 2018

@author: Eric
'''

from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

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

#instantiate items
potion_clw = Item("CLW Potion", "potion", "A potion to heal 50 HP", 50)
potion_csw = Item("CSW Potion", "potion", "A potion to heal 100 HP", 100)
potion_heal = Item("Heal Potion", "potion", "A potion to Heal the player for 200 HP", 200)
potion_restore = Item("Restore Player Potion", "elixer", "A potion to restore the player of all HP and MP", 9999)
potion_restoreParty = Item("Restore Party Potion", "elixer", "A potion to restore the party of all HP and MP", 9999)

grenade = Item("Holy Hand Grenade", "weapon", "A Holy Hand Grenade, doing 200 damage", 200)


spells = [fire, thunder, meteor, quake, cure]
items = [{"item": potion_clw, "quantity" : 10}, {"item": potion_csw, "quantity": 5}, {"item": grenade, "quantity": 1}]

#instantiate people
player1 = Person("Blix", 460, 65, 60, 35, spells, items)
player2 = Person("Dave", 460, 65, 60, 35, spells, items)
player3 = Person("Bill", 460, 65, 60, 35, spells, items)

enemy = Person("Enemy", 1000, 65, 25, 35, [], [])

players = [player1, player2, player3]

print(bcolors.BOLD + bcolors.OKGREEN +"Welcome to Underworld"+bcolors.ENDC)

print(bcolors.BOLD + bcolors.FAIL+"An Enemy Attacks!!!"+bcolors.ENDC)
print ("=======================")

running = True
#starts the battle
while running:
    #Print stats for all PCs
    print ("\n\n")
    print("NAME           HP                                  MP")
    for player in players:
        player.get_stats()
     
    
    #start the battle   
    for player in players:
        player.get_action()
        choice = input("What would you like to do?")
        index = int(choice) - 1
        #if the player chooses to attack, calcs damage and applies to enemy
        if index == 0:
            dmg = int(player.generate_damage())
            enemy.take_damage(dmg)
            print(bcolors.OKBLUE+"You hit the enemy for" , str(dmg) + "." + bcolors.ENDC)
        #if the player chooses magic, prints magic list and allows player to select
        elif index == 1:
            player.get_magic()
            magic_choice = input("\n    Select a spell:")
            index = int(magic_choice) - 1
            if index == -1:
                continue
            spell = player.magic[int(index)]
            magic_dmg = spell.generate_magic_damage()
            player_current_mp = player.get_mp()
            
            
            #tests if the player has enough magic points, then applies damage and reduces player magic points
            if player_current_mp >= spell.cost:
                player.reduce_mp(spell.cost)
                dmg = spell.generate_magic_damage()
                if spell.magic_type == "white":
                    player.heal(dmg)
                    print(bcolors.OKGREEN + "    You cast", str(spell.name), ". You are healed for", str(dmg)+"." + bcolors.ENDC)
                elif spell.magic_type == "black":
                    enemy.take_damage(dmg)
                    print(bcolors.OKBLUE + "    You cast", str(spell.name), ". You hit the enemy for", str(dmg) + "." + bcolors.ENDC)
                
                
                
            else:
                print(bcolors.BOLD + bcolors.FAIL  + "You don't have enough magic points!" + bcolors.ENDC)
                continue
         
        elif index==2:
            player.get_items()
            item_choice = input("\n    Select an Item:")
            index = int(item_choice) - 1
            if index == -1:
                continue
            item = player.items[int(index)]["item"]
            if player.items[int(index)]["quantity"] > 0:
                if item.kind == "potion":
                    player.heal(item.prop)
                    player.items[int(index)]["quantity"] -= 1
                    print(bcolors.OKGREEN + "    You used a", item.name, "You are healed for", str(item.prop), "HP." + bcolors.ENDC)
                elif item.kind == "elixer":
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    player.items[int(index)]["quantity"] -= 1
                    print(bcolors.OKGREEN + "    You used a", item.name, "Your HP and MP are restored." + bcolors.ENDC)
                elif item.kind == "weapon":
                    dmg = item.prop
                    enemy.take_damage(dmg)
                    player.items[int(index)]["quantity"] -= 1
                    print(bcolors.BOLD + bcolors.OKGREEN + "    You hit the enemy with", item.name, "for", str(item.prop), "damage." + bcolors.ENDC)
            else:
                print(bcolors.BOLD + bcolors.FAIL + "    You don't have any of that item left!!" + bcolors.ENDC)
                continue
         
        
    #enemy attack and reduce player hit points
    enemy_choice = 1
    dmg = int(enemy.generate_damage())
    player.take_damage(dmg)
    print(bcolors.BOLD + bcolors.FAIL + "The enemy hits you for", str(dmg) + "." + bcolors.ENDC)
    
    
    #when anyone's hitpoints get to 0, the other wins and program exits
    if enemy.get_hp() == 0:
        print(bcolors.BOLD + bcolors.OKGREEN + "You won!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "The enemy defeated you!" + bcolors.ENDC)
        running = False
        
        