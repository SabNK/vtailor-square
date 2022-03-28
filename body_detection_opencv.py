import cv2
import matplotlib.pyplot as plt
import numpy as np

# read the image
image = cv2.imread("res/in/alik_girl_big.jpg")
# convert to RGB
image = cv2.cvtColor(image, cv2.cv2.COLOR_BGR2RGB)

#where low value of saturation would get the background segmented
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)

# Filter out low saturation values, which means gray-scale pixels(majorly in background)
bgd_mask = cv2.inRange(image, np.array([0, 0, 0]), np.array([255, 30, 255]))
# Get a mask for pitch black pixel values
black_pixels_mask = cv2.inRange(image, np.array([0, 0, 0]), np.array([70, 70, 70]))

# Get the mask for extreme white pixels.
white_pixels_mask = cv2.inRange(image, np.array([230, 230, 230]), np.array([255, 255, 255]))

final_mask = cv2.max(bgd_mask, black_pixels_mask)
final_mask = cv2.min(final_mask, ~white_pixels_mask)
final_mask = ~final_mask

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# create a binary thresholded image
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# show it
plt.imshow(binary, cmap="gray")
plt.show()

final_mask = cv2.erode(final_mask, np.ones((3, 3), dtype=np.uint8))
final_mask = cv2.dilate(final_mask, np.ones((5, 5), dtype=np.uint8))

# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# show the image with the drawn contours
plt.imshow(image)
plt.show()