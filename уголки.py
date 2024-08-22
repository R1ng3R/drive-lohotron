import cv2
import numpy as np

# Load the two images
img1 = cv2.imread('3.png')
img2 = cv2.imread('1.png')

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Apply the Harris corner detector to the images
corners1 = cv2.cornerHarris(gray1, 2, 3, 0.04)
corners2 = cv2.cornerHarris(gray2, 2, 3, 0.04)

# Threshold the corner responses to get the corner points
corners1 = cv2.dilate(corners1, None)
corners2 = cv2.dilate(corners2, None)
thresh = 0.01 * corners1.max()
corner_points1 = np.where(corners1 > thresh)
corner_points2 = np.where(corners2 > thresh)

# Calculate the number of corner points in each image
num_corners1 = len(corner_points1[0])
num_corners2 = len(corner_points2[0])

# Calculate the similarity between the two images based on the number of corner points
similarity = min(num_corners1, num_corners2) / max(num_corners1, num_corners2)

print('Similarity:', similarity)

# Visualize the corner points
# cv2.drawChessboardCorners(img1, (7, 7), corner_points1, True)
# cv2.drawChessboardCorners(img2, (7, 7), corner_points2, True)
#
# cv2.imshow('Image 1', img1)
# cv2.imshow('Image 2', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()