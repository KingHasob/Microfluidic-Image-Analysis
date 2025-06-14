import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from skimage.color import label2rgb


img = imread("enhanced.png") #should be already graystyle


thresh = threshold_otsu(img) * 0.65 #global threshold, constant may be adjusted
binary = img > thresh


labeled = label(binary)


cleaned = np.zeros_like(binary)

for region in regionprops(labeled):
    if region.eccentricity > 0.85 and region.area > 50:
        for y, x in region.coords:
            cleaned[y, x] = 1


imsave("thresholded.png", (binary * 255).astype(np.uint8))           #binary mask
imsave("coloured.png", (label2rgb(labeled, image=img, bg_label=0) * 255).astype(np.uint8))  #colored labels
imsave("noblobs.png", (cleaned * 255).astype(np.uint8))              # cleaned mask

#display
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Thresholded")
plt.imshow(binary, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Labelled")
plt.imshow(label2rgb(labeled, image=img, bg_label=0))
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Blobs Removed")
plt.imshow(cleaned, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
