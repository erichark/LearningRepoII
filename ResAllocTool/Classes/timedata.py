'''
Created on Aug 8, 2018

@author: root
'''

class TimeData(object):
    '''
    Defines the TimeData object
    '''


    def __init__(self, ResName, Client, Project, WeekStart, Hours):
        '''
        Constructor
        '''
        self.ResName = ResName
        self.Client = Client
        self.Project = Project
        self.WeekStart = WeekStart
        self.Hours = Hours
        
        
    def SaveData(self):
        #reads time from the interface and saves it into the DB
        return
    
    def LoadData(self):
        #Takes time from file and puts in DB
        return
    
        
        