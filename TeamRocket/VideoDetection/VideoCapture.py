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


execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "data/resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
custom_objects = detector.CustomObjects(person=True, car=False)
detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path ,
                                                    "data/image2.png"), output_image_path=os.path.join(execution_path , 
                                                    "data/image2_new.png"), custom_objects=custom_objects, 
                                                    minimum_percentage_probability=65)


for eachObject in detections:
    print(eachObject)
    print("--------------------------------")
