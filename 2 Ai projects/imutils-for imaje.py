

"""
cv2
in Python refers to the OpenCV library, a powerful open-source computer vision and machine learning software
library. It provides a vast array of functions and tools for image and video processing, analysis, and manipulation.

Key aspects of cv2 in Python:
Installation: To use cv2, you need to install the opencv-python package using pip.

    pip install opencv-python
Importing: Once installed, you can import the library into your Python script using:

    import cv2
Image and Video Operations: cv2 enables a wide range of operations, including:
Reading and writing images: cv2.imread() and cv2.imwrite().

Displaying images: cv2.imshow().

Reading and writing videos: cv2.VideoCapture() and cv2.VideoWriter().

Image manipulation: Resizing (cv2.resize()), cropping, rotating, color space conversions (cv2.cvtColor()),
blurring (cv2.GaussianBlur()), thresholding (cv2.threshold()), edge detection (cv2.Canny()), and more.

Drawing: Drawing shapes, text, and lines on images.
Computer Vision Applications: cv2 is widely used for:
Object detection and recognition.
Face detection and recognition.
Image segmentation.
Motion tracking.
Augmented reality.
And many other computer vision tasks.

In essence, cv2 serves as the Python interface to the comprehensive OpenCV library, allowing developers to
leverage its extensive functionalities for various computer vision and image processing applications.

---------------------------
imutils
is a Python package containing a series of convenience functions designed to simplify common image
processing operations when working with OpenCV. It aims to reduce boilerplate code and make tasks like
translation, rotation, resizing, and contour manipulation more straightforward.

Key Features and Functions:
Image Translation: The translate() function allows shifting an image by a specified number of pixels in the
x and y directions without manually constructing translation matrices or calling cv2.warpAffine.

Image Rotation: The rotate() function simplifies image rotation by handling the calculation of rotation
matrices and applying the transformation, including options for rotating around a specific point.

Image Resizing: The resize() function provides an easy way to resize images while maintaining aspect ratio,
specifying either the width or height and letting the function calculate the other dimension.

Automatic Canny Edge Detection: The auto_canny() function automates the Canny edge detection process by
dynamically calculating the upper and lower thresholds based on the median of the grayscale pixel intensities,
eliminating the need for manual tuning.

4-point Perspective Transform: The perspective module offers functions for performing 4-point perspective
transforms, useful for obtaining a top-down view of a region of interest.

Contour Utilities: Functions like grab_contours() help in handling the varying return values of cv2.findContours()
across different OpenCV versions, and other utilities assist in sorting and manipulating contours.

Skeletonization: The skeletonize() function constructs the topological skeleton of an object in an image, a
process that is not directly available in standard OpenCV functions.

pip install imutils
"""

import cv2
import imutils

# Load an image
image = cv2.imread("example.jpg")

# Resize the image
resized_image = imutils.resize(image, width=500)

# Rotate the image
rotated_image = imutils.rotate(image, angle=45)

# Perform automatic Canny edge detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = imutils.auto_canny(gray_image)

# Display images (requires matplotlib or cv2.imshow)
# cv2.imshow("Original", image)
# cv2.imshow("Resized", resized_image)
# cv2.imshow("Rotated", rotated_image)
# cv2.imshow("Edges", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()










