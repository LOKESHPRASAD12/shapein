import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time

offset=20
imgSize=300

folder="Data/S"
counter= 0
labels=["A","B","C","K","N","P","R","S"]

cap=cv2.VideoCapture(0)
detector=HandDetector(maxHands=1)
classifier=Classifier("Model/keras_model.h5","Model/labels.txt")

while True:
    success, img =cap.read()
    imgOutput=img.copy()
    hands, img =detector.findHands(img)
    if hands:
        hand=hands[0]
        x,y,w,h=hand['bbox']


        imgWhite=np.ones((imgSize,imgSize,3),np.uint8)*255
        imgCrop=img[y-offset:y+h+offset,x-offset:x+w+offset]

        imgCropShape=imgCrop .shape

        aspectRatio=h/w

        if aspectRatio>1:
            k=imgSize/h
            wCal= math.ceil(k*w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap=math.ceil((imgSize-wCal)/2)
            # imgWhite[0:imgCropShape[0], 0:imgCropShape[1]] = imgCrop
            imgWhite[:, wGap:wCal+wGap] = imgResize
            prediction,index=classifier.getPrediction(imgWhite,draw=False)
            print(prediction,index)

        else:
            k=imgSize/w
            hCal= math.ceil(k*h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap=math.ceil((imgSize-hCal)/2)
            # imgWhite[0:imgCropShape[0], 0:imgCropShape[1]] = imgCrop
            imgWhite[hGap:hCal+hGap,:] = imgResize
            prediction, index = classifier.getPrediction(imgWhite,draw=False)
        cv2.rectangle(imgOutput,(x-offset,y-offset-100),(x-offset+50,y-offset-50+50),(255,255,255),cv2.FILLED)
        cv2.putText(imgOutput,labels[index],(x,y-25),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,0,255),2)
        cv2.rectangle(imgOutput,(x-offset,y-offset),(x+w+offset,y+h+offset),(255,0,255),4)

        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", imgOutput)
    cv2.waitKey(1)
    # if key==ord("s"):
    #     counter+=1
    #     cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
    #     print(counter)
