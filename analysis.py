import cv2
import numpy as np
import matplotlib.pyplot as plt
heatmap_image = cv2.imread('heatmap_capture.png')  # Replace 'heatmap.png' with the path to your image file
gray_heatmap = cv2.cvtColor(heatmap_image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_heatmap, cmap='hot')
plt.colorbar()
plt.show()
threshold_value = 150  # Adjust this value as needed
_, binary_heatmap = cv2.threshold(gray_heatmap, threshold_value, 255, cv2.THRESH_BINARY)
plt.imshow(binary_heatmap, cmap='gray')
plt.show()
x, y = 100, 200  # Replace with the coordinates you're interested in
intensity = gray_heatmap[y, x]
print(f'Intensity at ({x}, {y}): {intensity}')
mean_intensity = np.mean(gray_heatmap)
max_intensity = np.max(gray_heatmap)
min_intensity = np.min(gray_heatmap)
print(f'Mean Intensity: {mean_intensity}')
print(f'Max Intensity: {max_intensity}')
print(f'Min Intensity: {min_intensity}')
