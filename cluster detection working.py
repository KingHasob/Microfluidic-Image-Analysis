import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu, rank
from skimage.morphology import disk

# Load image
image_path = "bacteria_test.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 1: Apply Entropy Filter (Enhances Textured Regions)
entropy_img = rank.entropy(image, disk(3))

# Step 2: Apply Otsu’s Threshold to Segment High-Texture Regions
threshold = threshold_otsu(entropy_img)
binary_mask = entropy_img > threshold

# Convert to uint8
binary_mask = (binary_mask * 255).astype(np.uint8)

# Step 3: Adaptive Thresholding (Better for Uneven Lighting)
adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV, 21, 5)

# Combine entropy and adaptive thresholding
combined_mask = cv2.bitwise_and(binary_mask, adaptive_thresh)

# Step 4: Morphological Refinement (Expand Slightly Without Noise)
kernel = np.ones((3, 3), np.uint8)  
processed_mask = cv2.dilate(combined_mask, kernel, iterations=1)

# Step 5: Find Contours
contours, _ = cv2.findContours(processed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 6: Select Only the Largest Compact Object in the Center
height, width = image.shape
center_x, center_y = width // 2, height // 2
roi_x_min, roi_x_max = int(0.3 * width), int(0.7 * width)  # Focuses on central region
roi_y_min, roi_y_max = int(0.3 * height), int(0.7 * height)  

best_contour = None
best_score = -1

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 200:  # Ignore tiny objects
        continue
    
    # Compute compactness (convexity)
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    solidity = float(area) / hull_area if hull_area > 0 else 0
    
    # Compute distance to center and check if it's within the target area
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        if not (roi_x_min < cx < roi_x_max and roi_y_min < cy < roi_y_max):
            continue  # Ignore anything outside the center region
        distance = np.sqrt((cx - center_x) ** 2 + (cy - center_y) ** 2)
    else:
        distance = float('inf')

    # Scoring based on area, solidity, and closeness to center
    score = (area * solidity) / (1 + distance * 0.2)  
    
    if score > best_score:
        best_score = score
        best_contour = cnt

# Step 7: Visualization
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Display Filtered Clusters
contour_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
if best_contour is not None:
    cv2.drawContours(contour_image, [best_contour], -1, (0, 255, 0), 2)

axs[0].imshow(contour_image, cmap='gray')
axs[0].set_title("Final Isolated Bacterial Cluster")
axs[0].axis("off")

# Generate Bacterial Heatmap
heatmap = np.zeros_like(image, dtype=np.uint8)
if best_contour is not None:
    cv2.drawContours(heatmap, [best_contour], -1, (255), thickness=cv2.FILLED)

axs[1].imshow(heatmap, cmap='hot', interpolation='nearest')
axs[1].set_title("Final Bacterial Heatmap")
axs[1].axis("off")

# Histogram of Cluster Sizes (only one valid cluster)
if best_contour is not None:
    axs[2].hist([cv2.contourArea(best_contour)], bins=5, color="blue", alpha=0.7, edgecolor="black")
axs[2].set_title("Cluster Size Distribution")
axs[2].set_xlabel("Cluster Size (pixels)")
axs[2].set_ylabel("Count")

print("Final Isolated Bacterial Cluster Found:", best_contour is not None)

plt.tight_layout()
plt.show()
