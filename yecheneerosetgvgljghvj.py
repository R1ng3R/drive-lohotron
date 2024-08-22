import cv2
import numpy as np

# Load the images
img1 = cv2.imread('1.png')
img2 = cv2.imread('2.png')

# Resize the images to the same resolution
img1 = cv2.resize(img1, (920, 640))
img2 = cv2.resize(img2, (920, 200))

cv2.imshow("Difference", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
gray1 = cv2.GaussianBlur(gray1, (5, 5), 0)
gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)

# Create an ORB detector
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# Create a Brute-Force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match the descriptors
matches = bf.match(des1, des2)

# Apply ratio test to filter out weak matches
good_matches = []
for m in matches:
    if m.distance < 0.7 * m.distance:
        good_matches.append(m)

# Compute the similarity score based on the number of good matches
similarity_score = len(good_matches) / len(matches)
print("Similarity score:", similarity_score)
