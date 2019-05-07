'''
Created on Feb 24, 2019

@author: Riggs-MAC
'''

from tkinter import messagebox
class Emergency(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.emergencyPopUp() 
        
    def emergencyPopUp(self):
        messagebox.showinfo("Emergency Procedure Initialized", 
                                    "Vehicle Returning to Base")
