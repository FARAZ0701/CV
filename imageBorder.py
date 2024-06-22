import cv2
import numpy as np

img = cv2.imread("resources/AHS0cc2566.jpg")
img = cv2.resize(img,(500,600))
img0 = cv2.resize(img,(420,520))
img1=cv2.copyMakeBorder(img0,40,40,40,40,cv2.BORDER_CONSTANT,None,value=2)
print(img.shape,img0.shape,img1.shape)
h = np.hstack((img,img1))
cv2.imshow("M.faraz nadir",h)
cv2.waitKey(0)
cv2.destroyAllWindows()

