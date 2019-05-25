import cv2
import numpy as np
# img = cv2.imread('E:pythoneeLearnOpenCV\test222.jpg',1)
img = cv2.imread('/home/python/Desktop/kk.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dstImg = np.zeros((height,width,1),np.uint8)
# 算法：newPixel = grayCurrentPixel - grayNextPixel + 150
for i in range(0,height):
 for j in range(0,width-1):
  grayCurrentPixel = int(gray[i,j])
  grayNextPixel = int(gray[i,j+1])
  newPixel = grayCurrentPixel - grayNextPixel + 150
  # if newPixel > 255:
  if newPixel > 255:
   newPixel = 255
  if newPixel < 0:
   newPixel = 0
  dstImg[i,j] = newPixel
cv2.imshow('dstImg',dstImg)
cv2.waitKey(0)
