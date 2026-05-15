import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("gray.jpg", cv2.IMREAD_GRAYSCALE)

#1. Compute and dispaly histogram of image:
histogram = np.zeros(256, dtype=int)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pixel = img[i][j]
        histogram[pixel] += 1

cdf = np.zeros(256, dtype = int)
cdf[0] = histogram[0]
for k in range(1,256):
    cdf[k] = cdf[k-1] + histogram[k]

pixels = img.shape[0] * img.shape[1]
cdf_min = cdf[cdf>0][0]

equalize_map = np.zeros(256, dtype=np.uint8)
for k in range(256):
    equalize_map[k] = round((cdf[k] - cdf_min) / (pixels - cdf_min) * 255)

img_eq = np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_eq[i][j] = equalize_map[img[i][j]]

cv2.imwrite("equalized.jpg", img_eq)

histogram_eq = np.zeros(256, dtype=int)
for i in range(img_eq.shape[0]):
    for j in range(img_eq.shape[1]):
        pixel = img_eq[i][j]
        histogram_eq[pixel] += 1

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title("Original Image (Grayscale)")
axes[0, 0].axis('off')

axes[0, 1].imshow(img_eq, cmap='gray')
axes[0, 1].set_title("Equalization Image")
axes[0, 1].axis('off')

axes[1, 0].bar(range(256), histogram, color='gray', width=1)
axes[1, 0].set_title("Original Histogram")
axes[1, 0].set_xlabel("Pixel Intensity")
axes[1, 0].set_ylabel("Frequency")

axes[1, 1].bar(range(256), histogram_eq, color='gray', width=1)
axes[1, 1].set_title("Histogram After Equalization")
axes[1, 1].set_xlabel("Pixel Intensity")
axes[1, 1].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("equalization_result.png")
plt.show()
print("Done! Saved to equalized.jpg và equalization_result.png")










