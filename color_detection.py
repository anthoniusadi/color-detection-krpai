#import the necessary packages
import cv2
import numpy as np

def nothing(x):
    pass

def rescale_frame(frame,percent=100):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim = (width,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

def detect(frame):
    kernel = np.ones(4)
    cx,cy =0 , 0
    luas=0
    
    frame=cv2.GaussianBlur(frame,(3,3),0)
    imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    min_HSV = np.array([0,85,65], dtype = "uint8")
    max_HSV = np.array([212,238,255], dtype = "uint8")
    skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)
    skinHSV = cv2.bitwise_and(frame, frame, mask = skinRegionHSV)  
    erosi = cv2.erode(skinHSV,kernel,iterations=1)
    dilasi = cv2.dilate(erosi,kernel,iterations=5)
    edge = cv2.Canny(dilasi,30,100,3)
    contours, hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        luas = (y-(y+h))*(x-(x+w))
        
        # roi =frame[y:y+h,x:x+w]
        
        # cv2.imshow('roi',roi)
        if(luas>18700):
            # print(f'koordinat : {x,y}, luasan : {w,h}, luas : {luas}' )
            M = cv2.moments(c)
            if M['m00'] != 0:
                # cx1= int(M['m01'])
                # cx2= int(M['m00'])
                # cx3= int(M['m10'])
                
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            else:
                cx,cy =0 , 0
        else:
            cx,cy=0,0
    
    # print(f'X:{cx},Y:{cy}')
    # print(f'X:{cx1},Y:{cx2},{cx3}')
    return cx,cy,dilasi,luas
#Capture video from the stream
# cap = cv2.VideoCapture(2)
# img = cv2.imread('img1.jpeg')
# frame = rescale_frame(img,50)


# frame=cv2.GaussianBlur(frame,(3,3),0)

# res = detect(frame)
# edge = cv2.Canny(res,30,100,3)

# contours, hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# for c in contours:
#     M = cv2.moments(c)
#     if M['m00'] != 0:
#         cx = int(M['m10']/M['m00'])
#         cy = int(M['m01']/M['m00'])
#     else:
#         cx,cy =0 , 0
# print(f'X:{cx},Y:{cy}')
# cv2.circle(res,(cx,cy),5,(255,5,5),-1)
# cv2.imshow('edge',edge)
# cv2.imshow('wnd', res)
# cv2.imshow('ori', hsv)

# cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
# cv2.imshow('contour',frame)
# interrupt = cv2.waitKey()
# if interrupt & 0xFF == 27: # esc key
#     break

# cap.release()
# cv2.destroyAllWindows()