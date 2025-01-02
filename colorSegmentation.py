import cv2
import numpy as np

# Read image
img = cv2.imread('images/lena.png')

# Image from RGB to HSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Min and max H values
min = 133
max = 168

# Initialize num
num = 0

# Look for pixels in H range and change values to 0
for j in range(0, img.shape[0]):
    for i in range(0, img.shape[1]):
        if imgHSV[j,i,0] > min and imgHSV[j,i,0] < max:
            imgHSV[j,i,0] = 0
            imgHSV[j,i,1] = 200
            num = num + 1

# Image from HSV to BGR
imgBGR = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR)

# Print count of pixels changed
print("-> pixels: " + str(num))

# Save image
cv2.imwrite('images/result.png', imgBGR)

