import cv2
import numpy as np
from matplotlib import pyplot as plt

filename='oudan.jpg'
img=cv2.imread(filename)

img_lowres=cv2.pyrDown(img)

gray=cv2.cvtColor(img_lowres,cv2.COLOR_BGR2GRAY)

s = cv2.xfeatures2d.SIFT_create()
mask=uint8(ones(gray.shape))
keypoints=s.detect(gray,mask)

vis=cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
for k in keypoint[::10]:
    cv2.circle(vis,int(k.pt[0]),int(k.pt[1]),2,(0,255,0),-1)
    cv2.circle(vis,int(k.pt[0]),int(k.pt[1]),int(k.size),(0,255,0),2)

cv2.imshow('local descriptors',vis)
cv2.waitKey()
