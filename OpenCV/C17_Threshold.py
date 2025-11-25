import cv2

'''
Definition:
    Thresholding converts a grayscale image into a binary image by comparing each pixel to a threshold value.
    — Pixels greater than threshold → replaced with maxValue
    — Pixels less than threshold → replaced with 0 (or depending on the type)
    It is used to separate foreground from background.

Usage:
    Image segmentation
    Object detection
    Pre-processing for contour detection
    Simple background removal
    Creating binary masks

Syntax:
    threshold_value, threshold_image = cv2.threshold(src, thresh, maxval, type)

Parameter Details:

src: The input image (must be grayscale).

thresh:
    The threshold value.
    Pixels are compared against this value.

maxval:
    The value assigned to pixels exceeding the threshold.
    Used only in binary thresholding operations.

type (Thresholding operation):

    Type                    Meaning
    cv2.THRESH_BINARY:      thresh → maxval, else 0
    cv2.THRESH_BINARY_INV:  thresh → 0, else maxval
    cv2.THRESH_TRUNC:       thresh → set to thresh, else unchanged
    cv2.THRESH_TOZERO:      thresh → unchanged, else 0
    cv2.THRESH_TOZERO_INV:  thresh → 0, else unchanged
    cv2.THRESH_OTSU:        Auto threshold using Otsu's Method
    cv2.THRESH_TRIANGLE:    Auto threshold using Triangle Method

Note:

    You can combine types using

    cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) --------- Use when lighting conditions are uneven.
    
    cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE) --------- Works well for images with large background.


Returns:
    threshold_value:    The threshold value (useful in automatic methods like Otsu).
    threshold_image:    The resulting binary or thresholded image.

'''

img = cv2.imread(r'D:/codes/images/Tony_Stark.jpg', cv2.IMREAD_GRAYSCALE)


threshold_value, threshold_img_array = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Black_And_White_Image_After_Threshold', threshold_img_array)
cv2.waitKey(0)
cv2.destroyAllWindows()