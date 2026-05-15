import cv2

img_original = cv2.imread("bruno.jpg")
img_gray     = cv2.imread("bruno_gray.jpg", cv2.IMREAD_GRAYSCALE)

def print_info(img, name):
    print(f"─── {name} ───")
    print(f"  Size          : {img.shape[1]} x {img.shape[0]} (W x H)")
    print(f"  Channels      : {img.shape[2] if len(img.shape) == 3 else 1}")
    print(f"  Data type     : {img.dtype}")
    print(f"  Min pixel     : {img.min()}")
    print(f"  Max pixel     : {img.max()}")
    print()

print_info(img_original, "Original Image (BGR)")
print_info(img_gray,     "Grayscale Image")