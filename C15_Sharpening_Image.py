import cv2
import numpy  as np


'''
Sharpening Image:

Syntax:     sharp_img = cv2.filter2D(src, ddepth, kernel)

src:    The source (input) image you want to sharpen.
ddepth:  Desired depth of the output image. Use -1 to keep the same depth as the source.
kernel:  A 2D array (NumPy matrix) defining the sharpening filter.

'''

img = cv2.imread(r'D:\codes\images\Tree_Blured.jpg')

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened_img = cv2.filter2D(img, -1, sharpen_kernel)

cv2.imshow('Orginal_Image', img)
cv2.imshow('Sharpened_Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

