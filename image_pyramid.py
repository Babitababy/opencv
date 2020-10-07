import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('D:\only memories/babbi.jpg')
layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer=gp[5]
cv2.imshow('Upper Level',layer)
lp=[layer]

for i in range(5,0,-1):
    layer = cv2.pyrUp(layer)
    lp.append(layer)
    cv2.imshow(str(i),layer)



#lr1=cv2.pyrDown(img)
#lr2=cv2.pyrDown(lr1)
#lr3=cv2.pyrDown(lr2)
#lr4=cv2.pyrUp(lr3)
#cv2.imshow("original image",img)
#cv2.imshow("PyrDown1",lr1)
#cv2.imshow("PyrDown2",lr2)
#cv2.imshow("PyrDown3",lr3)
#cv2.imshow("PyrUp",lr4)

cv2.waitKey(0)
cv2.destroyAllWindows()
