import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread("gray.jpg", cv2.IMREAD_GRAYSCALE)
img_eq   = cv2.imread("equalized.jpg", cv2.IMREAD_GRAYSCALE)


fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].imshow(img_gray, cmap='gray')
axes[0].set_title("Original Grayscale")
axes[0].axis('off')

axes[1].imshow(img_eq, cmap='gray')
axes[1].set_title("Equalized Grayscale")
axes[1].axis('off')

plt.tight_layout()
plt.savefig("comparison.png")
plt.show()