'''
Created on Aug 8, 2018

@author: root
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    
    def __init__(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('web.png'))
        
    
    
if __name__=='__main__':
   
    app=QApplication(sys.argv)
    sys.exit(app.exec_())
   
    