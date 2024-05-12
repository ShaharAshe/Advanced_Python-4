import numpy as np
from numba import njit
from PIL import Image

# Define the image size and colors
H, W = 1080, 1920
background_color = np.array([0.4, 0.4, 0.4])
circle_color = np.array([0.8, 0.3, 0.1])
rectangle_color = np.array([0.5, 0.3, 0.2])

# Initialize the image with the background color
image = np.ones((H, W, 3)) * background_color

# Define the circle parameters
circle_center = np.array([600, 400])
circle_radius = 350

# Define the rectangle parameters
rectangle_start = np.array([800, 450])
rectangle_end = np.array([1600, 920])

# Create a meshgrid for coordinate-wise operations
Y, X = np.ogrid[:H, :W]

# Define a numba-jitted function to draw the circle and rectangle
def draw_shapes(image, X, Y):
    # Draw the circle
    circle_mask = (X - circle_center[0])**2 + (Y - circle_center[1])**2 <= circle_radius**2
    image[circle_mask] = circle_color

    # Draw the rectangle
    rectangle_mask = (rectangle_start[0] <= X) & (X < rectangle_end[0]) & (rectangle_start[1] <= Y) & (Y < rectangle_end[1])
    image[rectangle_mask] = rectangle_color

    return image

# Draw the shapes on the image
image = draw_shapes(image, X, Y)

# Convert the image to an 8-bit RGB image and save it
Image.fromarray((image * 255).astype(np.uint8)).show()
Image.fromarray((image * 255).astype(np.uint8)).save('output.png')
