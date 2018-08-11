'''
Created on Aug 8, 2018

@author: root
'''
from tkinter import *
#from timedata import *

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Resource Allocation Tool")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #Creating the menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        #create the file menu and add Exit command
        file=Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        
        #create the edit menu and add dummy Undo command
        edit=Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)
        
        
        # creating a button instance
        quitButton = Button(self, text="Quit", command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=735, y=560)
        
        #Creatre the Save Button, NOTE: NEEDS COMMAND UPDATED
        saveButton = Button(self, text = "Save", command=self.client_exit)
        saveButton.place(x=675, y=560)
    
    def client_exit(self):
        exit()
        
        
root = Tk()

#size of the window
root.geometry("800x600")

app = Window(root)
root.mainloop()  
        