import cv2
import time

'''
Syntax to rotate an image:

--> Apporach 1: Using cv2.rotate()
        variable = cv2.rotate(src, rotateCode)

--> Apporach 2: Using Rotation Matrix:

        (h,w) = img.shape[:2]
        center = (w//2, h//2)       // center is a tuple with hight and width elements.
    
        m = cv2.getRotationMatrix2D(center, angle, scale)
        variable = cv2.warpAffine(img, M, (w,h))

    scale is the scaling factor (1.0 keeps original size, 2.0 double the size than the original, 0.5 halfs than the oiginal size.. )

    shape[:2] because shape return a tuple of 3 elements (height, width, channel)
'''

img = cv2.imread(r'D:\Codes\Images\Tree.jpg')


# rotating image using method 1
if img is not None:
    print('Image loaded successfully')
    print('Rotating image using first method')
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    print('Image rotated successfully')
    cv2.imshow('Original_Image', img)
    cv2.imshow('Rotated_Image-M1', rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #wating for 1.5 sec
    time.sleep(1.5)

    print('Rotating the image using second method')
    (h,w) = img.shape[:2]
    print('Height, width : ',h, w)
    center = (w//2, h//2)
    print('Center : ', center)
    m = cv2.getRotationMatrix2D(center, 126, 1.0)
    rotated_img = cv2.warpAffine(img, m, (w,h))
    print('Rotation successfull')
    
    cv2.imshow('Original_Image',img)
    cv2.imshow('Rotated_Image-M2', rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print('Program Ended')
else:
    print('Image cannot be loaded')


