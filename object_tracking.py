import cv2
import numpy as np
cap=cv2.VideoCapture(0)
def nothing(x):
    pass
cv2.namedWindow("tracking")
cv2.createTrackbar("UH","tracking",0,255,nothing)
cv2.createTrackbar("US","tracking",0,255,nothing)
cv2.createTrackbar("UV","tracking",0,255,nothing)

cv2.createTrackbar("HH","tracking",255,255,nothing)
cv2.createTrackbar("HS","tracking",255,255,nothing)
cv2.createTrackbar("HV","tracking",255,255,nothing)

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("UH","tracking")
    l_s=cv2.getTrackbarPos("US","tracking")
    l_v=cv2.getTrackbarPos("UV","tracking")

    h_h=cv2.getTrackbarPos("HH","tracking")
    h_s=cv2.getTrackbarPos("HS","tracking")
    h_v=cv2.getTrackbarPos("HV","tracking")

    lb=np.array([l_h,l_s,l_v])
    hb=np.array([h_h,h_s,h_v])

    mask=cv2.inRange(hsv,lb,hb)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    print(res)
    cv2.imshow('frame',frame)
    cv2.imshow('result',res)
    
    key=cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

    
    
