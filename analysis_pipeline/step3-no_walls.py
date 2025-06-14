import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave


hyphae = imread("noblobs.png", as_gray=True) > 0.5 #load clened image


manual_mask = imread("mask.png", as_gray=True) > 0.5 #load manual mask


masked_result = hyphae & manual_mask #apply mask


imsave("nowalls.png", (masked_result * 255).astype(np.uint8))

#display
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Original Hyphae")
plt.imshow(hyphae, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Manual Mask (Inner Region)")
plt.imshow(manual_mask, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Final Result")
plt.imshow(masked_result, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
