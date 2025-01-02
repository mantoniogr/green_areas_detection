import cv2
import matplotlib.pyplot as plt

# Use Agg backend for headless environments
import matplotlib
matplotlib.use('Agg')

# Image
imgName = 'images/lena.png'
img = cv2.imread(imgName)

# Convert BGR to RGB (matplotlib expects RGB format)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Set roi coordinates
x1 = 200
x2 = 230
y1 = 200
y2 = 230

# Display the roi using matplotlib
cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (255, 0, 0), 2)
plt.imshow(img_rgb)
plt.title("RGB image")
plt.axis("off")  # Hide axes for a cleaner display
plt.savefig("images/imageRGB.png")  # Save the plot to a file

# Image from BRG to HSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Extract ROI Hue values
roi_hue = imgHSV[y1:y2, x1:x2, 0]

# Display the image using matplotlib
plt.imshow(imgHSV)
plt.title("HSV image")
plt.axis("off")  # Hide axes for a cleaner display
plt.savefig("images/imageHSV.png")  # Save the plot to a file

# Initialize min and max
min = 360
max = 0

# Get min and max from image section
for j in range(y1, y2):
   for i in range(x1, x2):
       if imgHSV[j,i,0] > max:
           max = imgHSV[j,i,0]
       if imgHSV[j,i,0] < min:
           min = imgHSV[j,i,0]

# Print min and max
print("Min value: " + str(min))
print("Max value: " + str(max))
