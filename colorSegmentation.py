"""
Color segmentation script that identifies pixels within a specific Hue range
in HSV color space and modifies them. The modified image is saved as a new file.
"""

import cv2
import numpy as np
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Color segmentation using HSV color space')
    parser.add_argument('--input', default='images/lena.png', help='Input image path')
    parser.add_argument('--output', default='images/result.png', help='Output image path')
    parser.add_argument('--hue-min', type=int, default=133, help='Minimum Hue value')
    parser.add_argument('--hue-max', type=int, default=168, help='Maximum Hue value')
    return parser.parse_args()

# Constants
SATURATION_VALUE = 200

# Parse arguments
args = parse_args()
img_path = args.input
OUTPUT_PATH = args.output
HUE_MIN = args.hue_min
HUE_MAX = args.hue_max

# Read image
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Could not load image: {img_path}")

# Image from RGB to HSV
modified_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Replace the manual pixel iteration with vectorized operations
hue_mask = (modified_hsv[:,:,0] > HUE_MIN) & (modified_hsv[:,:,0] < HUE_MAX)
modified_hsv[hue_mask, 0] = 0
modified_hsv[hue_mask, 1] = SATURATION_VALUE
num_pixels = np.sum(hue_mask)

# Image from HSV to BGR
imgBGR = cv2.cvtColor(modified_hsv, cv2.COLOR_HSV2BGR)

# Print count of pixels changed
print("-> pixels: " + str(num_pixels))

# Save image
cv2.imwrite(OUTPUT_PATH, imgBGR)