import cv2
import time
import numpy as np
video=cv2.VideoCapture(0)
'''check,frame=video.read()
print(frame)
print(check)'''
a=1
while True:
    a=a+1
    check,frame=video.read()
    print(frame)
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    

#print(a)
video.release()
cv2.destroyAllWindows()
