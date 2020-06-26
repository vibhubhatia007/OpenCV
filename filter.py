import cv2
import numpy as np

image = cv2.imread("picture.png", -1)
#picture you want to add
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

nose_cascade = cv2.CascadeClassifier("Nose18x15.xml")
eyes_cascade = cv2.CascadeClassifier("frontalEyes35x16.xml")
nose = nose_cascade.detectMultiScale(img, 1.3, 5) 
nose


x,y,w,h = nose[0]
cv2.rectangle(img, (x,y), (x+h, y+w), (0,255,255), 2)

cv2.imshow("nose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

eyes = eyes_cascade.detectMultiScale(img, 1.3, 5)
eyes

glasses=cv2.imread("glasses.png",-1) 
cv2.imshow("glasses", glasses)
cv2.waitKey(0)
cv2.destroyAllWindows()

mustache=cv2.imread("mustache.png",-1)
cv2.imshow("mustache", mustache)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image.shape
mustache.shape
glasses.shape

x,y,w,h = eyes[0]
glasses = cv2.resize(glasses, (h,w))

w,h,c = glasses.shape

for i in range(0, w):
    for j in range(0, h):
        if glasses[i,j][3]!=0:
            image[y+i,x+j]=glasses[i,j]
            
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

x,y,w,h = nose[0]
img_section = img[y+(w//2+22):y+w, x:x+h]
cv2.imshow("img_section", img_section)
cv2.waitKey(0)
cv2.destroyAllWindows()

W=(w//2+22)
H=h
mustache=cv2.resize(mustache, (H,W))
cv2.imshow("mustache", mustache)
cv2.waitKey(0)
cv2.destroyAllWindows()

x,y,w,h=nose[0]
W,H,c = mustache.shape
y=y+(w//2-5)

for i in range(0, W):
    for j in range(0,H):
        if mustache[i,j][3]!=0:
            image[y+i,x+j]=mustache[i,j]
            
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("new Image pixel values:-")
print(image)

import matplotlib.pyplot as plt

coloured = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)
plt.imshow(coloured)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
