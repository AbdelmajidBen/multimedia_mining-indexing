import cv2
import numpy as np
from matplotlib import pyplot as plt


# Charger une image en niveaux de gris
image = cv2.imread('learning/Images/im4.jpeg', cv2.IMREAD_GRAYSCALE)


# Étape 1 : Réduction du bruit
blurred = cv2.GaussianBlur(image, (5, 5), 0)


# Étape 2 : Détection automatique des seuils
median_intensity = np.median(blurred)  


# Fixer les seuils automatiquement en fonction de l'intensité médiane
low_threshold = int(max(0, 0.44 * median_intensity))
high_threshold = int(min(255, 1.33 * median_intensity))


# Étape 3 : Appliquer l'algorithme de Canny
edges = cv2.Canny(blurred, low_threshold, high_threshold)


# Visualisation des résultats
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.title('Image originale')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title(f'Contours détectés (Canny) \nSeuils: [{low_threshold}, {high_threshold}]')
plt.imshow(edges, cmap='gray')

plt.tight_layout()
plt.show()
