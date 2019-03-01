import tkinter as tk
from tkinter import Frame, BOTH, LEFT, RIGHT, Label, ttk, TOP, NE, BOTTOM, Message, Button
from tkinter.ttk import Style
import TLMdisplayParse

tlmCategories = ['Altitude', 'Temperature', 'Power', 'Health']

root = tk.Tk()
style = tk.ttk.Style()
style.theme_use('classic')

mainFrame = Frame(root, height=350, width=1300)
mainFrame.pack(fill=BOTH, expand=tk.YES)
mainFrame.pack_propagate(0)

vidFrame = Frame(mainFrame, height=300, width=650, bg="#607674")
vidFrame.pack(side=LEFT,fill=BOTH, expand=tk.YES)
vidFrame.pack_propagate(0)

tlmFrame = Frame(mainFrame, height=300,width=650, bg="black")
tlmFrame.pack(side=RIGHT,fill=BOTH, expand=tk.YES)
tlmFrame.pack_propagate(0)

closeInd = 0
index = 0

def closeDownSet(x):
    global closeInd
    closeInd = x


def closeDownRead():
    global closeInd
    return closeInd

exitButton = Button(root, text="ABORT", command = lambda: closeDownSet(1))
exitButton.pack(side=BOTTOM, fill=BOTH, expand=tk.YES)

dataFrame1 = Frame(tlmFrame, height=150, width=650, bg = "white")
dataFrame1.pack(side = TOP,fill=BOTH, expand=tk.YES)

dataFrame2 = Frame(tlmFrame, height=150, width=650, bg = "white")
dataFrame2.pack(side = BOTTOM,fill=BOTH, expand=tk.YES)



altFrame = Frame(dataFrame1, height=150, width=325, bg = "black")
altFrame.pack(side = LEFT,fill=BOTH, expand=tk.YES)
altFrame.pack_propagate(0)
altLabel = Label(altFrame, text=tlmCategories[0], fg="white", bg="black", anchor=NE)
altLabel.pack(side=LEFT, fill=tk.Y)
altMsg = Message(altFrame)

tempFrame = Frame(dataFrame1, height=150, width=325, bg = "black")
tempFrame.pack(side = RIGHT,fill=BOTH, expand=tk.YES)
tempFrame.pack_propagate(0)
tempLabel = Label(tempFrame, text=tlmCategories[1], fg="white", bg="black", anchor=NE)
tempLabel.pack(side=LEFT, fill=tk.Y)
tempMsg = Message(tempFrame)

pwrFrame = Frame(dataFrame2, height=150, width=325, bg = "black")
pwrFrame.pack(side = LEFT,fill=BOTH, expand=tk.YES)
pwrFrame.pack_propagate(0)
pwrLabel = Label(pwrFrame, text=tlmCategories[2], fg="white", bg = "black", anchor=NE)
pwrLabel.pack(side=LEFT, fill=tk.Y)
pwrMsg = Message(pwrFrame)
pwrMsg2 = Message(pwrFrame)

hlthFrame = Frame(dataFrame2, height=150, width=325, bg = "black")
hlthFrame.pack(side = RIGHT,fill=BOTH, expand=tk.YES)
hlthFrame.pack_propagate(0)
hlthLabel = Label(hlthFrame, text=tlmCategories[3], fg="white", bg="black", anchor=NE)
hlthLabel.pack(side=LEFT, fill=tk.Y)
hlthMsg = Message(hlthFrame)
hlthMsg2 = Message(hlthFrame)


def refreshData(index):
    
    altObj = TLMdisplayParse.TLMdisplayParse(altMsg,index,6)
    tempObj = TLMdisplayParse.TLMdisplayParse(tempMsg,index,1)
    pwrObj1 = TLMdisplayParse.TLMdisplayParse(pwrMsg,index,21)
    pwrObj2 = TLMdisplayParse.TLMdisplayParse(pwrMsg2,index,20)
    hlthObj1 = TLMdisplayParse.TLMdisplayParse(hlthMsg,index,38)
    hlthObj2 = TLMdisplayParse.TLMdisplayParse(hlthMsg2,index,41)
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

    
root.destroy()
root.mainloop()
