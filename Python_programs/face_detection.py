import cv2
import numpy as np
import matplotlib.pyplot as plt
'''create a cascadeClassifier object taken from a path to the XML file \
which contains the face features'''
face_cascade=cv2.CascadeClassifier("D:\Python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
#Reading the image as it is
img=cv2.imread("D:\Python programs\capture2.png")

#Reading the image as gray scale image i.e converting from color to gray img
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#search the co-ordinates of the image
#detectMultiScale->method to search for the face rectangle coordinates
'''Here scaleFactor decreases the shape value by 5%, until the face is found'''
#Smaller the scaleFactor value, greater the accuracy
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    #rectangle is a method to create the face rectangle
    #img->image object
    #(255,0,0)->RGB value of rectangle outline....Here it is red
    #3->Width of the rectangle

def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

resized=cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))
plt.imshow(convertToRGB(img))
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
