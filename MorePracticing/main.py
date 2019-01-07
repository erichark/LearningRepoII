'''
Created on Jan 4, 2019

@author: root
'''


"""#a file for practing Python

#create a couple of games and let user choose what they want to play

def number_game(user_name = "Mr. Shine"):
    answer = 69
    running = True
    print("Hello", user_name)
    while running:
        guess = int(input("Guess a number:"))
        if guess == answer:
            print("YOU GOT IT!!!")
            running = False
        elif guess < answer:
            print("That's too low!")
        else:
            print("That's too high!")

def higher_lower (user_name = "Mr. Shine"):
    count = 0
    user_score = 0
    computer_score = 0
    print("Hello", user_name)
    print("You have ten guesses of higher or lower, and we'll keep score.")
    while count <10 :
        number1 = random.randint(1,25)
        number2 = random.randint(1,25)
        guess = input("Is number 1 higher or lower or same:")
        print(number1)
        print(number2)
        
        if number1 > number2 and guess == "higher":
            user_score += 1
            print("User Score:", user_score)
            print("Computer Score", computer_score)
                   
        elif number1 == number2 and guess == "same":
            user_score=user_score + 2
            print ("You got 2 points!")
            print("User Score:", user_score)
            print("Computer Score", computer_score)

        elif number1 < number2 and guess == "lower":
            user_score += 1
            print("User Score:", user_score)
            print("Computer Score", computer_score)

        else:
            computer_score += 1
            print("User Score:", user_score)
            print("Computer Score", computer_score)
        count += 1
        
    print("At the end of the game, the score is:")
    print(user_name + ":", user_score)
    print("Computer Score:", computer_score)
    if user_score > computer_score:
        print("YOU WIN!!!")
    elif user_score < computer_score:
        print("I WIN!!!!")
    else:
        print("It's a tie")

print("Welcome to the game machine.")
user_name = input("What is your name?")
print("Hello", user_name)

choice = input("Would you like to play a game?")
while choice in ("Yes", "yes", "y", "Y", "1", "OK", "YES", "YEs"):
    game_choice = input("Please enter 1 for guessing numbers, or 2 for 'hi/low':")
    if game_choice == "1":
        number_game(user_name)
    else:
        higher_lower(user_name)
    choice = input("Would you like to play another game?")

print("OK", user_name, "have a nice day.")       
        
"""

import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is:", data["age"], "--adding a year")
    data["age"] +=1 
    print("New age is", data["age"])
    
else:
    old_file = open("./ages.json", "w+")
    data = {"Name": "Eric", "age":43}
    print("Initializing file. Age is", data["age"])
    
old_file.seek(0)
old_file.write(json.dumps(data))





