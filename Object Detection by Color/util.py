
import cv2
import numpy as np

def get_limits(color):
    c=np.uint8([[color]])
    hsvC=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    H = hsvC[0][0][0]

    lowerLimit = np.array([max(H - 10,0),100,100],dtype=np.uint8)
    upperLimit = np.array([min(H + 10,179),255,255],dtype=np.uint8)

   
   

    return lowerLimit,upperLimit
    

