import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_contrasts(image):
    print(image.shape)
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    norm_image = image / 255.0

    global_contrast = norm_image.max() - norm_image.min()

    kernel_size = 3  
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size * kernel_size)
    local_mean = cv2.filter2D(norm_image, -1, kernel)
    local_contrast = np.mean(np.abs(norm_image - local_mean))

    rms_contrast = np.sqrt(np.mean((norm_image - norm_image.mean()) ** 2))

    return global_contrast, local_contrast, rms_contrast

image_path = 'learning/Images/im1.jpg' 
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

global_contrast, local_contrast, rms_contrast = compute_contrasts(image)

print(f"Global Contrast: {global_contrast:.4f}")
print(f"Local Contrast: {local_contrast:.4f}")
print(f"RMS Contrast: {rms_contrast:.4f}")

plt.figure(figsize=(6, 6))
plt.title("Grayscale Image")
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()
