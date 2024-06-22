import cv2

myImage = cv2.imread("resources/AHS0cc2566.jpg")
myImage = cv2.resize(myImage,(600,700))
rectangleImage = cv2.rectangle(myImage,(5000,5000),(1500,25000),(0,255,0),-1,3,4)
cv2.imshow("Faraz",rectangleImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
#(img: MatLike, pt1: Point, pt2: Point, color: Scalar, thickness: int = ..., lineType: int = ..., shift: int = ...) -> MatLike