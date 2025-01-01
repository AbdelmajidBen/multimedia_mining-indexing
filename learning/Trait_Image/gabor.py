import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_gabor_filters():
    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 4):
        for sigma in (1, 3, 5):
            lamda = np.pi / 4
            gamma = 0.5
            psi = 0
            kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, psi, ktype=cv2.CV_32F)
            filters.append(kernel)
    return filters

def apply_gabor_filters(image, filters):
    responses = []
    for kernel in filters:
        response = cv2.filter2D(image, cv2.CV_8UC3, kernel)
        responses.append(response)
    return responses

def characterize_texture(responses, roi):
    stats = []
    for response in responses:
        roi_response = response[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
        mean = roi_response.mean()
        std = roi_response.std()
        stats.append((mean, std))
    return stats

def classify_texture(image, responses, texture_stats):
    binary_image = np.zeros_like(image, dtype=np.uint8)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            pixel_stats = [response[y, x] for response in responses]
            distances = [np.sqrt((pixel_stats[i] - texture_stats[i][0])**2) for i in range(len(texture_stats))]
            if np.mean(distances) < 20:
                binary_image[y, x] = 255
    return binary_image

def main():
    image = cv2.imread('lab6/Image/c.jpg', cv2.IMREAD_GRAYSCALE)
    filters = create_gabor_filters()
    responses = apply_gabor_filters(image, filters)
    roi = cv2.selectROI("Select ROI", image)
    cv2.destroyWindow("Select ROI")
    texture_stats = characterize_texture(responses, roi)
    binary_image = classify_texture(image, responses, texture_stats)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.title("Image Originale")
    plt.imshow(image, cmap='gray')
    plt.subplot(1, 3, 2)
    plt.title("Image Binaire")
    plt.imshow(binary_image, cmap='gray')
    plt.subplot(1, 3, 3)
    plt.title("Réponse d'un Filtre")
    plt.imshow(responses[0], cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()
