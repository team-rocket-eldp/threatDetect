'''
Created on Mar 4, 2019

@author: Riggs-MAC
'''
'''
Created on Mar 3, 2019

@author: Riggs-MAC
'''
from imageai.Detection import ObjectDetection
import os
import datetime

class VideoCapture(object):
    
    def __init__(self):
        pass
    
    def detectImage(self, image):
        x = datetime.datetime.now()
        timeStamp = x.strftime("%m%d%Y_%H%M%S")
        
        execution_path = os.getcwd()
    
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath( os.path.join(execution_path , "data/resnet50_coco_best_v2.0.1.h5"))
        detector.loadModel()
        custom_objects = detector.CustomObjects(person=True, car=False)
        detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path ,
                                                            "videos/"+ image), output_image_path=os.path.join(execution_path , 
                                                            "videos/frame_" + timeStamp + ".png"), custom_objects=custom_objects, 
                                                            minimum_percentage_probability=65)
        
        
        for eachObject in detections:
            print(eachObject)
            print("--------------------------------")
