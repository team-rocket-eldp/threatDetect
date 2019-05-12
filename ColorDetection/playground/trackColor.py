from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
max_value = 255
max_value_H = 360//2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
window_low_name = 'Low Image Color'
window_high_name = 'High Image Color'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'

low_R = 0
low_G = 0
low_B = 0
high_R = max_value
high_G = max_value
high_B = max_value
low_R_name = 'Low R'
low_G_name = 'Low G'
low_B_name = 'Low B'
high_R_name = 'High R'
high_G_name = 'High G'
high_B_name = 'High B'

low_hsv = [0,0,0]
high_hsv = [max_value_H,max_value,max_value]

img_low = np.zeros((300,512,3), np.uint8)
img_high = np.zeros((300,512,3), np.uint8)

def on_low_B_thresh_trackbar(val):
    global low_B
    global low_R
    global low_G
    
    global low_hsv
    global high_hsv

    low_B = val
    low_bgr = np.uint8([[[low_B,low_G,low_R]]])
    low_hsv = cv.cvtColor(low_bgr,cv.COLOR_BGR2HSV)

    update_hsv()
    cv.setTrackbarPos(low_B_name, window_detection_name, low_B)
def on_high_B_thresh_trackbar(val):
    global high_B
    global high_R
    global high_G

    global high_hsv
    global low_hsv

    high_B = val
    high_bgr = np.uint8([[[high_B,high_G,high_R]]])
    high_hsv = cv.cvtColor(high_bgr,cv.COLOR_BGR2HSV)

    update_hsv()
    cv.setTrackbarPos(high_B_name, window_detection_name, high_B)
def on_low_R_thresh_trackbar(val):
    global low_B
    global low_R
    global low_G
    
    global low_hsv
    global high_hsv

    low_R = val
    low_bgr = np.uint8([[[low_B,low_G,low_R]]])
    low_hsv = cv.cvtColor(low_bgr,cv.COLOR_BGR2HSV)

    update_hsv()
    cv.setTrackbarPos(low_R_name, window_detection_name, low_R)
def on_high_R_thresh_trackbar(val):
    global high_B
    global high_R
    global high_G

    global high_hsv
    global low_hsv

    high_R = val
    high_bgr = np.uint8([[[high_B,high_G,high_R]]])
    high_hsv = cv.cvtColor(high_bgr,cv.COLOR_BGR2HSV)

    update_hsv()
    cv.setTrackbarPos(high_R_name, window_detection_name, high_R)
def on_low_G_thresh_trackbar(val):
    global low_B
    global low_R
    global low_G
    
    global low_hsv
    global high_hsv

    low_G = val
    low_bgr = np.uint8([[[low_B,low_G,low_R]]])
    low_hsv = cv.cvtColor(low_bgr,cv.COLOR_BGR2HSV)

    update_hsv()
    cv.setTrackbarPos(low_G_name, window_detection_name, low_G)
def on_high_G_thresh_trackbar(val):
    global high_B
    global high_R
    global high_G

    global high_hsv
    global low_hsv

    high_G = val
    high_bgr = np.uint8([[[high_B,high_G,high_R]]])
    high_hsv = cv.cvtColor(high_bgr,cv.COLOR_BGR2HSV)

    update_hsv()
    cv.setTrackbarPos(high_G_name, window_detection_name, high_G)

def update_hsv():
    global high_hsv
    global low_hsv

    high_hsv = np.maximum(high_hsv, low_hsv)
    low_hsv = np.minimum(high_hsv, low_hsv)

    

parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera devide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(args.camera)
cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)
cv.createTrackbar(low_R_name, window_detection_name , low_R, max_value, on_low_R_thresh_trackbar)
cv.createTrackbar(high_R_name, window_detection_name , high_R, max_value, on_high_R_thresh_trackbar)
cv.createTrackbar(low_G_name, window_detection_name , low_G, max_value, on_low_G_thresh_trackbar)
cv.createTrackbar(high_G_name, window_detection_name , high_G, max_value, on_high_G_thresh_trackbar)
cv.createTrackbar(low_B_name, window_detection_name , low_B, max_value, on_low_B_thresh_trackbar)
cv.createTrackbar(high_B_name, window_detection_name , high_B, max_value, on_high_B_thresh_trackbar)


while True:
    
    ret, frame = cap.read()
    if frame is None:
        break
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, np.array(low_hsv,np.uint8), np.array(high_hsv,np.uint8))
    
    

    cv.imshow(window_low_name,img_low)
    cv.imshow(window_high_name,img_high)
    cv.imshow(window_detection_name, frame_threshold)
    
    img_low[:] = [low_B,low_G,low_R]
    img_high[:] = [high_B,high_G,high_R]
    

    #Tracking Colour (Yellow) 
    (contours,hierarchy)=cv.findContours(frame_threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
            area = cv.contourArea(contour)
            if(area>300):
                    
                    x,y,w,h = cv.boundingRect(contour)     
                    frame = cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    
    cv.imshow(window_capture_name, frame)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break