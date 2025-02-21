import matplotlib.pyplot as plt
from skimage import io, color
from skimage.filters.rank import entropy
from skimage.filters import try_all_threshold, threshold_otsu
from skimage.morphology import disk
import numpy as np

img = io.imread(r"C:\Users\Bokan\OneDrive\Documents\image_analysis\bacteria_test.png")

#convert to grayscale
if img.ndim == 3 and img.shape[-1] == 3:
    gray_img = color.rgb2gray(img)
else:
    gray_img = img


gray_img_uint8 = (gray_img * 255).astype('uint8')

#computing entropy
entropy_img = entropy(gray_img_uint8, disk(1))


plt.imshow(entropy_img, cmap="gray")

#applying Otsu thresholding
threshold = threshold_otsu(entropy_img)
binary = entropy_img <= threshold  # Thresholded binary image

#displaying binary image
plt.figure()
plt.imshow(binary, cmap='gray')

#calculating percentage of bright pixels
bright_percentage = (np.sum(binary == 1) * 100) / (np.sum(binary == 1) + np.sum(binary == 0))
print(f"The percentage of bright pixels is: {bright_percentage:.2f}%")

plt.show()
