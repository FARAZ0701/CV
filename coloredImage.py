import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

orignalImg = cv2.imread("resources/AHS02274.JPG")
print(orignalImg.shape)
orignalImg=cv2.resize(orignalImg,(720,720))
versionOneImage = orignalImg.copy()
versionTwoImage = orignalImg.copy()
versionThreeImage = orignalImg.copy()

print(versionOneImage.shape)
versionOneImage[:,:,0] = 0
versionTwoImage[:,:,1] = 0
versionThreeImage[:,:,2] = 0
versionOneImage.crop((0,0,500,500))
print(versionOneImage.shape)
cv2.imshow("v 1",versionOneImage)
cv2.imshow("v 2",versionTwoImage)
cv2.imshow("v 3",versionThreeImage)

cv2.waitKey(0)
