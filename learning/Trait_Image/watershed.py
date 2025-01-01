import cv2
import numpy as np
from queue import Queue

def watershed_segmentation(image, markers=None):
    if len(image.shape) > 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
    # Création de la carte des étiquettes
    labels = np.zeros_like(gray, dtype=np.int32)
    if markers is not None:
        labels = markers.copy()
    # Trier les pixels par intensité
    height, width = gray.shape
    pixels = [(gray[i, j], i, j) for i in range(height) for j in range(width)]
    pixels.sort(key=lambda x: x[0])
    # File d'attente pour les pixels à traiter
    queue = Queue()
    current_label = 1
    # Directions pour vérifier les voisins (8-connectivité)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    # Traitement des pixels par ordre croissant d'intensité
    for intensity, i, j in pixels:
        if labels[i, j] != 0:  # Pixel déjà étiqueté
            continue
    
        # Vérifier les voisins
        neighbor_labels = set()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                if labels[ni, nj] > 0:
                    neighbor_labels.add(labels[ni, nj])
        
        if len(neighbor_labels) == 0:
            # Nouveau bassin
            labels[i, j] = current_label
            current_label += 1
            queue.put((i, j))
        elif len(neighbor_labels) == 1:
            # Appartient à un bassin existant
            labels[i, j] = neighbor_labels.pop()
            queue.put((i, j))
        else:
            # Ligne de partage des eaux
            labels[i, j] = -1
            
        # Propager les étiquettes aux voisins de même intensité
        while not queue.empty():
            ci, cj = queue.get()
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if (0 <= ni < height and 0 <= nj < width and 
                    labels[ni, nj] == 0 and gray[ni, nj] <= intensity):
                    labels[ni, nj] = labels[ci, cj]
                    queue.put((ni, nj))
    
    return labels

def create_watershed_visualization(image, labels):
    result = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR) if len(image.shape) == 2 else image.copy()
    
    result[labels == -1] = [0, 0, 255]
    for label in range(1, labels.max() + 1):
        color = np.random.randint(0, 255, 3)
        mask = labels == label
        result[mask] = result[mask] * 0.7 + color * 0.3
        
    return result

def apply_watershed(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    denoised = cv2.GaussianBlur(image, (5, 5), 0)
    
    labels = watershed_segmentation(denoised)
    
    result = create_watershed_visualization(image, labels)
    return image, result

image_originale, image_segmentee = apply_watershed("learning/Images/im7.png")
cv2.imshow("Original", image_originale)
cv2.imshow("Segmentée", image_segmentee)
cv2.waitKey(0)
cv2.destroyAllWindows()