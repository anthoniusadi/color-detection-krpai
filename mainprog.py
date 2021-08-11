# Required modules
import cv2
import numpy as np

def detect(frame):
    imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    min_HSV = np.array([0, 40, 66], dtype = "uint8")
    max_HSV = np.array([207, 248, 248], dtype = "uint8")
    skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)
    skinHSV = cv2.bitwise_and(frame, frame, mask = skinRegionHSV)    
    return skinHSV
cap = cv2.VideoCapture('video2.mp4')
while True:
    _,frame = cap.read()
#    frame = cv2.imread('/root/PySkinDetection/src/compare.png')
    # YCbCr_image = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    # binary_mask_image = imageHSV
    frame=cv2.GaussianBlur(frame,(3,3),0)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # lower_YCbCr_values = np.array((0, 138, 67), dtype = "uint8")
    # upper_YCbCr_values = np.array((255, 173, 133), dtype = "uint8")
    
    # mask_YCbCr = cv2.inRange(YCbCr_image, lower_YCbCr_values, upper_YCbCr_values)
    # mask_HSV = cv2.inRange(imageHSV, min_HSV, max_HSV) 
    # binary_mask_image = cv2.add(mask_HSV,mask_YCbCr)

    # # Get pointer to video frames from primary device
    # image_foreground = cv2.erode(binary_mask_image,None,iterations = 3)     	#remove noise
    # dilated_binary_image = cv2.dilate(binary_mask_image,None,iterations = 3)   #The background region is reduced a little because of the dilate operation
    # ret,image_background = cv2.threshold(dilated_binary_image,1,128,cv2.THRESH_BINARY)  #set all background regions to 128
    # image_marker = cv2.add(image_foreground,image_background)   ##add both foreground and backgroud, forming markers. The markers are "seeds" of the future image regions.
    # image_marker32 = np.int32(image_marker) #convert to 32SC1 format

    # cv2.watershed(frame,image_marker32)
    # m = cv2.convertScaleAbs(image_marker32) #convert back to uint8 

	# 	#bitwise of the mask with the input image
    # ret,image_mask = cv2.threshold(m,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # output = cv2.bitwise_and(frame,frame,mask = image_mask)
        
    segmented = detect(frame)
    cv2.imshow("segmented",segmented)
    # cv2.imshow("binary",binary_mask_image)
    # cv2.imshow("watershed",output)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break

cap.release()
cv2.destroyAllWindows()
