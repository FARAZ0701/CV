import cv2
import numpy as np

img = cv2.imread("resources/AHS0cc2566.jpg")
img = cv2.resize(img,(600,600))
cv2.imshow("Mohammad faraz" , img)
cannyImg = cv2.Canny(img,200,600)
cv2.imshow("Mohammad faraz canny" , cannyImg)
cv2.imwrite("D:\\Faraz\\COMPUTER VISION PYTHON\\resources\\DownloadedImageFromPYTHON.png",cannyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()