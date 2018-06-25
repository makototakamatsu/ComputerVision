
import cv2
import numpy as np

img1=cv2.imread('right.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('left.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

stereo = cv2.StereoBM_create(numDisparities = 16, blockSize = 17)
disparity = stereo.compute(img1, img2)

cv2.imshow('DepthMap', disparity)
cv2.waitKey()
cv2.destroyAllWindows()
