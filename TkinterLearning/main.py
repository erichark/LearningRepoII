'''
Created on Aug 8, 2018

@author: root
'''

import sys
from PyQt5.QtWidgets import (QLineEdit, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0
        
    def init_ui(self):
        self.label = QLabel("Enter Name: ")
        self.button = QPushButton("Nothing")
        self.TextLabel = QLabel("There has been nothing entered")
        self.text_field = QLineEdit()
        
        self.button.setText("Nothing has been entered yet")
        self.button.clicked.connect(self.AlterButton)
        horiztonal1 = QHBoxLayout()
        horiztonal1.addWidget(self.label)
        horiztonal1.addWidget(self.text_field)
        
        
        vertical1 = QVBoxLayout()
        vertical1.addWidget(self.TextLabel)
        vertical1.addLayout(horiztonal1)
        vertical1.addWidget(self.button)
       
        self.setLayout(vertical1)
        
        self.setWindowTitle("This is new")
        self.show()

    def AlterButton(self):
        user_name = self.text_field.text()
        our_string = "Your name is " + user_name
        self.TextLabel.setText(our_string)
        self.setWindowTitle(user_name + "'s Window")
        self.button.setText("Reset Name")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    
    