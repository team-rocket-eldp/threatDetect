# This script uses a computers front facing cam to record video and detect the color red in the video.
# Adjust the low_ H, S, and V values, as well as the high_ H, S, and V values to filter the red (or any) color.
#
# to run:
#   python findRed.py
#
# video file:
#   to use a video file instead, replace the 0 in 'cv.VideoCapture(0)' with the video file location
#
# save video:
#   to save the video with the red filter, uncomment 'fourcc = cv.VideoWriter_fourcc(*'DIVX')', 
#   'out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))', and 'out.write(frame)'

from __future__ import print_function
import cv2 as cv
import argparse

# images are filtered by Hue, Saturation, and Value (HSV), not RGB. The limits are,
#   hue: 0-179
#   saturation: 0-255
#   value: 0-255
low_H = 161
low_S = 155
low_V = 84
high_H = 179
high_S = 255
high_V = 255
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'

# starts the video capture, change the argument if you want to use a video file
cap = cv.VideoCapture(0)

# saving file
# fourcc = cv.VideoWriter_fourcc(*'DIVX')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

# creating 2 windows, one with the original screen capture and one filtered image
cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)

print('Hit q to quit')

while True:
    
    # look at the stream frame by frame, this grabs a single frame
    ret, frame = cap.read()    
    if frame is None:
        break

    # this allows us to resize the video
    # frame = cv.resize(frame, (960, 540))  

    # filtering happens by HSV in openCV so need to convert to HSV and then find red with inRange
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    
    #Tracking Color and placing a box around it
    (contours,hierarchy)=cv.findContours(frame_threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        # update line below to find smaller instances of red
        if(area>20):
                x,y,w,h = cv.boundingRect(contour)     
                frame = cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                centerX = x + w//2
                centerY = y + h//2
                cv.putText(frame, 
                            "RED - Center=" + str(centerX) + ',' + str(centerY),
                            (x,y-5), # Coordinates
                            cv.FONT_HERSHEY_COMPLEX_SMALL, # Font
                            1.0, # Scale. 2.0 = 2x bigger
                            (255,0,0))

    # show the original video with the modifications above and the filtered video
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)
    
    # write the frame
    # out.write(frame)

    # have to wait after each frame processing
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break