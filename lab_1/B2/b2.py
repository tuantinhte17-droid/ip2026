import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("bruno.jpg")
img_new = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(1,5,figsize=(20,4))
axes[0].imshow(img_new, cmap='gray')
axes[0].set_title("Original")
axes[0].axis('off')

params = [(1.0, 50), (1.0, -50), (1.5, 0), (0.5, 0)]
for idx, (a, b) in enumerate(params):
    output = np.zeros_like(image, dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i][j]
            value = a * pixel + b
            output[i][j] = np.clip(value, 0, 255)

    output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)  # fixed: convert output
    cv2.imwrite(f"processed_a{a}_b{b}.jpg", output)       # fixed: indent

    axes[idx + 1].imshow(output_rgb)                       # fixed: output_rgb
    axes[idx + 1].set_title(f"a={a}, b={b}")
    axes[idx + 1].axis('off')

plt.tight_layout()











    





