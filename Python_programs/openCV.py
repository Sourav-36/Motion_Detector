import cv2
'''provide path file. 1->colored img & 0->black and white img'''
img= cv2.imread("D:\lottery.gif",1)
'''TO reduce the size of image asymmetrically'''
#resized=cv2.resize(img,(600,550))
'''To reduce the size of image symmetrically''' #Can multiply and divide the img shape
resized=cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))
print(img)
print(type(img))
#<class nd.array> ->numpy array
print(img.shape)
#for colored img, its 3D array & for black n white, its 2D array shape
#cv2.imshow("Lottery photo",img)
cv2.imshow("Lottery photo",resized)  #show the image
'''Display the image. If 0 is written, then after pressing the key, the \
windows'll be destroyed along with the image'''
'''If any time other than 0 is mentioned in it..that means the windows will dissappear \
after those milliseconds'''
cv2.waitKey(0)
cv2.destroyAllWindows()
