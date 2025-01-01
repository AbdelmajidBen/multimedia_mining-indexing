import cv2
from matplotlib import pyplot as plt


def compute_inversion(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Read all pixels
    height, width = image.shape
    for y in range(height):
        for x in range(width):
            pixel = image[y, x]
            pixel = 255-pixel
            image[y, x] = pixel
    return image

            
image_path = 'learning/Images/im1.jpg' 
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)           
new=compute_inversion(image)

plt.imshow(new, cmap='gray')
plt.title("Inverted Image")
plt.show()