'''
Created on Aug 8, 2018

@author: root
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eric's Calculator")
        self.show()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())