import cv2
import numpy as np

img1=cv2.imread('D:\only memories/babbi.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('D:\only memories/baby.jpg',cv2.IMREAD_COLOR)
#add=img1+img2
#add=cv2.add(img1,img2)

#weighted=cv2.addWeighted(img1,0.4,img2,0.6,0)

#cv2.imshow('Add',add)
#cv2.imshow('Weighted',weighted)

#rows,cols,channels=img2.shape
#roi=img1[0:rows,0:cols]

#img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('Mask',mask)

print(img2.shape)
print(img2.size)
print(img2.dtype)
b,g,r=cv2.split(img2)
img2=cv2.merge((b,g,r))

#ball=img2[100:100,100:100]
#img2[273:333,100:160]=ball
#cv2.imshow('Image',img2)
img1=cv2.resize(img1,(512,512))
img2=cv2.resize(img2,(512,512))

#add=cv2.add(img1,img2)
add=cv2.addWeighted(img1,.4,img2,.6,0)


cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()




