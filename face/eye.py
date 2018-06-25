import cv2

cascade_path = "./haarcascade_frontalface_alt.xml"
#cascades_path="./haarcascade_eye.xml"
#ここに任意の画像を入れる
image_file = "6001.jpg"
image_path = "./inputs/" + image_file
output_path = "./outputs/" + image_file

import os
print(os.path.exists(image_path))

image = cv2.imread(image_path)

cascade = cv2.CascadeClassifier(cascade_path)
#cascades = cv2.CascadeClassifier(cascades_path)

facerect = cascade.detectMultiScale(image, scaleFactor=1.2, minNeighbors=2, minSize=(100, 100))
print(facerect)
color = (255, 255, 255)
if len(facerect) > 0:

    for rect in facerect:
        cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
#facerect = cascades.detectMultiScale(image, scaleFactor=1.2, minNeighbors=1, minSize=(100, 100))
        #print(facerect)
        #color = (255, 255, 255)
        #if len(facerect) > 0:
            #for rect in facerect:
                #cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
    #for (x,y,w,h) in faces:
    #img = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    #roi_color = img[y:y+h, x:x+w]
    #eyes = cascades.detectMultiScale(roi_color)
    #for (ex,ey,ew,eh) in eyes:
    #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imwrite(output_path,image)
