import TLMFileRead
import tkinter as tk
from tkinter import font


class TLMdisplayParse(object):

    obj = TLMFileRead.TLMFileRead()
    arr = obj.fileRead('data/testData.txt')

    def __init__(self, msgframe, index, case):
        self.msgframe = msgframe
        self.index = index
        self.case = case
        self.display()

    def display(self):

        var = tk.StringVar()
        tlmFont = font.Font(family="Times New Roman", size=18, weight="bold")
        
        if(self.case == 6):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=65, width=150)
            self.msgframe.pack(side=tk.TOP, fill=tk.BOTH)
            var.set(self.arr[self.case][self.index] + " ft")
        if(self.case == 1):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=65, width=150)
            self.msgframe.pack(side=tk.TOP, fill=tk.BOTH)
            var.set(self.arr[self.case][self.index] + " deg F")
        if(self.case == 21):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=25, width=150)
            self.msgframe.pack(side=tk.TOP, fill=tk.BOTH)
            var.set(self.arr[self.case][self.index] + " V")
        if(self.case == 20):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=25, width=150)
            self.msgframe.pack(side=tk.BOTTOM, fill=tk.BOTH)
            var.set(self.arr[self.case][self.index] + "%")
        if(self.case == 38):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=25, width=150)
            self.msgframe.pack(side=tk.TOP, fill=tk.BOTH)
            var.set(self.arr[self.case][self.index] + "?")
        if(self.case == 41):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=25, width=150)
            self.msgframe.pack(side=tk.BOTTOM, fill=tk.BOTH)
            var.set(self.arr[self.case][self.index] + "?")


        
