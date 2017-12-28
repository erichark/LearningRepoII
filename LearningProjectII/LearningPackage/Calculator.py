'''
Created on Dec 27, 2017

@author: Eric
'''

print("Our Calculator")
print("Type 'Quit' to exit\n")
previous = 0
run = True


def performMath():
    global run
    equation = input("Enter equation:")
    if equation == "Quit":
        run = False
    elif equation == "quit":
        run = False
    else:
        print("You typed", equation)
    



while run:
    performMath()