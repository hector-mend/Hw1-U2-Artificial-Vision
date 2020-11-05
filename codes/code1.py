#From the following image: Find the skeleton of the image.
#Fill the image until you obtain the circles with no black spaces between them.

#Libraries
import cv2
import numpy as np

# Read image in grayscale
img_org = cv2.imread('circles.jpg')
img = cv2.imread('circles.jpg', 0)

#Threshold
ret,img = cv2.threshold(img, 127, 255, 0)

#Empty skeleton
size = np.size(img)
kel = np.zeros(img.shape, np.uint8)
kernel = np.ones((5,5), np.uint8) 

#Cross shaped Kernel
elem = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
dil_img = cv2.dilate(img, kernel, iterations=2)

while True:
    #Open image.
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, elem)
    #Substraction from the original image
    temp = cv2.subtract(img, open)
    #Erotion of original image and refine the skeleton
    eroded = cv2.erode(img, elem)
    kel = cv2.bitwise_or(kel,temp)
    img = eroded.copy()
    #If image has been completely eroded, quit the loop
    if cv2.countNonZero(img)==0:
        break

#Print results
cv2.imshow("Original", img_org)
cv2.imshow("Skeleton", kel)
cv2.imshow('Dilation', dil_img) 

cv2.imwrite('Skeleton.jpg', kel)
cv2.imwrite('Dilation.jpg', dil_img)

cv2.waitKey(0)
cv2.destroyAllWindows()