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