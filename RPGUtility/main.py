'''
Created on Jan 18, 2019

@author: root
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random

class Dice:
    """Class for handling the dice setup, selection of die, and roll vs. comparator. """
    
    def __init__(self, selected_dice_value, comparator, text, results):
        #init the die selector buttons (2 through 100)
        self.dieButton = QPushButton(str(text))
        self.text = text
        self.dieButton.clicked.connect(lambda: self.SelectDiceValue(self.text))
        
        #init the roll button
        self.rollButton = QPushButton(str(text))
        self.selected_dice_value = selected_dice_value
        self.comparator = comparator
        self.results = results
        self.rollButton.clicked.connect(lambda: self.CompareResults(self.selected_dice_value, self.comparator, self.results))
        
    def CompareResults(self, selected_dice_value, comparator, results):
        #gets the value of the rolled dice and compares, returns a string indicating result
        #everything is working, excepting getting the value of the comparator.
        Dice.seleceted_dice_value = "2"
        print("Comparator is:", comparator.text())
        print("Selected Dice Value is:", Dice.selected_dice_value)
        roll_value = random.randint(1,Dice.selected_dice_value)
        print("Roll Value is:", roll_value)
        
        if roll_value == Dice.selected_dice_value:
            result_string = "You've rolled the MAX!!! Success"
        elif roll_value >= int(comparator.text()):
            result_string = "Success"
        elif roll_value < int(comparator.text()):
            result_string =  "Fail"
        else:
            result_string =  "There has been an error!" 
        #result_string = str("Die:", Dice.selected_dice_value, "Roll:", roll_value, "Result:", result_string)
        results.setText(result_string)
        
    def SelectDiceValue(self, dice_value):
        Dice.selected_dice_value = dice_value
        print(Dice.selected_dice_value)
        
class UtilityApp(QWidget):
    """
    Builds the actual app, laying out the grid and putting the necessary widgets into the right spots.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG Utility")
        self.CreateApp()
        
        
    def CreateApp(self):
        dice_values = [2,4,6,8,10,12,20,100]
        comparator = 10
        selected_die_value = 2
        grid = QGridLayout()
        
        row = 0
        col = 0
        counter = 0   
        results = QLabel("Results")
        
        for dice_sides in dice_values:
            buttonObject = Dice(selected_die_value, comparator, dice_values[counter], results)
            counter +=1
            grid.addWidget(buttonObject.dieButton, row, col, 1, 1)
            if col < 3:
                col +=1 
            else:
                row += 1
                col = 0
           
        description = QLabel("Enter Value:")
        grid.addWidget(description, row, col, 1, 1)
        
        
        col +=1
        comparator = QLineEdit()
        comparator.setText("0")
        grid.addWidget(comparator, row, col, 1,2)   

        row +=1
        roller = Dice(selected_die_value, comparator, "Roll", results)
        grid.addWidget(roller.rollButton, row, col, 1, 2)

        row +=1
        grid.addWidget(results, row, 0, 1, 2)

        
          
        self.setLayout(grid)
        self.show()   
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UtilityApp()
    sys.exit(app.exec())
    
