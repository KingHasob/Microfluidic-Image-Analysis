from skimage.io import imread
import numpy as np

#constants at 20x magnification
PIXEL_SIZE_MICRONS = 0.588
PIXEL_AREA_MICRONS2 = PIXEL_SIZE_MICRONS ** 2


img = imread("nowalls.png", as_gray=True)
binary_mask = img > 0.5  #further threshold


total_pixels = binary_mask.size #converage calculation
hyphae_pixels = np.sum(binary_mask)

percentage_coverage = (hyphae_pixels / total_pixels) * 100
actual_coverage_um2 = hyphae_pixels * PIXEL_AREA_MICRONS2

#output
print(f"Total pixels: {total_pixels}")
print(f"Hyphae pixels: {hyphae_pixels}")
print(f"Percentage coverage: {percentage_coverage:.2f}%")
print(f"Actual hyphae area: {actual_coverage_um2:.2f} µm²")
