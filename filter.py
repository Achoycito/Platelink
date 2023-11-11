import cv2
import imutils
import numpy as np

run = True

while(run):
    
    img = cv2.imread("NA102.jpeg")
    # img = cv2.imread("102fil.png")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY", gray)

    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
    cv2.imshow("BILATERAL FILTER", bfilter)

    edged = cv2.Canny(bfilter, 50, 200)
    cv2.imshow("CANNY", edged)

    hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV', hsv_image)
    cv2.imshow('Hue channel', hsv_image[:,:,0])
    cv2.imshow('Saturation', hsv_image[:,:,1])
    cv2.imshow('Value', hsv_image[:,:,2])


    # keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contours = imutils.grab_contours(keypoints)
    # contours = sorted(contours, key=cv2.contourArea, reverse = True)[:10]

    # location = None
    # for contour in contours:
    #     approx = cv2.approxPolyDP(contour, 10, True)
    #     if len(approx) == 4:
    #         location = approx
    #         break

    # mask = np.zeros(gray.shape, np.uint8)
    # new_image = cv2.drawContours(mask, [location], 0,255,-1)
    # new_image = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("FINAL SEGUN", cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    
    
    k = cv2.waitKey(5)
    if k == 27:
        run = False