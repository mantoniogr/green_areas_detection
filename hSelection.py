"""
This script analyzes the Hue values in a selected region of interest (ROI) 
from an image in HSV color space. It extracts min/max Hue values and saves
the HSV channels as separate images.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os

# Use Agg backend for headless environments
import matplotlib
matplotlib.use('Agg')

def parse_args():
    parser = argparse.ArgumentParser(description='Analyze Hue values in ROI')
    parser.add_argument('--input', '-i', 
                        default='images/lena.png',
                        help='Input image path')
    parser.add_argument('--output-dir', '-o',
                        default='images',
                        help='Output directory for saved images')
    parser.add_argument('--roi',
                        nargs=4,
                        type=int,
                        default=[200, 230, 200, 230],
                        metavar=('x1', 'x2', 'y1', 'y2'),
                        help='ROI coordinates: x1 x2 y1 y2')
    return parser.parse_args()

def process_image(args):
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Read image
    img = cv2.imread(args.input)
    if img is None:
        raise FileNotFoundError(f"Could not load image: {args.input}")

    # Convert BGR to RGB (matplotlib expects RGB format)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Update to use ROI coordinates from args.roi
    x1, x2, y1, y2 = args.roi

    # Draw ROI rectangle 
    cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (255, 0, 0), 2)
    plt.imshow(img_rgb)
    plt.title("RGB image")
    plt.axis("off")
    plt.savefig(os.path.join(args.output_dir, "imageRGB.png"))
    plt.close()  # Close the figure to free memory

    # Image from BGR to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Extract ROI Hue values
    roi_hue = imgHSV[y1:y2, x1:x2, 0]

    # Save HSV image and channels
    HSV_HUE_MAX = 179  # OpenCV uses 0-179 for Hue
    RGB_MAX = 255

    h, s, v = cv2.split(imgHSV)
    h_scaled = (h * RGB_MAX / HSV_HUE_MAX).astype("uint8")
    imgHSV_scaled = cv2.merge([h_scaled, s, v])
    
    # Save all images
    cv2.imwrite(os.path.join(args.output_dir, "hsv_image_scaled.png"), imgHSV_scaled)
    cv2.imwrite(os.path.join(args.output_dir, "hue_channel.png"), h_scaled)
    cv2.imwrite(os.path.join(args.output_dir, "saturation_channel.png"), s)
    cv2.imwrite(os.path.join(args.output_dir, "value_channel.png"), v)

    return np.min(roi_hue), np.max(roi_hue)

def main():
    args = parse_args()
    min_hue, max_hue = process_image(args)
    print(f"Min value: {min_hue}")
    print(f"Max value: {max_hue}")

if __name__ == "__main__":
    main()
