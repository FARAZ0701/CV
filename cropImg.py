import cv2

img = cv2.imread("resources/AHS02274.JPG")
img = cv2.resize(img,(600,600))
cropImg = img[:250,:250]

cv2.imshow("Mohammd Faraz", img)
cv2.imshow("Ayzel", cropImg)

cv2.waitKey(0)