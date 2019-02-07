# -*- coding: utf-8 -*-

import cv2
'''
imgc =cv2.imread("sharan.jpg",1)
print('color image ',imgc)
imgg=cv2.imread("sharan.jpg",0)
print('Grey scale image ',imgg)
print('shape of image', imgc.shape)

cv2.imshow("Sharan",imgc)
cv2.waitKey(0)
#cv2.waitkey(2000)
cv2.destroyAllWindows()


resized_image=cv2.resize(imgc,(int(imgc.shape[1]/4),int(imgc.shape[0]/4)))

cv2.imshow("Sharan",resized_image)
cv2.waitKey(0)
#cv2.waitkey(2000)
cv2.destroyAllWindows()
'''

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img =cv2.imread("sharan.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))

cv2.imshow("Gray",resized)
cv2.waitKey(0)



