import cv2
from functions import *
import numpy as np

for i in range(7):
    path = 'data/' + str(i+1) + '.png'

    img_bgr = cv2.imread(path)
    img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # Перевод и bgr в rgb
    # x = float(input('Введите параметр x_distortion:\n'))
    # y = float(input('Введите параметр y_distortion:\n'))

    x, y = 0.2, 0.2

    # Запуск функции:
    output_img = distortion(img, x, y)

    # Отображение результатов:
    plot_result(img, output_img)

    # запуск окна настроек
    interctive_window(path, itr=i)

img1 = cv2.imread('1.png')
img2 = cv2.imread(interctive_window(output_img))

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
