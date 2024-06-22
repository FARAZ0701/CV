
                                                                        # alllFramesOfVideoInImg

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

                                                                            # BlurIng


img = cv2.imread("resources/AHS0cc2566.jpg")

bluredImage = cv2.GaussianBlur(img, (7,7),0)
cv2.imshow("M.faraz", bluredImage)
cv2.waitKey(0)
# (src: MatLike, ksize: Size, sigmaX: float, dst: MatLike | None = ..., sigmaY: float = ..., borderType: int = ...) -> MatLike






import numpy as np

img = cv2.imread("resources/AHS0cc2566.jpg")
img = cv2.resize(img,(600,600))
cv2.imshow("Mohammad faraz" , img)
cannyImg = cv2.Canny(img,200,600)
cv2.imshow("Mohammad faraz canny" , cannyImg)
cv2.imwrite("D:\\Faraz\\COMPUTER VISION PYTHON\\resources\\DownloadedImageFromPYTHON.png",cannyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()








import cv2

img = cv2.imread("resources/AHS0cc2566.jpg")
img = cv2.resize(img,(600,600))

newImg = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
cv2.imshow("imggg", newImg)
cv2.waitKey(0)
cv2.imwrite("D:\\Faraz\\COMPUTER VISION PYTHON\\resources\\newImg.png", newImg)










import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

orignalImg = cv2.imread("resources/AHS02274.JPG")
print(orignalImg.shape)
orignalImg=cv2.resize(orignalImg,(720,720))
versionOneImage = orignalImg.copy()
versionTwoImage = orignalImg.copy()
versionThreeImage = orignalImg.copy()

print(versionOneImage.shape)
versionOneImage[:,:,0] = 0
versionTwoImage[:,:,1] = 0
versionThreeImage[:,:,2] = 0
versionOneImage.crop((0,0,500,500))
print(versionOneImage.shape)
cv2.imshow("v 1",versionOneImage)
cv2.imshow("v 2",versionTwoImage)
cv2.imshow("v 3",versionThreeImage)

cv2.waitKey(0)













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







                                                            #   FAILD ATTEMPT
                                                            #   FAILD ATTEMPT
                                                            #   FAILD ATTEMPT


import cv2
import numpy as np

OfficialImage = cv2.imread('resources/AHS0cc2566.jpg')
OfficialImageArray = np.array(OfficialImage)

RandomArray = np.array([[117, 153, 177],[117, 154, 176],[115, 154, 176]])
print("Array to be added  \n" , RandomArray)
print("this is offical Image Array", OfficialImageArray)
OfficialImageArray = np.delete(OfficialImageArray,0)
FinalArray = np.hstack((RandomArray, OfficialImageArray))
print("this is Final Image Array", FinalArray)













import cv2

img = cv2.imread("resources/AHS02274.JPG")
img = cv2.resize(img,(600,600))
cropImg = img[:250,:250]

cv2.imshow("Mohammd Faraz", img)
cv2.imshow("Ayzel", cropImg)

cv2.waitKey(0)











import cv2

myImage = cv2.imread("resources/AHS0cc2566.jpg")
myImage = cv2.resize(myImage,(600,700))
rectangleImage = cv2.rectangle(myImage,(5000,5000),(1500,25000),(0,255,0),-1,3,4)
cv2.imshow("Faraz",rectangleImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
#(img: MatLike, pt1: Point, pt2: Point, color: Scalar, thickness: int = ..., lineType: int = ..., shift: int = ...) -> MatLike











import cv2
import numpy as np

# cap = cv2.VideoCapture("resources/y2mate.is - आज का बादशाह तू... कोई बिच में नहीं आएगा - Sunny Deol Action Scene - Ghatak Movie Best Scene-6qJnTjrWA1I-720p-1711913877.mp4")
# image = cv2.imread("resources/AHS0cc2566.jpg")
# cv2.imshow("iiimmgg", image)
# cap = cv2.VideoCapture(1)
# cap.set(3,640)
# cap.set(4,480)
# while True:
#     success, img = cap.read()
#     if cv2.waitKey(1) & 0xFF ==ord("q"):
#         break
img = cv2.imread("resources/AHS0cc2566.jpg")
imageResize = cv2.resize(img,(1080,920))
print(img.shape)
print(imageResize.shape)
cv2.imshow("imag resize",imageResize)
cv2.imshow("image",img)
cv2.waitKey(0)












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







import cv2
import numpy as np

cap = cv2.VideoCapture(r"D:\\Downloads\\Downloads\\MOV_0142.mp4")

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












import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

ListOfImage = os.listdir(r"D:\Faraz\COMPUTER VISION PYTHON\resources")
print(ListOfImage)
for name in ListOfImage:
    Locate = "D:\\Faraz\\COMPUTER VISION PYTHON\\resources"
    path = Locate +"\\"+name
    imgLoop = cv2.imread(path)
    imgLoop = cv2.resize(imgLoop,(500,600)) 
    cv2.imshow("Loop", imgLoop)
    cv2.waitKey(4000)












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











import cv2

image = cv2.imread("resources/AHS0cc2566.jpg")
image = cv2.resize(image,(600,700))
imageTxt= cv2.putText(image,"Faraz",(50,100),2,4.1,(255,0,0),4,3,False)
#(img: MatLike, text: str, org: Point, fontFace: int, fontScale: float, color: Scalar, thickness: int = ..., lineType: int = ..., bottomLeftOrigin: bool = ...) -> MatLike
cv2.imshow("Mohammad Faraz", imageTxt)
cv2.waitKey(0)