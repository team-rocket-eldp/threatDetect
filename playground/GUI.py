import tkinter as tk
from tkinter import Frame, BOTH, LEFT, RIGHT, Label, ttk, TOP, NE, BOTTOM
from tkinter.ttk import Style
import TLMdisplayParse

tlmCategories = ['Altitude', 'Temperature', 'Power', 'Health']

root = tk.Tk()
style = tk.ttk.Style()
style.theme_use('classic')

mainFrame = Frame(root, height=300, width=1300)
mainFrame.pack(fill=BOTH, expand=tk.YES)
mainFrame.pack_propagate(0)

vidFrame = Frame(mainFrame, height=300, width=650, bg="#607674")
vidFrame.pack(side=LEFT,fill=BOTH, expand=tk.YES)

tlmFrame = Frame(mainFrame, height=300,width=650, bg="blue")
tlmFrame.pack(side=RIGHT,fill=BOTH, expand=tk.YES)

dataFrame1 = Frame(tlmFrame, height=150, width=650, bg = "white")
dataFrame1.pack(side = TOP,fill=BOTH, expand=tk.YES)

dataFrame2 = Frame(tlmFrame, height=150, width=650, bg = "white")
dataFrame2.pack(side = BOTTOM,fill=BOTH, expand=tk.YES)



altFrame = Frame(dataFrame1, height=150, width=325, bg = "black")
altFrame.pack(side = LEFT,fill=BOTH, expand=tk.YES)
altFrame.pack_propagate(0)
altLabel = Label(altFrame, text=tlmCategories[0], fg="white", bg="black", anchor=NE)
altLabel.pack(side=LEFT, fill=tk.Y)

tempFrame = Frame(dataFrame1, height=150, width=325, bg = "black")
tempFrame.pack(side = RIGHT,fill=BOTH, expand=tk.YES)
tempFrame.pack_propagate(0)
tempLabel = Label(tempFrame, text=tlmCategories[1], fg="white", bg="black", anchor=NE)
tempLabel.pack(side=LEFT, fill=tk.Y)

pwrFrame = Frame(dataFrame2, height=150, width=325, bg = "black")
pwrFrame.pack(side = LEFT,fill=BOTH, expand=tk.YES)
pwrFrame.pack_propagate(0)
pwrLabel = Label(pwrFrame, text=tlmCategories[2], fg="white", bg = "black", anchor=NE)
pwrLabel.pack(side=LEFT, fill=tk.Y)

hlthFrame = Frame(dataFrame2, height=150, width=325, bg = "black")
hlthFrame.pack(side = RIGHT,fill=BOTH, expand=tk.YES)
hlthFrame.pack_propagate(0)
hlthLabel = Label(hlthFrame, text=tlmCategories[3], fg="white", bg="black", anchor=NE)
hlthLabel.pack(side=LEFT, fill=tk.Y)

index = 0

def refreshData(index):
    altObj = TLMdisplayParse.TLMdisplayParse(altFrame,index,6)
    tempObj = TLMdisplayParse.TLMdisplayParse(tempFrame,index,1)
    pwrObj1 = TLMdisplayParse.TLMdisplayParse(pwrFrame,index,21)
    pwrObj2 = TLMdisplayParse.TLMdisplayParse(pwrFrame,index,20)
    hlthObj1 = TLMdisplayParse.TLMdisplayParse(hlthFrame,index,38)
    hlthObj2 = TLMdisplayParse.TLMdisplayParse(hlthFrame,index,41)
    root.update()
    del altObj
    del tempObj
    del pwrObj1
    del pwrObj2
    del hlthObj1
    del hlthObj2

while index < 20:
    refreshData(index)
    index += 1

root.mainloop()
