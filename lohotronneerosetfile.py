import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image1 = Image.open('1.png').convert("L")
image2 = Image.open('2.png').convert("L")

image1.show()
image2.show()

plt.imshow(image2, cmap='gray', vmin=0, vmax=255)
plt.show()

plt.imshow(image1, cmap='gray', vmin=0, vmax=255)
plt.show()

def compare_images(img1, img2):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the two images
    diff = cv2.absdiff(gray1, gray2)

    # Calculate the mean squared error (MSE) between the two images
    mse = np.mean((diff ** 2))

    # Calculate the peak signal-to-noise ratio (PSNR) between the two images
    psnr = 10 * np.log10(255 ** 2 / mse)

    # Calculate the structural similarity index (SSIM) between the two images
    ssim = cv2.quality.QualitySSIM_compute(gray1, gray2)

    # Print the results
    print("MSE:", mse)
    print("PSNR:", psnr)
    print("SSIM:", ssim)

    # Display the difference image
    cv2.imshow("Difference", diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load the two images
img1 = cv2.imread("1.png")
img2 = cv2.imread("2.png")

# Compare the two images
compare_images(img1, img2)
