import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("bruno_gray.jpg", cv2.IMREAD_GRAYSCALE)

thresholds = [80,120,160]
fig, axes = plt.subplots(1,4, figsize=(20,5))
axes[0].imshow(img, cmap='gray')
axes[0].set_title("Grayscale Original")
axes[0].axis('off')

for i,T in enumerate(thresholds):
 output = np.zeros_like(img, dtype=np.uint8)
 for j in range(img.shape[0]):
    for k in range(img.shape[1]):
        pixel = img[j][k]
        if pixel > T :
           output[j][k] = 255
        else :
           output[j][k] = 0

 axes[i + 1].imshow(output, cmap='gray')
 axes[i + 1].set_title(f"Threshold T={T}")
 axes[i + 1].axis('off')

plt.tight_layout()
plt.show()





        


