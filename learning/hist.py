import cv2
import matplotlib.pyplot as plt


def calculate_hist(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the histogram
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    
    # Display the histogram
    plt.plot(hist)
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

image_path = 'learning/Images/im1.jpg'
image = cv2.imread(image_path)

# Call the calculate_hist function
calculate_hist(image)




