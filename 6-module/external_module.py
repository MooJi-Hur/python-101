import cv2 as cv
import sys
img = cv.imread("./python-logo.png")

# pip install opencv-python
# = python3 -m pip install opencv-python

if img is None:
    sys.exit("file not found")

cv.imshow("img", img)
cv.waitKey()
cv.destroyWindow()