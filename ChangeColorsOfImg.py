import cv2

img = cv2.imread("resources/AHS0cc2566.jpg")
img = cv2.resize(img,(600,600))

newImg = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
cv2.imshow("imggg", newImg)
cv2.waitKey(0)
cv2.imwrite("D:\\Faraz\\COMPUTER VISION PYTHON\\resources\\newImg.png", newImg)
