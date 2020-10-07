import matplotlib.pyplot as plt
import numpy as np
import cv2


img=cv2.imread('D:\only memories/babbi.jpg',0)
_,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,50,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,50,255,cv2.THRESH_TOZERO_INV)

titles=['Original Image','Binary','Binary_inv','Trunc','Tozero','Tozero_inv']
images=[img,th1,th2,th3,th4,th5]


for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])



plt.savefig('plot.png')
plt.show()



#img=cv2.imread('D:\only memories/babbi.jpg',-1)
#cv2.imshow('image',img)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.imshow(img)
#plt.xticks([]),plt.yticks([])
#plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()

