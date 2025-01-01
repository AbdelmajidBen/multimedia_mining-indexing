import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "learning/Images/im4.jpeg"
image = cv2.imread(image_path)
if image is None:
    print(f"Erreur : Impossible de charger l'image {image_path}. Vérifiez le chemin.")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gaussian_filtered = cv2.GaussianBlur(gray_image, (9, 9), 0)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title("Image Originale (bruyante)")
plt.axis("off") 
plt.subplot(1, 2, 2)
plt.imshow(gaussian_filtered, cmap='gray')
plt.title("Image Filtrée (Gaussienne)")
plt.axis("off")

plt.tight_layout()
plt.show()
