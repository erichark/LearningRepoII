'''
Created on Jan 1, 2018

@author: Eric
'''

from classes.enemy import Enemy2

        
#instantiate first enemy and print out it's stats
enemy1 = Enemy2(25,50)
print(enemy1.get_hp())

#instantiate second enemy and print out it's stats
enemy2 = Enemy2(35, 60)
print(enemy2.get_hp())




'''
player_hp = 260
enemy_atk_low = 10
enemy_atk_high = 29


while player_hp > 0:
    dmg = random.randrange(enemy_atk_low, enemy_atk_high)
    player_hp = player_hp - dmg 
    print("Enemy strikes for", dmg, "points of damage. Current HP is", player_hp)
        
    if player_hp <= 30:
        player_hp = 30

    
    if player_hp > 30:
        continue
    
    print("You have low health, you have been transported to the nearest inn.")
    break

  '''   