'''

    Python RPG
    November 25, 2019
    Second RPG game

'''

from classfolder.gamestuff import Person, bcolors
import random


magic = [{"name": "Fireball", "cost": 10, "dmg": 50},
         {"name": "Lightening", "cost": 15, "dmg": 75},
         {"name": "Ice Storm", "cost": 8, "dmg": 40}
         ]
player1 = Person(460, 50, 50, 250, magic)
enemy1 = Person(500, 0, 25, 250, magic)

print(bcolors.PURPLE, "Welcome to Dungeon Slayer.", bcolors.ENDC)
print(bcolors.PURPLE, "A text based RPG by Blix. December 2020.", bcolors.ENDC)
print(bcolors.YELLOW, bcolors.BOLD, "An enemy ATTACKS!", bcolors.ENDC)
running = True
while running:
    player1.choose_action()
    action = input("Select Action:")
    index = int(action) - 1
    if index == 0:
        dmg = player1.generate_damage()
        enemy1.take_damage(dmg)
        print("The enemy takes", dmg, "points of damage. Enemy HP =", enemy1.get_hp())
        if enemy1.get_hp() == 0:
            print(bcolors.RED, bcolors.BOLD, "The enemy has died!!!", bcolors.ENDC)
            print(bcolors.BLUE, bcolors.BOLD, "The enemy has resurrected!!!!", bcolors.ENDC)
            enemy1.hp = 50
    elif index == 1:
        player1.choose_magic()
        magic_choice = int(input("Choose Magic:"))
        dmg = player1.generate_spell_damage(magic_choice)
        cost = player1.get_spell_cost(magic_choice)
        spell = player1.get_spell_name(magic_choice)
        current_mp = player1.get_mp()

        if cost > current_mp:
            print(bcolors.YELLOW, "\nYou don't have enough Magic Points. Choose again.", bcolors.ENDC)
            continue
        else:
            enemy1.take_damage(dmg)
            player1.reduce_mp(cost)
            current_mp = player1.get_mp()
            print(bcolors.BLUE, bcolors.BOLD, "You hit the enemy for", str(dmg) + ". You have", str(current_mp) ,"magic points left.", bcolors.ENDC)
            print("The enemy has", enemy1.get_hp(), "hp left.")
    dmg = enemy1.generate_damage()
    player1.take_damage(dmg)
    print("The player takes", dmg, "points of damage. Player HP =", player1.get_hp())
    if player1.get_hp() == 0:
        print(bcolors.RED, bcolors.BOLD, "Player1 has died!!!", bcolors.ENDC)
        print(bcolors.RED, bcolors.BOLD, "GOOD BYE!!!", bcolors.ENDC)
        running = False


