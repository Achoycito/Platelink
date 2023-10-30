import cv2

run = True

while(run):
    
    img = cv2.imread("NA102.jpeg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY", gray)

    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
    cv2.imshow("BILATERAL FILTER", bfilter)

    edged = cv2.Canny(bfilter, 30, 200)
    cv2.imshow("CANNY", edged)


    

    # hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # cv2.imshow('HSV', hsv_image)
    # cv2.imshow('Hue channel', hsv_image[:,:,0])
    # cv2.imshow('Saturation', hsv_image[:,:,1])
    # cv2.imshow('Value', hsv_image[:,:,2])
    
    
    k = cv2.waitKey(5)
    if k == 27:
        run = False