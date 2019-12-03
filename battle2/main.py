'''

    Python RPG
    November 25, 2019
    Second RPG game

'''

from classes.game import Person, bcolors


magic = [{"name": "Fireball", "cost": 10, "dmg": 50},
         {"name": "Lightening", "cost": 15, "dmg": 75},
         {"name": "IcsStorm", "cost": 8, "dmg": 40}
         ]
player1 = Person(460, 50, 25, 250, magic)
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

        dmg = enemy1.generate_damage()
        player1.take_damage(dmg)
        print("The player takes", dmg, "points of damage. Player HP =", player1.get_hp())
