import matplotlib.pyplot as plt
from skimage import io, color
from skimage.filters.rank import entropy
from skimage.filters import try_all_threshold, threshold_otsu
from skimage.morphology import disk
import numpy as np

# Load image
img = io.imread(r"C:\Users\Bokan\OneDrive\Documents\image_analysis\bacteria_test.png")

# Handle grayscale and RGB images correctly
if img.ndim == 3 and img.shape[-1] == 3:
    gray_img = color.rgb2gray(img)
else:
    gray_img = img  # Already grayscale

# Convert to 8-bit unsigned integer
gray_img_uint8 = (gray_img * 255).astype('uint8')

# Compute entropy
entropy_img = entropy(gray_img_uint8, disk(1))

# Display entropy image
plt.imshow(entropy_img, cmap="gray")

# Apply different thresholding methods
fig, ax = try_all_threshold(entropy_img, figsize=(10, 8), verbose=False)

# Apply Otsu thresholding
threshold = threshold_otsu(entropy_img)
binary = entropy_img <= threshold  # Thresholded binary image

# Display binary image
plt.figure()
plt.imshow(binary, cmap='gray')

# Calculate percentage of bright pixels
bright_percentage = (np.sum(binary == 1) * 100) / (np.sum(binary == 1) + np.sum(binary == 0))
print(f"The percentage of bright pixels is: {bright_percentage:.2f}%")

plt.show()
