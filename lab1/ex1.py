import cv2
import numpy as np

def nothing(x):
    pass

image = cv2.imread('/Users/mac/Desktop/MST AISD/S3/mutimedia mining/multimedia-mining-indexing labs/lab1/images/im1.jpg')

# Convert the image to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a window and trackbars for adjusting HSV ranges
cv2.namedWindow('Image')

cv2.createTrackbar('H Lower', 'Image', 0, 179, nothing)
cv2.createTrackbar('H Upper', 'Image', 179, 179, nothing)
cv2.createTrackbar('S Lower', 'Image', 0, 255, nothing)
cv2.createTrackbar('S Upper', 'Image', 255, 255, nothing)
cv2.createTrackbar('V Lower', 'Image', 0, 255, nothing)
cv2.createTrackbar('V Upper', 'Image', 255, 255, nothing)

while True:
    h_lower = cv2.getTrackbarPos('H Lower', 'Image')
    h_upper = cv2.getTrackbarPos('H Upper', 'Image')
    s_lower = cv2.getTrackbarPos('S Lower', 'Image')
    s_upper = cv2.getTrackbarPos('S Upper', 'Image')
    v_lower = cv2.getTrackbarPos('V Lower', 'Image')
    v_upper = cv2.getTrackbarPos('V Upper', 'Image')

    lower_hsv = np.array([h_lower, s_lower, v_lower])
    upper_hsv = np.array([h_upper, s_upper, v_upper])

    mask = cv2.inRange(hsv_image, lower_hsv, upper_hsv)

    cv2.imshow('Image', mask)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()
