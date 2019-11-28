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



print("Player1 hp =", player1.hp)
spell_dmg = player1.generate_spell_damage(1)
player1.take_damage(spell_dmg)
print(spell_dmg)
print("Player1 hp =", player1.hp)


