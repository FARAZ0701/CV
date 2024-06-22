import cv2
import numpy as np

blankImage = np.zeros((500,500,3),np.uint8)*255
cv2.namedWindow("ColorWindow")

def ColorFunction(x):
    pass


cv2.createTrackbar("R","ColorWindow",0,255,ColorFunction)
cv2.createTrackbar("G","ColorWindow",0,255,ColorFunction)
cv2.createTrackbar("B","ColorWindow",0,255,ColorFunction)

while True:
    cv2.imshow("ColorWindow",blankImage)
    if cv2.waitKey(1) & 0xff == ord('p'):
        break
    r = cv2.getTrackbarPos("R","ColorWindow")
    g = cv2.getTrackbarPos("G","ColorWindow")
    b = cv2.getTrackbarPos("B","ColorWindow")

    blankImage[:] = [b,g,r]


