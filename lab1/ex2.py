import cv2
import numpy as np


image = cv2.imread('/Users/mac/Desktop/MST AISD/S3/mutimedia mining/multimedia-mining-indexing labs/lab1/images/fondvert.png')
background = cv2.imread('/Users/mac/Desktop/MST AISD/S3/mutimedia mining/multimedia-mining-indexing labs/lab1/images/im1.jpg')  # Replace with your background image

background = cv2.resize(background, (image.shape[1], image.shape[0]))

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 40, 40]) 
upper_green = np.array([85, 255, 255])

mask = cv2.inRange(hsv_image, lower_green, upper_green)

mask_inv = cv2.bitwise_not(mask)

foreground = cv2.bitwise_and(image, image, mask=mask_inv)

background = cv2.bitwise_and(background, background, mask=mask)

result = cv2.add(foreground, background)

cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
