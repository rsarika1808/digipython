
#pip insall opencv-contrib-python mediapipe

import cv2
from datetime import datetime as dt

cam =cv2.videocapture(0)
font=cv2.FONT_HERSHEY_SIMPLEX
color_black =(0,0,0)#black
color_white=(225,255,255)#white

while cam.isOpened():
    status, image =cam.read()
    h,w,_=image.shape
    print(w,h)
    if status:
        #draw a box
        cv2. rectangle(image,(10,40),(300,100),(0,255),2)
        #add text
        cv2.putText(image,"Live camera Feed",(10,30),font,1,color_black,2 )
        #draw a clock 
        timestr =dt.now().strftime("%H:%M%S")
        cv2.putText(image,timestr,(10,70),font,1,color_black,2)
        cv2. imshow("Live Camera",image)
        if cv2.waitKey(1)==27:#27 is the ASCII code for the Escape key
            break
cam.release()
cv2.destroyAllwindow()

    