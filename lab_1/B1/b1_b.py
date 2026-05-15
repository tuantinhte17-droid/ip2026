import cv2 
import numpy as np

img = cv2.imread("bruno.jpg")
print("Start Gray")
print("Image : ",img.shape)


for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        pixel = img[i][j]
        s = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
        s = min(s, 255)
        pixel[0] = s
        pixel[1] = s
        pixel[2] = s


cv2.imwrite("bruno_gray.jpg", img)
print("finish gray")
print(img.shape)



# Resize:
original_h = img.shape[0]
original_w = img.shape[1]

new_h = int(original_h * 1.5)
new_w = int(original_w * 1.5)



img_new  = np.zeros((new_h, new_w), dtype=np.uint8)
for i in range(new_h):
    for j in range(new_w):
        src_i = int(i / 1.5)
        src_j = int(j / 1.5)
        img_new[i][j] = img[src_i][src_j][0]

cv2.imwrite("resized.jpg", img_new)
print(f"Original size : {original_h} x {original_w}")
print(f"Resized size  : {new_h} x {new_w}")







