import cv2

image = cv2.imread("resources/AHS0cc2566.jpg")
image = cv2.resize(image,(600,700))
imageTxt= cv2.putText(image,"Faraz",(50,100),2,4.1,(255,0,0),4,3,False)
#(img: MatLike, text: str, org: Point, fontFace: int, fontScale: float, color: Scalar, thickness: int = ..., lineType: int = ..., bottomLeftOrigin: bool = ...) -> MatLike
cv2.imshow("Mohammad Faraz", imageTxt)
cv2.waitKey(0)