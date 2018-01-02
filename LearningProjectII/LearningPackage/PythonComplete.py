'''
Created on Dec 23, 2017

@author: Eric
'''

import re


CatchFire = False

def MainProg():
    global CatchFire
    
    print('Welcome to our first program/n')
    print('You can (c)ount, (e)valuate, (g)uess, or (q)uit')
    menu_choice = input('What would you like me to do?')
    
    if menu_choice == 'c':
        numb = 0
        top = int(input("what would you like to count to?"))
        while top >= numb:
            print(numb)
            numb+=1

    elif menu_choice == 'e':
        equation = input('What would you like to evaluate?\n')
        equation = re.sub('[A-Za-z:;,."]', '', equation)
        print(eval(equation))
        
    elif menu_choice == 'g':
        answers = ['New York','Boston', 'London', 'Lyon']
        exiter = False
        while exiter == False:
            print("This is a guessing game.")
            guess = input('Guess a city I\'ve been to this year:')
            if guess in answers:
                print("You're RIGHT!")
                exiter = True
            else:
                print("Incorrect. Try again")
    elif menu_choice == 'q':
        print('Goodbye, Dave.')
        CatchFire = True
        

while CatchFire == False:
    MainProg()