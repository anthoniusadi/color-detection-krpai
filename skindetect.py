#import the necessary packages
import cv2
import numpy as np
# from mainprog import detect 
def nothing(x):
    pass
#'optional' argument is required for trackbar creation parameters
def rescale_frame(frame,percent=100):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim = (width,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
def detect(frame):
    imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    min_HSV = np.array([0, 40, 66], dtype = "uint8")
    max_HSV = np.array([207, 248, 248], dtype = "uint8")
    skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)
    skinHSV = cv2.bitwise_and(frame, frame, mask = skinRegionHSV)    
    return skinHSV
#Capture video from the stream
cap = cv2.VideoCapture(2)
# img = cv2.imread('img1.jpeg')
# frame = rescale_frame(img,50)
cv2.namedWindow('Colorbars') #Create a window named 'Colorbars'
#assign strings for ease of coding
hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'
wnd = 'Colorbars'
#Begin Creating trackbars for each
cv2.createTrackbar(hl, wnd,0,255,nothing)
cv2.createTrackbar(hh, wnd,0,255,nothing)
cv2.createTrackbar(sl, wnd,0,255,nothing)
cv2.createTrackbar(sh, wnd,0,255,nothing)
cv2.createTrackbar(vl, wnd,0,255,nothing)
cv2.createTrackbar(vh, wnd,0,255,nothing)
while(1):
    #read the streamed frames (we previously named this cap)
    _,frame=cap.read()
 
    #it is common to apply a blur to the frame
    frame=cv2.GaussianBlur(frame,(3,3),0)

    #convert from a BGR stream to an HSV stream
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #read trackbar positions for each trackbar
    hul=cv2.getTrackbarPos(hl, wnd)
    huh=cv2.getTrackbarPos(hh, wnd)
    sal=cv2.getTrackbarPos(sl, wnd)
    sah=cv2.getTrackbarPos(sh, wnd)
    val=cv2.getTrackbarPos(vl, wnd)
    vah=cv2.getTrackbarPos(vh, wnd)

    #make array for final values
    HSVLOW=np.array([hul,sal,val])
    HSVHIGH=np.array([huh,sah,vah])

#create a mask for that range
    mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
    res = cv2.bitwise_and(frame,frame, mask =mask)

    edge = cv2.Canny(res,30,100,3)
    
    contours, hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    
    cv2.imshow('edge',edge)
    cv2.imshow(wnd, res)
    cv2.imshow('ori', hsv)
    
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    cv2.imshow('contour',frame)
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break

cap.release()
cv2.destroyAllWindows()