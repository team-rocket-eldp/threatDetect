import csv
import cv2
import subprocess

class TLMFileRead(object):
    def __init__(self):
        self.fileRead()

    def fileRead(self):
        #file = open("readme.txt", "r")
        #folder = file.read()
        
        #proc = subprocess.run('/Users/Riggs-MAC/blackbox_decode' +
        #                      ' /Users/Riggs-MAC/git/TeamRocket/TeamRocket/GroundSystem/logfiles/blackbox_log_2016-03-21_181104',
        #                      shell=True,check=True)
        #proc.kill()
        file = 'logfiles/blackbox_log_2016-03-21_181104.01.csv'
        cap = cv2.VideoCapture("videos/test.mov") 
                
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            y = 0
            rows = []
            
            LoopIteration = []
            time_us = []
            axisP0 = []
            axisP1 = []
            axisP2 = []
            axisI0 = []
            axisI1 = []
            axisI2 = []
            axisD0 = []
            axisD1 = []
            rcCommand0 = []
            rcCommand1 = []
            rcCommand2 = []
            rcCommand3 = []
            vbatLatest_V = []
            BaroAlt_cm = []
            gyroADC0 = []
            gyroADC1 = []
            gyroADC2 = []
            accSmooth0 = []
            accSmooth1 = []
            accSmooth2 = []
            debug0 = []
            debug1 = []
            debug2 = []
            debug3 = []
            motor0 = []
            motor1 = []
            motor2 = []
            motor3 = []
            flightModeFlags_flags = []
            stateFlags_flags = []
            failsafePhase_flags = []
            rxSignalReceived = []
            rxFlightChannelValid = []

            listOfArrays = [
                LoopIteration,          #0
                time_us,                #1
                axisP0,                 #2
                axisP1,                 #3
                axisP2,                 #4
                axisI0,                 #5
                axisI1,                 #6
                axisI2,                 #7
                axisD0,                 #8
                axisD1,                 #9
                rcCommand0,             #10
                rcCommand1,             #11
                rcCommand2,             #12
                rcCommand3,             #13
                vbatLatest_V,           #14
                BaroAlt_cm,             #15
                gyroADC0,               #16
                gyroADC1,               #17
                gyroADC2,               #18
                accSmooth0,             #19
                accSmooth1,             #20
                accSmooth2,             #21
                debug0,                 #22
                debug1,                 #23
                debug2,                 #24
                debug3,                 #25
                motor0,                 #26
                motor1,                 #27
                motor2,                 #28
                motor3,                 #29
                flightModeFlags_flags,  #30
                stateFlags_flags,       #31
                failsafePhase_flags,    #32
                rxSignalReceived,       #33
                rxFlightChannelValid    #34
                ]             
                        
            for row in csv_reader:
                rows.append(row)
                        
            for arr in listOfArrays:
                for dataset in rows:
                    arr.append(dataset[y])
                arr.pop(0)
                y+=1
                
        fileList = [cap, listOfArrays]
                        
        return fileList


