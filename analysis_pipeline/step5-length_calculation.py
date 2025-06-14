import numpy as np
from skimage.io import imread, imsave
from skimage.morphology import skeletonize
import matplotlib.pyplot as plt


img = imread("nowalls.png", as_gray=True)
binary_mask = img > 0.5 


skeleton = skeletonize(binary_mask) #skeletonise to 1 pixel wide


imsave("skeletal.png", (skeleton * 255).astype(np.uint8))


skeleton_length_pixels = np.sum(skeleton) #measure length


PIXEL_SIZE_MICRONS = 0.588  #constant for 20x images
absolute_length_microns = skeleton_length_pixels * PIXEL_SIZE_MICRONS


height, width = skeleton.shape #relative length
image_diagonal_pixels = np.sqrt(height**2 + width**2)
relative_length_percent_diagonal = skeleton_length_pixels / image_diagonal_pixels * 100

#output
print("=== Hyphal Length Analysis ===")
print(f"Skeleton pixels (raw length): {skeleton_length_pixels}")
print(f"Absolute length: {absolute_length_microns:.2f} µm (using {PIXEL_SIZE_MICRONS} µm/pixel)")
print(f"Relative length: {relative_length_percent_diagonal:.2f}% of image diagonal")
