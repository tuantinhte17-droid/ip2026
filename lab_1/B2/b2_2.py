import cv2 
import numpy as np
import matplotlib.pyplot as plt

img_1 = cv2.imread("processed_1.jpg")
img_2 = cv2.imread("processed_2.jpg")
img_3 = cv2.imread("processed_3.jpg")
img_4 = cv2.imread("processed_4.jpg")

array_img = [img_1,img_2,img_3,img_4]
params    = [(1.0, 50), (1.0, -50), (1.5, 0), (0.5, 0)]
colors    = ['blue', 'green', 'red']   

fig, axes = plt.subplots(1, 4, figsize=(20, 4))

for idx,img in enumerate(array_img):
    histogram = np.zeros((3,256), dtype=int)
    for i in range(img.shape[0]):
      for j in range(img.shape[1]):
        for c in range(3):
                histogram[c][img[i][j][c]] += 1 

    a,b = params[idx]
    for c in range(3):
        axes[idx].bar(range(256), histogram[c], color=colors[c], alpha=0.4, width=1)
    axes[idx].legend(['B', 'G', 'R'])
    axes[idx].set_title(f"a={a}, b={b}")
    axes[idx].set_xlabel("Pixel Intensity")
    axes[idx].set_ylabel("Frequency")

plt.tight_layout()
plt.show()







