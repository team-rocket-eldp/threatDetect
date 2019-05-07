'''
Created on May 1, 2019

@author: Riggs-MAC
'''
import random
import os
import subprocess
import sys
from posix import getcwd

class split_data_set:
    
    dir = getcwd()
    image_dir = dir +"/JPEGImages"

    f_val = open("models/box_test.txt", 'w')
    f_train = open("models/box_train.txt", 'w')
    
    path, dirs, files = next(os.walk(image_dir))
    data_size = len(files)

    ind = 0
    data_test_size = int(0.1 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)
    
    for f in os.listdir(image_dir):
        if(f.split(".")[1] == "jpg"):
            ind += 1
            
            if ind in test_array:
                f_val.write(image_dir+'/'+f+'\n')
            else:
                f_train.write(image_dir+'/'+f+'\n')


   