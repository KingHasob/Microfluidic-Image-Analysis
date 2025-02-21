# Microfluidic-Image-Analysis
A Python-based image analysis pipeline for bacterial and fungal behaviour in microfluidic environments

This project provides automated tools for processing raw microscopy images of bacteria and fungi in microfluidic channels

# 🦠 Bacterial Movement Analysis using Image Processing

## 📌 Overview
This project is part of our **DAPP microfluidic chip study** to investigate bacterial movement along fungal highways. The Python program developed here is used for **analyzing microscopy images** obtained from the chip. The goal is to extract **quantitative data** to better understand bacterial behavior, motility, and interactions within the microfluidic environment.

## 🎯 Goal
- Process microscopy images and extract relevant bacterial movement data.
- Quantify bacterial **position, movement speed, clustering behavior**, and **hitchhiking patterns**.
- Improve image clarity through **denoising, edge detection, and segmentation** techniques.
- Automate the image analysis pipeline to handle large datasets efficiently.

---

## 🛠️ Current Methodology

The program uses **Python-based image processing** with the following libraries:
- [`numpy`](https://numpy.org/) - Numerical computation
- [`skimage`](https://scikit-image.org/) - Image processing functions
- [`opencv`](https://opencv.org/) - Computer vision and feature detection

### 🔬 **Processing Techniques & Applications**

| Processing Technique       | Purpose                                              | Application |
|----------------------------|------------------------------------------------------|-------------|
| **Denoising**              | Removes noise, enhances clarity                     | Improves microscopic image quality |
| **Edge Detection**         | Identifies boundaries in images                     | Highlights bacterial cluster boundaries |
| **Deconvolution**          | Anti-blurring, enhances sharpness                   | Assists in highlighting boundaries if images are blurred |
| **Filtering (entropy filter)** | Measures image complexity (entropy) to detect key features | Improves segmentation clarity, pre-processing for thresholding |
| **Thresholding**           | Converts grayscale images to binary images          | Separates bacteria from non-bacteria regions |
| **Movement Tracking** _(in progress)_ | Tracking algorithm for motile bacteria     | Calculates motility & hitchhiking behavior |
| **Numerical Quantification** _(in progress)_ | Extracts quantitative movement data     | Computes bacterial track distance, hitchhiking efficiency |
| **Custom Object Segmentation** | Identifies bacterial clusters from microchannels  | Measures area, ratios, bacterial separation |

---

## 📂 Project Structure

