                                                            #   FAILD ATTEMPT
                                                            #   FAILD ATTEMPT
                                                            #   FAILD ATTEMPT


import cv2
import numpy as np

OfficialImage = cv2.imread('resources/AHS0cc2566.jpg')
OfficialImageArray = np.array(OfficialImage)

RandomArray = np.array([[117, 153, 177],[117, 154, 176],[115, 154, 176]])
print("Array to be added  \n" , RandomArray)
print("this is offical Image Array", OfficialImageArray)
OfficialImageArray = np.delete(OfficialImageArray,0)
FinalArray = np.hstack((RandomArray, OfficialImageArray))
print("this is Final Image Array", FinalArray)
