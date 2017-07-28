import cv2
import numpy as np

# Read image
img1 = cv2.imread('vlcsnap-2015-02-26-18h00m13s99.png')
cv2.imshow("Original", img1)

# Image from RGB to HSV
imgHSV = cv2.cvtColor(img1, cv2.COLOR_RGB2HSV)

# Min and Max H values
minimo = 72.5
maximo = 100

# Initialize numero
numero = 0

# Look for pixels in H range and change values to 0
for j in range(0, img1.shape[0]):
    for i in range(0, img1.shape[1]):
        if imgHSV[j,i,0] > minimo and imgHSV[j,i,0] < maximo:
            imgHSV[j,i,0] = 0
            numero=numero+1

# Image from HSV to RGB            
imgRGB = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2RGB)

cv2.imshow("Modificada", imgRGB)

# Print count of pixels changed
print "-> pixels: " + str(numero)

# Save image
cv2.imwrite('test.png', imgRGB)

# End of program
cv2.waitKey(0)
cv2.destroyAllWindows()
