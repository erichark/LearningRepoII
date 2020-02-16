'''

    Python RPG
    November 25, 2019
    Second RPG game

'''

from classfolder.gamestuff import Person, bcolors
from classfolder.magic import Spell

import random
# instantiate Spells
fireball = Spell("Fireball", 10, 50, "Black")
lightening = Spell("Lightening", 15, 75, "Black")
ice = Spell("Ice Storm", 8, 40, "Black")
cure = Spell("Cure", 10, 50, "white")
heal = Spell("Heal", 15, 200, "white")

# instantiate players
player1 = Person(460, 50, 50, 250, [fireball, lightening, ice, cure, heal])
enemy1 = Person(500, 0, 25, 250, [])

print(bcolors.PURPLE, "Welcome to Dungeon Slayer.", bcolors.ENDC)
print(bcolors.PURPLE, "A text based RPG by Blix. December 2020.", bcolors.ENDC)
print(bcolors.YELLOW, bcolors.BOLD, "An enemy ATTACKS!", bcolors.ENDC)

running = True

# Main Game Loop, exits if the the player has 0 hp
while running:
    player1.choose_action()
    action = input("Select Action: ")
    index = int(action) - 1
    # If action choice is attack, simple physical attack
    if index == 0:
        dmg = player1.generate_damage()
        enemy1.take_damage(dmg)
        print("The enemy takes", dmg, "points of damage.")

    # If action choice is magic, choose the magic spell
    elif index == 1:
        player1.choose_magic()
        print("____________________________________________")
        magic_choice = int(input("Choose Magic: ")) - 1

        spell = player1.magic[magic_choice]
        current_mp = player1.get_mp()

        # Make sure the player has enough magic points. if not they have to choose again.
        if spell.cost > current_mp:
            print(bcolors.YELLOW, "\nYou don't have enough Magic Points. Choose again.", bcolors.ENDC)
            continue

        else:
            # determine if it's white (healing) or black(Hurting) magic
            print(spell.kind)
            if spell.kind == "Black":
                # generate magic damage and spell cost
                dmg = spell.generate_damage()
                enemy1.take_damage(dmg)
                player1.reduce_mp(spell.cost)
                current_mp = player1.get_mp()
                print(bcolors.BLUE, bcolors.BOLD, "You hit the enemy for", str(dmg) + ". You have", str(current_mp), "magic points left.", bcolors.ENDC)
            elif spell.kind == "White":
                # generate amount to heal and apply to character, lower their mp
                meds = spell.generate_healing()
                player1.take_healing(meds)
                player1.reduce_mp(spell.cost)
                current_mp = player1.get_mp()
                print(bcolors.BLUE, bcolors.BOLD, "You healed yourself for", str(meds) + ". You have", str(current_mp), "magic points left.", bcolors.ENDC)

    # Test if the enemy has no hp left, if so, deal with it.
    if enemy1.get_hp() == 0:
        print(bcolors.RED, bcolors.BOLD, "The enemy has died!!!", bcolors.ENDC)
        print(bcolors.BLUE, bcolors.BOLD, "The enemy has resurrected!!!!", bcolors.ENDC)
        enemy1.hp = 50
        # TODO keep enemy from resurrecting each time.

    # now the enemy attacks, physical damage only for now
    # TODO give enemy magic and randomize their choices for attacks and spell choice
    dmg = enemy1.generate_damage()
    player1.take_damage(dmg)
    print("The player takes", dmg, "points of damage.")

    # Print out the current HP of everyone
    print(bcolors.GREEN + "_______________________________________________________" + bcolors.ENDC)
    print(bcolors.PURPLE + "Enemy HP: " + bcolors.RED + str(enemy1.get_hp()) + "/" + bcolors.PURPLE + str(enemy1.get_max_hp()) + bcolors.ENDC)
    print(bcolors.BLUE + "Player HP: " + bcolors.RED + str(player1.get_hp()) + "/" + bcolors.BLUE + str(player1.get_max_hp()) + "   Player MP: " + bcolors.RED + str(player1.get_mp()) + "/" + bcolors.BLUE + str(player1.get_max_mp()) + bcolors.ENDC)
    print(bcolors.GREEN + "_______________________________________________________\n" + bcolors.ENDC)

    # test if the player has any remaining HP and if not, end the game.
    if player1.get_hp() == 0:
        print(bcolors.RED, bcolors.BOLD, "Player1 has died!!!", bcolors.ENDC)
        print(bcolors.RED, bcolors.BOLD, "GOOD BYE!!!", bcolors.ENDC)
        running = False

#TODO create and use objects
#TODO multiple players in a party, multiple enemies in a group
