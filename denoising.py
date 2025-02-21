from skimage import io, img_as_float, color
from scipy.ndimage import gaussian_filter, median_filter
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np
from skimage.util import img_as_ubyte  # Convert float images for saving

#load image in grayscale (or it doesnt work, may refine if needed)
img = io.imread(r"C:\Users\Bokan\Onedrive\Documents\image_analysis\bacteria_test.png")


if img.ndim == 3:
    img = color.rgb2gray(img)  # convert to grayscale if RGB

img = img_as_float(img)

#applying Gaussian Filter Denoising
gaussian_img = gaussian_filter(img, sigma=3)
io.imsave(r"C:\Users\Bokan\OneDrive\Documents\image_analysis\nlm.png", img_as_ubyte(gaussian_img))

#applying Median Filter Denoising
median_img = median_filter(img, size=3)
io.imsave(r"C:\Users\Bokan\OneDrive\Documents\image_analysis\nlm.png", img_as_ubyte(median_img))

#applying Non-Local Means Denoising (so far best result but actual denoising means TBD)
sigma_est = np.mean(estimate_sigma(img))  
nlm_img = denoise_nl_means(img, h=5 * sigma_est, fast_mode=False, patch_size=5, patch_distance=3)

# Save Non-Local Means Denoising Result 



io.imsave(r"C:\Users\Bokan\OneDrive\Documents\image_analysis\gaussian.png", img_as_ubyte(gaussian_img))
io.imsave(r"C:\Users\Bokan\OneDrive\Documents\image_analysis\median.png", img_as_ubyte(median_img))
io.imsave(r"C:\Users\Bokan\OneDrive\Documents\image_analysis\nlm.png", img_as_ubyte(nlm_img))
print('Executed, check image folder') #shows directly on specified folder
