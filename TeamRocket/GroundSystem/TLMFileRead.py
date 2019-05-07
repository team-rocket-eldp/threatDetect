import csv
import cv2

class TLMFileRead(object):
    def __init__(self):
        pass

    def fileRead(self,file,vidFile):
                
        cap = cv2.VideoCapture(vidFile) 
                
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            y = 0
            rows = []

            Id = []
            TimeInSec = []
            TimeInText = []
            Latitude = []
            Longitude = []
            FlightMode = []
            AltitudeInFeet = []
            AltitudeInMeters = []
            VpsAltitudeInFeet = []
            VpsAltitudeInMeters = []
            HSpeedInMPH = []
            HSpeedInMetersPerSec = []
            GpsSpeedInMPH = []
            GpsSpeedInMetersPerSec = []
            HomeDistanceInFeet = []
            HomeDistanceInMeters = []
            HomeLatitude = []
            HomeLongitude = []
            GpsCount = []
            GpsLevel = []
            BatteryPowerInPercent = []
            BatteryVoltage = []
            BatteryVoltageDeviation = []
            BatteryCell1Voltage = []
            BatteryCell2Voltage = []
            BatteryCell3Voltage = []
            VelocityX = []
            VelocityY = []
            VelocityZ = []
            Pitch = []
            Roll = []
            Yaw = []
            YawIn360 = []
            RcAileron = []
            RcElevator = []
            RcGyro = []
            RcRudder = []
            RcThrottle = []
            NonGpsError = []
            GoHomeStatus = []
            AppTip = []
            AppWarning = []
            AppMessage = []

            listOfArrays = [
                Id,                     #0
                TimeInSec,              #1
                TimeInText,             #2
                Latitude,               #3
                Longitude,              #4
                FlightMode,             #5
                AltitudeInFeet,         #6
                AltitudeInMeters,       #7
                VpsAltitudeInFeet,      #8
                VpsAltitudeInMeters,    #9
                HSpeedInMPH,            #10
                HSpeedInMetersPerSec,   #11
                GpsSpeedInMPH,          #12
                GpsSpeedInMetersPerSec, #13
                HomeDistanceInFeet,     #14
                HomeDistanceInMeters,   #15
                HomeLatitude,           #16
                HomeLongitude,          #17
                GpsCount,               #18
                GpsLevel,               #19
                BatteryPowerInPercent,  #20
                BatteryVoltage,         #21
                BatteryVoltageDeviation,#22
                BatteryCell1Voltage,    #23
                BatteryCell2Voltage,    #24
                BatteryCell3Voltage,    #25
                VelocityX,              #26
                VelocityY,              #27
                VelocityZ,              #28
                Pitch,                  #29
                Roll,                   #30
                Yaw,                    #31
                YawIn360,               #32
                RcAileron,              #33
                RcElevator,             #34
                RcGyro,                 #35
                RcRudder,               #36
                RcThrottle,             #37
                NonGpsError,            #38
                GoHomeStatus,           #39
                AppTip,                 #40
                AppWarning,             #41
                AppMessage              #42
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


