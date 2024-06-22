import cv2

img = cv2.imread("resources/AHS0cc2566.jpg")

bluredImage = cv2.GaussianBlur(img, (7,7),0)
cv2.imshow("M.faraz", bluredImage)
cv2.waitKey(0)
# (src: MatLike, ksize: Size, sigmaX: float, dst: MatLike | None = ..., sigmaY: float = ..., borderType: int = ...) -> MatLike