import theimage
from skimage import io
image = io.imread('girl.jpg')

image_gray = color.rgb2gray(image)
image_show(image_gray);


def circle_points(resolution, center, radius):
    """
        Generate points which define a circle on an image.Centre refers to the centre of the circle
        """

radians = np.linspace(0, 2 * np.pi, resolution)
c = center[1] + radius * np.cos(radians)  # polar co-ordinates
r = center[0] + radius * np.sin(radians)

return np.array([c, r]).T
# Exclude last point because a closed path should not have duplicate points
points = circle_points(200, [80, 250], 80)[:-1]

plt.imshow(image);

