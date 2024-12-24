import cv2
import numpy as np
from matplotlib import pyplot as plt


image_path = '/Users/mac/Desktop/MST AISD/S3/mutimedia mining/multimedia-mining-indexing labs/learning/Images/im1.jpg' 
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 1. Seuilage manuel
seuil_manuel = 127 
retour_manuel, image_binaire_manuel = cv2.threshold(image_gray, seuil_manuel, 255, cv2.THRESH_BINARY)

# 2. Seuilage avec la méthode d'Otsu

retour_otsu, image_binaire_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(10, 7))

# Image originale
plt.subplot(1, 3, 1)
plt.imshow(image_gray, cmap='gray')
plt.title('Image Originale')
plt.axis('off')

# Seuilage manuel
plt.subplot(1, 3, 2)
plt.imshow(image_binaire_manuel, cmap='gray')
plt.title(f'Seuilage Manuel (T={seuil_manuel})')
plt.axis('off')

# Seuilage Otsu
plt.subplot(1, 3, 3)
plt.imshow(image_binaire_otsu, cmap='gray')
plt.title('Seuilage Otsu')
plt.axis('off')

plt.show()
