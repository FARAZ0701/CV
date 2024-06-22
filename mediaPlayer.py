import cv2
import numpy as np

cap = cv2.VideoCapture(r"D:\Downloads\Downloads\\MOV_0142.mp4")

while cap.isOpened():
    r,frame = cap.read()
    if r==True:
        frame = cv2.resize(frame,(720,720))
        cv2.imshow("Mohammad Faraz Nadir", frame)
        if cv2.waitKey(30) & 0xff == ord("p"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()