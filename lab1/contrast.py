import cv2
import numpy as np

# Function to adjust contrast
def adjust_contrast(image, alpha):
    # Clip ensures pixel values are within 0-255
    return np.clip(alpha * image, 0, 255).astype(np.uint8)

# Callback function for trackbar (does nothing, just required for trackbar to work)
def nothing(x):
    pass

# Load the image
image = cv2.imread('/Users/mac/Desktop/MST AISD/S3/mutimedia mining/multimedia-mining-indexing labs/lab1/images/im1.jpg')

# Set the height and width to minus 50%
height, width = image.shape[:2]
new_height = int(height * 0.5)
new_width = int(width * 0.5)
resized_image = cv2.resize(image, (new_width, new_height))


# Check if image loaded properly
if image is None:
    print("Error: Unable to load image.")
    exit()

# Create a window
cv2.namedWindow('Contrast Adjustment')

# Create trackbar to control contrast (alpha value from 1 to 3 with step of 0.01)
cv2.createTrackbar('Contrast', 'Contrast Adjustment', 100, 300, nothing)

# Loop until the user presses 'q' to exit
while True:
    # Get the current trackbar position (scale down to 1.0-3.0)
    alpha = cv2.getTrackbarPos('Contrast', 'Contrast Adjustment') / 100.0
    
    # Adjust the contrast
    adjusted_image = adjust_contrast(resized_image, alpha)
    
    # Display the image with adjusted contrast
    cv2.imshow('Contrast Adjustment', adjusted_image)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Cleanup and close windows
cv2.destroyAllWindows()