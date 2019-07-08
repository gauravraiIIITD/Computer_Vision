   
import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture  =cv2.VideoCapture(0)
while(True):
    i=0

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        i+= 1
        print (i)
        cv2.putText(frame,str(i),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,.7,(150,150,0),2)
        cv2.imshow('img',frame)
    if(cv2.waitKey(1)==ord('q')):
        break

frame.release()
cv2.destroyAllWindows()