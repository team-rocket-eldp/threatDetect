'''
Created on Mar 4, 2019

@author: Riggs-MAC
'''

'''
Created on Mar 3, 2019

@author: Riggs-MAC
'''
from imageai.Detection import ObjectDetection

#from GroundSystem import GUI 
import os
import datetime

index = 0

file = open("videos/readme.txt", "r")
folder = file.read()
os.makedirs(folder+"/detects")
reportF = open(folder+"/detects/detects.txt", "a+")

start = datetime.datetime.now()
startTimeStamp = start.strftime("%m-%d-%Y_%H-%M-%S")

   

for img in os.listdir(folder): 
    if img.endswith(".png"):
    
        x = datetime.datetime.now()
        timeStamp = x.strftime("%h-%M-%S")
        
        execution_path = os.getcwd()
        
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath( os.path.join(execution_path , "videos/resnet50_coco_best_v2.0.1.h5"))
        detector.loadModel()
        custom_objects = detector.CustomObjects(person=True, car=False)
        detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path ,
                                                            folder+"/"+img), output_image_path=os.path.join(execution_path , 
                                                            folder+"/detects/detect_"+timeStamp+".png"), custom_objects=custom_objects, 
                                                            minimum_percentage_probability=65)
        
        
        for value in detections:
            print(value)
            print("--------------------------------")
            reportF.write("\nObject "+str(index)+"\n")
            for key,value in value.items():
                    reportF.write(str(key)+":\t"+str(value)+"\n")
            reportF.write("--------------------\n")
            index = index + 1
        
        durationInd = x - start
        durationIndStr = str(durationInd)
        reportF.write(durationIndStr)

duration = x - start
durationStr = str(duration)
#durationFormat = durationStr.strftime("%H%M%S")

reportF.write("\ntime:\t"+durationStr)    
reportF.close()
