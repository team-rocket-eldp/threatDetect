import tkinter as tk
from tkinter import Frame, LEFT, RIGHT, Label, Button, BOTTOM, ttk, RAISED, ACTIVE, messagebox, ttk
from GUI import VideoCapture, Emergency
from PIL.ImageColor import colormap
from tkinter.constants import RAISED, GROOVE, SUNKEN, RIDGE

class GUI(object):
    window = "Team Rocket Live Drone Feed"

    root = tk.Tk()
    style = tk.ttk.Style
    style.theme_use('classic')
    root.wm_title(window)
    root.config(bg="black", height=375, width=1270)
     
    mainFrame = Frame(root)
    mainFrame.pack()
     
    videoFrame = Frame(root, width=625, height=250, bg="",
                        colormap="new")
    videoFrame.pack(side = LEFT)
    lVideoFrame = ttk.Label(videoFrame, text="Live Feed")
    lVideoFrame.grid(row=0,column=0)
     
    tlmFrame = Frame(root, width=625, height=250, bg="")
    tlmFrame.pack(side = RIGHT)
    tlmFrame.pack_propagate(0)
    
    dataFrame = Frame(tlmFrame, width=625, height=200, bg="blue")
    
    for r in range(5):
        for c in range(5):
            ttk.Label(dataFrame, text='R%s/C%s'%(r,c), fg="white").grid(row=r,column=c)

    emerStopFrame = Frame(tlmFrame)
    emerStopFrame.pack(side=BOTTOM)
     
    
    emergencyStop = Button(emerStopFrame, text="EMERGENCY STOP", fg='red',
                            relief=RIDGE, command=lambda : Emergency.Emergency())
                         
    emergencyStop.pack()
     
    VideoCapture.VideoCapture('videos/testDrone.mov',lVideoFrame)
    
    
    root.mainloop()