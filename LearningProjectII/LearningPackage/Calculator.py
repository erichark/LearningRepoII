'''
Created on Dec 27, 2017

@author: Eric
'''
import re

print("Our Calculator")
print("Type 'Quit' to exit\n")
previous = 0
run = True


def performMath():
    global run
    global previous
    equation=""
    
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
        
        
    if equation == "Quit":
        run = False
        print("Goodbye, Dave.")
    elif equation == "quit":
        run = False
        print("Goodbye, Dave.")
    else:
        equation = re.sub('[a-zA-Z,.:" ",]','', equation)
       
        if previous == 0:
            previous = eval(equation)
        else: 
            previous = eval(str(previous) + equation)
    



while run:
    performMath()