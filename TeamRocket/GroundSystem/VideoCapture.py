'''
Created on Feb 22, 2019

@author: Riggs-MAC
'''
import cv2
from PIL import Image, ImageTk



class VideoCapture(object):
        
    def __init__(self, video, videoFrame):
        self.videoFrame = videoFrame
        self.video = video
        self.cap = self.captureVideo()
        self.readVideo()
    
    def captureVideo(self):
        cap = cv2.VideoCapture(self.video) 
        return cap   
    
    def readVideo(self):
        cap = self.cap
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  
    
        img = Image.fromarray(gray).resize((600,200))
        imgTk = ImageTk.PhotoImage(image=img)
        self.videoFrame.imgtk = imgTk
        self.videoFrame.configure(image=imgTk) 
        self.videoFrame.after(5,self.readVideo)
     
            