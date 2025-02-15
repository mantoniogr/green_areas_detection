"""
This script analyzes the Hue values in a selected region of interest (ROI) 
from an image in HSV color space. It extracts min/max Hue values and saves
the HSV channels as separate images.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Use Agg backend for headless environments
import matplotlib
matplotlib.use('Agg')

# Image
imgName = 'images/lena.png'
img = cv2.imread(imgName)
if img is None:
    raise FileNotFoundError(f"Could not load image: {imgName}")

# Convert BGR to RGB (matplotlib expects RGB format)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Set roi coordinates
x1 = 200
x2 = 230
y1 = 200
y2 = 230

# Draw ROI rectangle 
cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (255, 0, 0), 2)
plt.imshow(img_rgb)
plt.title("RGB image")
plt.axis("off")  # Hide axes for a cleaner display
plt.savefig("images/imageRGB.png")  # Save the plot to a file

# Image from BRG to HSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Extract ROI Hue values
roi_hue = imgHSV[y1:y2, x1:x2, 0]

# Save HSV image and channels
HSV_HUE_MAX = 179  # OpenCV uses 0-179 for Hue
RGB_MAX = 255

h, s, v = cv2.split(imgHSV)
h_scaled = (h * RGB_MAX / HSV_HUE_MAX).astype("uint8")
imgHSV_scaled = cv2.merge([h_scaled, s, v])
cv2.imwrite("hsv_image_scaled.png", imgHSV_scaled)
cv2.imwrite("hue_channel.png", h_scaled)
cv2.imwrite("saturation_channel.png", s)
cv2.imwrite("value_channel.png", v)

# Initialize min and max
min_hue = np.min(roi_hue)
max_hue = np.max(roi_hue)

# Print min and max
print("Min value: " + str(min_hue))
print("Max value: " + str(max_hue))
