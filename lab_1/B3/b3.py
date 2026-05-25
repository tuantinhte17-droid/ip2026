import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("bruno_gray.jpg", cv2.IMREAD_GRAYSCALE)
histogram = np.zeros(256, dtype=int)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pixel = img[i][j]
        histogram[pixel] += 1

#1. Histogram
plt.figure(figsize=(10,4))
plt.bar(range(256),histogram,color="gray",width=1)
plt.title("Histogram of the image")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()




