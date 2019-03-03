from GroundSystem import TLMFileRead
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import cv2


class TLMdisplayParse(object):

    obj = TLMFileRead.TLMFileRead()
    arr = obj.fileRead('videos/testData.text','videos/testDrone2.mp4')
    
    cap = arr[0]
    listOfArrays = arr[1]
    
    def __init__(self, vidFrame, msgframe, index, case):
        self.vidFrame = vidFrame
        self.msgframe = msgframe
        self.index = index
        self.case = case
        self.display()

    def display(self):
        
        cap = self.cap
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  
    
        img = Image.fromarray(gray).resize((600,200))
        imgTk = ImageTk.PhotoImage(image=img)
        self.vidFrame.imgtk = imgTk
        self.vidFrame.configure(image=imgTk)

        var = tk.StringVar()
        tlmFont = font.Font(family="Times New Roman", size=18, weight="bold")
        
        if(self.case == 6):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=65, width=150)
            self.msgframe.pack(side=tk.TOP, fill=tk.BOTH,expand=tk.YES)
            var.set(self.listOfArrays[self.case][self.index] + " ft")
        if(self.case == 1):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=65, width=150)
            self.msgframe.pack(side=tk.TOP, fill=tk.BOTH,expand=tk.YES)
            var.set(self.listOfArrays[self.case][self.index] + " deg F")
        if(self.case == 21):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=25, width=150)
            self.msgframe.pack(side=tk.TOP, fill=tk.BOTH,expand=tk.YES)
            var.set(self.listOfArrays[self.case][self.index] + " V")
        if(self.case == 20):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=25, width=150)
            self.msgframe.pack(side=tk.BOTTOM, fill=tk.BOTH,expand=tk.YES)
            var.set(self.listOfArrays[self.case][self.index] + "%")
        if(self.case == 38):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=25, width=150)
            self.msgframe.pack(side=tk.TOP, fill=tk.BOTH,expand=tk.YES)
            var.set(self.listOfArrays[self.case][self.index] + "?")
        if(self.case == 41):
            
            self.msgframe.configure(textvariable=var, font=tlmFont,
                                     bg="black", fg="white",
                                     pady=25, width=150)
            self.msgframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)
            var.set(self.listOfArrays[self.case][self.index] + "?")


        
