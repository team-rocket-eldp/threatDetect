import tkinter as tk
from tkinter import Frame, LEFT, RIGHT, Label, Button, BOTTOM, RAISED, ACTIVE, messagebox, ttk
#from tkinter.ttk import Style
##from GroundSystem import VideoCapture, Emergency
from PIL.ImageColor import colormap
from tkinter.constants import RAISED, GROOVE, SUNKEN, RIDGE
from GroundSystem import TLMdisplayParse
#from VideoDetection import VideoCapture
from numpy.core.defchararray import center
import os
import datetime


# vidObj = VideoCapture.VideoCapture()    
    
window = "Team Rocket Live Drone Feed"

root = tk.Tk()
style = tk.ttk.Style()
style.theme_use('classic')
root.wm_title(window)
root.configure(bg="black")

 
mainFrame = Frame(root, height=350, width=1300, bg="black")
mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
mainFrame.pack_propagate(0)

 
videoFrame = Frame(mainFrame, width=625, height=250, bg="black",colormap="new")
videoFrame.pack(side = LEFT,fill=tk.BOTH, expand=tk.YES)
videoFrame.pack_propagate(0)
lVideoFrame = ttk.Label(videoFrame, text="Live Feed", padding=15, background='black')
lVideoFrame.pack(side=LEFT,fill=tk.BOTH)
 
tlmFrame = Frame(mainFrame, width=625, height=250, bg="black")
tlmFrame.pack(side = RIGHT,fill=tk.BOTH, expand=tk.YES)
tlmFrame.pack_propagate(0)

closeInd = 0
index = 0

dataFrame1 = Frame(tlmFrame, height=150, width=650, bg = "white")
dataFrame1.pack(side = tk.TOP,fill=tk.BOTH, expand=tk.YES)

dataFrame2 = Frame(tlmFrame, height=150, width=650, bg = "white")
dataFrame2.pack(side = BOTTOM,fill=tk.BOTH, expand=tk.YES)

tlmCategories = ['Altitude', 'Temperature', 'Power', 'Health']

altFrame = Frame(dataFrame1, height=150, width=325, bg = "black")
altFrame.pack(side = LEFT,fill=tk.BOTH, expand=tk.YES)
altFrame.pack_propagate(0)
altLabel = Label(altFrame, text=tlmCategories[0], fg="white", bg="black", anchor=tk.NE)
altLabel.pack(side=LEFT, fill=tk.Y)
altMsg = tk.Message(altFrame)

tempFrame = Frame(dataFrame1, height=150, width=325, bg = "black")
tempFrame.pack(side = RIGHT,fill=tk.BOTH, expand=tk.YES)
tempFrame.pack_propagate(0)
tempLabel = Label(tempFrame, text=tlmCategories[1], fg="white", bg="black", anchor=tk.NE)
tempLabel.pack(side=LEFT, fill=tk.Y)
tempMsg = tk.Message(tempFrame)

pwrFrame = Frame(dataFrame2, height=150, width=325, bg = "black")
pwrFrame.pack(side = LEFT,fill=tk.BOTH, expand=tk.YES)
pwrFrame.pack_propagate(0)
pwrLabel = Label(pwrFrame, text=tlmCategories[2], fg="white", bg = "black", anchor=tk.NE)
pwrLabel.pack(side=LEFT, fill=tk.Y)
pwrMsg = tk.Message(pwrFrame)
pwrMsg2 = tk.Message(pwrFrame)

hlthFrame = Frame(dataFrame2, height=150, width=325, bg = "black")
hlthFrame.pack(side = RIGHT,fill=tk.BOTH, expand=tk.YES)
hlthFrame.pack_propagate(0)
hlthLabel = Label(hlthFrame, text=tlmCategories[3], fg="white", bg="black", anchor=tk.NE)
hlthLabel.pack(side=LEFT, fill=tk.Y)
hlthMsg = tk.Message(hlthFrame)
hlthMsg2 = tk.Message(hlthFrame)

def closeDownSet(x):
    global closeInd
    closeInd = x


def closeDownRead():
    global closeInd
    return closeInd

exitButton = Button(root, text="ABORT", command = lambda: closeDownSet(1))
exitButton.pack(side=BOTTOM, fill=tk.BOTH, expand=tk.YES)

x = datetime.datetime.now()
timeStamp = x.strftime("%m-%d-%y_%h-%M.%S")
global folder 
folder = timeStamp
os.makedirs(folder)
file = open("videos/readme.txt", "w+")
file.write(folder)
file.close()


def refreshData(index):
    
    altObj = TLMdisplayParse.TLMdisplayParse(lVideoFrame,altMsg,index,6,folder)
    tempObj = TLMdisplayParse.TLMdisplayParse(lVideoFrame,tempMsg,index,1,folder)
    pwrObj1 = TLMdisplayParse.TLMdisplayParse(lVideoFrame,pwrMsg,index,21,folder)
    pwrObj2 = TLMdisplayParse.TLMdisplayParse(lVideoFrame,pwrMsg2,index,20,folder)
    hlthObj1 = TLMdisplayParse.TLMdisplayParse(lVideoFrame,hlthMsg,index,38,folder)
    hlthObj2 = TLMdisplayParse.TLMdisplayParse(lVideoFrame,hlthMsg2,index,41,folder)
    root.update()
    root.after(50)

while(index < 5084):

    shouldExit = closeDownRead()
    if(shouldExit == 1):
        break
    
    refreshData(index)
    index += 1
    
    if(index == 4999):
        index = 0

#VideoCapture.VideoCapture('videos/testDrone.mov',lVideoFrame)  
# for filename in os.listdir('videos'):
#     if filename.endswith(".png"): 
#         # print(os.path.join(directory, filename))
#         VideoCapture.VideoCapture.detectImage(filename) 
#     else:
#         continue

    
root.destroy()
root.mainloop()