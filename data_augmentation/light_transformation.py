import cv2
import numpy as np


def enlight_v2(image):
    # 模拟部分亮光或暗光
    img = image
    height, width, channel = img.shape

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the brightest pixel in the image
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
    max_loc = (np.random.randint(height), np.random.randint(width))
    radius = np.random.randint(200)
    strength = np.random.randint(255)
    print(f'radius: {radius}, strength: {strength}')

    # Create a circle at the location of the brightest pixel
    circle_img = np.zeros_like(gray)
    cv2.circle(circle_img, max_loc, radius, (strength, strength, strength), -1)

    # Apply a Gaussian blur to the circle to create a light source effect
    blur_img = cv2.GaussianBlur(circle_img, (101, 101), 0)
    blur_img = cv2.cvtColor(blur_img, cv2.COLOR_GRAY2BGR)
    # Add the blurred circle to the original image
    result = cv2.addWeighted(img, 1, blur_img, 0.5, 0)
    return result

