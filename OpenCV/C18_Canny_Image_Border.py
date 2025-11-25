import cv2

'''
cv2.Canny() is use for ecge detection in images. It identifies edges by detecting areas of rapid intensity change(gradients)
The Canny Edge Detector is a muti-stage algorithm that includes noise reduction, gradient calculation, non-maximum suppression, and hysteresis thresholding.

Syntax:
    cv2.Canny(image, threshold1, threshold, apertureSize = 3, L2gradient = False)

image:      Source image (should be in grayscale)
threshold1:     Lower threshold for the hysteresis procedure
threshold2:     Upper threshold for the hysteresis procedure
apertureSize:       (Optional) Aperture size for the Sobel operator (default = 3). It must be odd (3, 5, or 7).
L2gradient:     (Optional) If True, uses a more accurate L2 norm for gradient magnitude; otherwise, L1 norm is used (default = False).
'''

#img = cv2.imread(r'D:\codes\images\Tree.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread(r'D:\codes\images\Tree.jpg', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 170, apertureSize = 3, L2gradient = False)

ret, thresh_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('Original_Image', img)
cv2.imshow('Edges_Cutout_Image', edges)
cv2.imshow('Threshold_Image', thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


