import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

ListOfImage = os.listdir(r"D:\Faraz\COMPUTER VISION PYTHON\resources")
print(ListOfImage)
for name in ListOfImage:
    Locate = "D:\\Faraz\\COMPUTER VISION PYTHON\\resources"
    path = Locate +"\\"+name
    imgLoop = cv2.imread(path)
    imgLoop = cv2.resize(imgLoop,(500,600)) 
    cv2.imshow("Loop", imgLoop)
    cv2.waitKey(4000)