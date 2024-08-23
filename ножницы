import cv2
import numpy as np

# Load the image
img = cv2.imread('1.png')

# Get the dimensions of the image
height, width, _ = img.shape

# Calculate the size of each segment
segment_width = width // 3
segment_height = height // 3

# Create a dictionary to store the segmented regions
regions = {}

# Segment the image into 9 parts
for i in range(3):
    for j in range(3):
        x = j * segment_width
        y = i * segment_height
        roi = img[y:y+segment_height, x:x+segment_width]
        region_name = f"Region {i*3 + j + 1}"
        regions[region_name] = roi

# Display the segmented regions
for region_name, region in regions.items():
    cv2.imshow(region_name, region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Save the segmented regions to files
for region_name, region in regions.items():
    cv2.imwrite(f"{region_name}.jpg", region)
