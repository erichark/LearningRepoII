'''
Created on Aug 8, 2018

@author: root
'''

import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Button:
    def __init__(self,text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))
        
    def handleInput(self, val):


        
        if val == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif val == "√":
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
            
        elif val == "AC":
            self.results.setText("")
        elif val == "DEL":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        else:
            current_value = self.results.text()
            new_value = current_value + str(val)
            self.results.setText(new_value)
            
class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eric's Calculator")
        self.CreateApp()
        
    def CreateApp(self):
        grid = QGridLayout()
        
        buttons = ["AC", "√", "DEL", "/",
                   7, 8, 9, "*",
                   4,5,6, "-",
                   1,2,3, "+",
                   0, ".", "="]
        results = QLineEdit()
        
        grid.addWidget(results, 0,0,1,4)
        
        row = 1
        column = 0
        
        for button in buttons:
            buttonObject=Button(button, results)
             
            if button == "=":
                grid.addWidget(buttonObject.b, row, column, 1,2)
                column +=1
            else:
                grid.addWidget(buttonObject.b, row, column, 1,1)
                column +=1
                
            if column >3:
                row +=1
                column =0 

                        
        self.setLayout(grid)
        self.show()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())