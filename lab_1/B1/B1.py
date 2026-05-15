import cv2 
import numpy as np
import matplotlib.pyplot as plt

#1. Convert RGB to Gray scale image
img_1 = cv2.imread("mu.jpg")
#img_2 = cv2.imread("Mona_Lisa.webq")

print("Start Gray")
print("Image 1: ",img_1.shape)
#print("Image 2: ",img_2.shape)


for i in range (img_1.shape[0]):
    for j in range (img_1.shape[1]):
        pixel = img_1[i][j]
        s = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
        s = min(s, 255)
        pixel[0] = s
        pixel[1] = s
        pixel[2] = s


cv2.imwrite("gray.jpg", img_1)
print("finish gray")
print(img_1.shape)




