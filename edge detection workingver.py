from skimage import io
from matplotlib import pyplot as plt

img = io.imread(r"C:\Users\Bokan\Onedrive\Documents\image_analysis\bacteria_test.png", as_gray = True)


#commented basic transformation codes if needed
#rescaled_img = rescale(img, 0.1, anti_aliasing = True) #eg 50% smaller = 0.5
#resized_img = resize(img, (50,50)) #eg 200x200, not display, but number of pixels that make up image
#downscaled_img = downscale_local_mean(img, (4,3))



from skimage.filters import roberts, sobel, scharr, prewitt

edge_roberts = roberts(img)
edge_sobel = sobel(img)
edge_scharr = scharr(img)


from skimage.feature import canny
edge_canny = canny(img, sigma=1.5) #sigma to be experimented
plt.imshow(edge_canny)
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True,
                         figsize=(8, 8))
ax = axes.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title('Original image')

ax[1].imshow(edge_roberts, cmap=plt.cm.gray)
ax[1].set_title('Roberts Edge Detection')

ax[2].imshow(edge_sobel, cmap=plt.cm.gray)
ax[2].set_title('Sobel')

ax[3].imshow(edge_scharr, cmap=plt.cm.gray)
ax[3].set_title('Scharr')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()

