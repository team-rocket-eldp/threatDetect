import csv


class TLMFileRead(object):

    file = 'data/testData.txt'

    def __init__(self,file):
        self.file = file
        return self.csvRead(self.file)

    def csvRead(self, file):
                
        #each column is an array
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
                Id,
                TimeInSec,
                TimeInText,
                Latitude,
                Longitude,
                FlightMode,
                AltitudeInFeet,
                AltitudeInMeters,
                VpsAltitudeInFeet,
                VpsAltitudeInMeters,
                HSpeedInMPH,
                HSpeedInMetersPerSec,
                GpsSpeedInMPH,
                GpsSpeedInMetersPerSec,
                HomeDistanceInFeet,
                HomeDistanceInMeters,
                HomeLatitude,
                HomeLongitude,
                GpsCount,
                GpsLevel,
                BatteryPowerInPercent,
                BatteryVoltage,
                BatteryVoltageDeviation,
                BatteryCell1Voltage,
                BatteryCell2Voltage,
                BatteryCell3Voltage,
                VelocityX,
                VelocityY,
                VelocityZ,
                Pitch,
                Roll,
                Yaw,
                YawIn360,
                RcAileron,
                RcElevator,
                RcGyro,
                RcRudder,
                RcThrottle,
                NonGpsError,
                GoHomeStatus,
                AppTip,
                AppWarning,
                AppMessage
                ]
        with open(file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                rows = []
                y = 0
                #parse data into array list
                for row in csv_reader:
                        rows.append(row)
                
                for arr in listOfArrays:
                        for dataset in rows:
                                arr.append(dataset[y])
                        #increase in y aligns header with data
                        y+=1

        return listOfArrays
