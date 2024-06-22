
import cv2
cap = cv2.VideoCapture("resources/VID20230401004733.mp4")
c = 0

while True:
    r,frame = cap.read()
    if r == True:
        frame = cv2.resize(frame,(600,600))
        fileName = "D:\\Faraz\\COMPUTER VISION PYTHON\\resources"+ str(c)+".png"
        cv2.imwrite(fileName,frame)
        cv2.imshow("video", frame)
        c += 1
        if cv2.waitKey(10) & 0xff == ord('p'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows( )



