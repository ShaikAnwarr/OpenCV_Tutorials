import cv2

image = cv2.imread("sample.jpg")

if image is not None:
    h,w,c= image.shape
    print(f"Image loaded:\n Height {h}\n Width {w}\n Channnels {c}")
else:
    print("could not load image")