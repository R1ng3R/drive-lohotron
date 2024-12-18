import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Define the source and destination points
src_points = np.float32([[0, 0], [image.shape[1], 0], [image.shape[1], image.shape[0]], [0, image.shape[0]]])
dst_points = np.float32([[100, 100], [image.shape[1] - 100, 100], [image.shape[1] - 100, image.shape[0] - 100], [100, image.shape[0] - 100]])

# Compute the perspective transformation matrix
M = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply the perspective transformation
warped_image = cv2.warpPerspective(image, M, (image.shape[1], image.shape[0]))

# Display the original image
cv2.imshow('Original Image', image)

# Display the warped image
cv2.imshow('Warped Image', warped_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

# Save the warped image to a file
cv2.imwrite('warped_image.jpg', warped_image)
