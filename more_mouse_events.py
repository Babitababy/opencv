import numpy as np
import cv2

def click_event(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        myColorImage=np.zeros((512,512,3),np.uint8)
        myColorImage[:]=[blue,green,red]
        cv2.imshow('myColorImage',myColorImage)
        #cv2.circle(img,(x,y),3,(0,0,255),-1)#center,radius,thickness
       # points.append(x,y)
       # if len(points) >=2:
           # cv2.line(img,points[-1],points[-2],(255,0,0),5)
        #cv2.imshow('image',img)

#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('D:\only memories/babbi.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
#points=[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()




