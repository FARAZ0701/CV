import cv2
import numpy as np

cap = cv2.VideoCapture("resources/VID20230401004733.mp4")
subM = cv2.createBackgroundSubtractorMOG2()
while True:
    r,frame = cap.read()
    if r==True:
        frame = cv2.resize(frame,(600,600))
        subV = subM.apply(frame)
        cv2.imshow("Video",subV)
        if cv2.waitKey(24) & 0xff == ord('p'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()