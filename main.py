from color_detection import *
import cv2
import com
print(f'waiting aduino signal')
arduino_msg=0
# [3,89,68]
# [212,238,247]
#####################################################################
'''
Check image input
'''
# img = cv2.imread('img1.jpeg')
# img_rescale = rescale_frame(img,50)
# x1,y1,w,h,x,y,img_detection = detect(img_rescale)
# cv2.circle(img_detection,(x,y),5,(255,5,5),-1)
# # cv2.circle(img_detection,(x2,y2),5,(255,5,5),-1)
# roi =img[y-(y+h),x-(x+w)]
# cv2.imshow('roi',roi)
# cv2.imshow('object',img_detection)
# cv2.waitKey()
####################################################################
'''
Main program Input webcam
'''
cap = cv2.VideoCapture(2)
arduino_msg=com.get()
print("arduino_msg : ", arduino_msg)
while(arduino_msg):
    _,frame=cap.read()
    img_rescale = rescale_frame(frame,100)
    x,y,img_detection ,luas= detect(img_rescale)
    cv2.circle(img_detection,(x,y),5,(255,5,5),-1)
    cv2.imshow('object',img_detection)
    print(f'sent X:{x},Y:{y},Luas:{luas}')
    if luas>130000:
        print("done")
        break
    else:
        pass
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
cap.release()
cv2.destroyAllWindows()