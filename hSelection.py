import cv2
import numpy as np

# Image
imgName = 'images/lena.png'
img1 = cv2.imread(imgName)
# cv2.imshow("Test", img1)

# Get interest coordinates
x1 = 0
x2 = 100
y1 = 0
y2 = 100

# Coordinates from str to inn
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

# Image from RGB to HSV
imgHSV = cv2.cvtColor(img1, cv2.COLOR_RGB2HSV)

# Initialize min and max
minimo = 360
maximo = 0

# Get min and max from image section
for j in range(y1, y2):
   for i in range(x1, x2):
       if imgHSV[j,i,0] > maximo:
           maximo = imgHSV[j,i,0]
       if imgHSV[j,i,0] < minimo:
           minimo = imgHSV[j,i,0]

# Print min and max
print("-> Valor minimo: " + str(minimo))
print("-> Valor maximo: " + str(maximo))

# End of program
cv2.waitKey(0)
cv2.destroyAllWindows()
