import cv2,time
import numpy as np
import pandas as pd
from datetime import datetime

first_frame= None
'''status_list=[None,None]
times=[]
df=pd.DataFrame(columns=["Start","End"])'''

video=cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    check,frame=video.read()
    print(frame)
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0) #Convert gray image to gaussian blur

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta=cv2.dilate(thresh_delta,None,iterations=3)
    cnts,_=cv2.findContours(thresh_delta.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)< 1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    '''status_list.append(status)
    status_list=status_list[-2:]

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    print(status_list)
    print(times)'''

    cv2.imshow('frame',frame)
    cv2.imshow('Capturing',gray)
    cv2.imshow('delta',delta_frame)
    cv2.imshow('thresh',thresh_delta)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    '''for i in range(0,len(times),2):
        df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

    df.to_csv("D:\Times.csv")'''

print(a)
video.release()
cv2.destroyAllWindows()
    

