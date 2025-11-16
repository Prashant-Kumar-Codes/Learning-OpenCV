import cv2

'''
                        Image-Filtering
                              |
                            /   \
    Bluring    -     Noise    -    Smoothning     -    Kernel
      |
    /   \
Gaussian    Median     Bilateral      Normal
  Blur       Blur        Blur          Blur
'''


img = cv2.imread(r'D:\codes\images\Tree.jpg')

'''
Gaussian Blur:

Syntax:    cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)

src:      The source/input image.
ksize:    Kernel size → must be odd and positive (e.g., (3, 3), (5, 5)). Defines the amount of blurring.
sigmaX:   Standard deviation in the X direction (horizontal blur strength).
dst (optional):   Output image (default is created automatically).
sigmaY (optional):    Standard deviation in the Y direction. If 0, it's taken equal to sigmaX.
borderType (optional):    Pixel extrapolation method (e.g., cv2.BORDER_DEFAULT). Usually not needed.


Usage:
    Takes the weighted average of pixels, weights determined by a Gaussian function (σ = sigma).
    Gaussian blur is commonly used for noise reduction and image smoothing before edge detection (like in cv2.Canny()).

'''
gaussian_blur_img = cv2.GaussianBlur(img, (11,11), 10)


'''
Median Blur:

Syntax:     cv2.medianBlur(src, ksize)

Usage:  
    Median Blur replaces each pixel with the median value of all pixels within the kernel window — unlike Gaussian, which uses a weighted average.
    Excellent for removing salt-and-pepper noise (random white and black dots).


'''
median_blur_img = cv2.medianBlur(img, 11, 5)




cv2.imshow('Original_Image', img)
cv2.imshow('Image_Blured_Using_Gaussian_Blur', gaussian_blur_img)
cv2.imshow('Image_Blured_Using_Median_Blur', median_blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

