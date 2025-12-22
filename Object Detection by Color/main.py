import cv2
from util import get_limits
from PIL import Image
cam=cv2.VideoCapture(0)
color=[255,255,0]
while True:
    ret,frame=cam.read()

    hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lowerLimit,upperLimit = get_limits(color)

    mask=cv2.inRange(hsv_img,lowerLimit,upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1,y1,x2,y2=bbox
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()