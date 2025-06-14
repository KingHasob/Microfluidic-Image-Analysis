import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import denoise_tv_chambolle
from skimage import exposure
from skimage.io import imsave


img = cv2.imread("GFP.png", cv2.IMREAD_COLOR)

if img is None:
    raise FileNotFoundError("Image failed to load")


green_channel = img[:, :, 1] #extract green channel


img_gray = green_channel / 255.0


img_eq = exposure.equalize_adapthist(img_gray) #contrast step


img_denoised = denoise_tv_chambolle(img_eq, weight=0.1) #denoise step


imsave("enhanced.png", (img_eq * 255).astype(np.uint8))
imsave("denoised.png", (img_denoised * 255).astype(np.uint8))

#display
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.title("Original GFP")
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Contrast Enhanced")
plt.imshow(img_eq, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Denoised")
plt.imshow(img_denoised, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
