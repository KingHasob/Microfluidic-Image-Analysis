# Microfluidic-Image-Analysis
A Python-based image analysis pipeline for bacterial and fungal behaviour in microfluidic environments


**Overview**
- This project is part of our microfluidic chip study to investigate bacterial movement along fungal highways. The Python program developed here is used for analysing microscopy images obtained from the chip. The goal is to improve image clarity, as well as to extract quantitative data to better understand bacterial behaviour, motility, and interactions within the microfluidic environment.
  

**Goal**
- Process microscopy images, **improve image quality**, and **extract relevant quantitative data**.
- Quantify bacterial **position, movement speed, clustering behavior**, and **hitchhiking patterns**.
- Improve image clarity through **denoising, edge detection, and segmentation** techniques.
- Automate the image analysis pipeline to **handle large datasets efficiently**.


**Dependencies**

The program uses Python-based image processing, with the following libraries:

- **[numpy](https://numpy.org/)** – Used for numerical computations and array operations.
- **[matplotlib](https://matplotlib.org/)** – Used for visualising data, including plots and histograms.
- **[scipy](https://scipy.org/)** – Provides scientific computing tools, including image filtering (`gaussian_filter`, `median_filter`).
- **[opencv-python (cv2)](https://opencv.org/)** – Used for image processing, including feature detection and transformation.
- **[scikit-image (skimage)](https://scikit-image.org/)** – Used for image filtering, thresholding, segmentation, and morphology functions.



**Installation**

To install all required dependencies, run:

```sh
pip install numpy matplotlib scipy opencv-python scikit-image
```


**Processing Techniques & Applications**

| Processing Technique             | Purpose                                                  | Application |
|----------------------------------|----------------------------------------------------------|-------------|
| **Denoising**                    | Removes noise, enhances clarity                         | Improves microscopic image quality |
| **Edge Detection**               | Identifies boundaries in images                         | Highlights bacterial cluster boundaries |
| **Deconvolution**                | Anti-blurring, enhances sharpness                      | Assists in highlighting boundaries if images are blurred |
| **Filtering (entropy filter)**   | Measures image complexity (entropy) to detect key features | Improves segmentation clarity, pre-processing for thresholding |
| **Thresholding**                 | Converts grayscale images to binary images             | Separates bacteria from non-bacteria regions |
| **Movement Tracking** (in progress)  | Tracking algorithm for motile bacteria                  | Calculates motility & hitchhiking behavior |
| **Numerical Quantification** (in progress) | Extracts quantitative movement data             | Computes bacterial track distance, hitchhiking efficiency |
| **Custom Object Segmentation**   | Identifies bacterial clusters from microchannels        | Measures area, ratios, bacterial separation |


