import numpy as np
import cv2
img=cv2.imread('D:\only memories/babbi.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0,),(150,150),(0,0,0),15)#start and ending point of the line with color
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)#top left corner , bottom right corner
cv2.circle(img,(100,63),55,(0,0,255),-1)#center and radius
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"OPENCV",(0,130),font,2,(200,255,255),5,cv2.LINE_AA)#spacing and thickness
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('drawing.png',img)

