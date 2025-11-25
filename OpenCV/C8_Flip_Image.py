import cv2

'''
flipped_img = cv2.flip(src, flipCode)

Parameters:

    src: The source image (the image you want to flip).

    flipCode: Defines how the image is flipped:
        • 0 → Flip vertically (top ↔ bottom)
        • 1 → Flip horizontally (left ↔ right)
        • -1 → Flip both horizontally and vertically
'''

img = cv2.imread(r'D:\Codes\Images\Tree.jpg')

if img is not None:
    print('Image loaded successfully')
    flip_hor = cv2.flip(img, 1)
    flip_ver = cv2.flip(img, 0)
    flip_hor_ver = cv2.flip(img, -1)

    cv2.imshow('Original_Image', img)
    cv2.imshow('Flipped_Horizontally', flip_hor)
    cv2.imshow('Flipped_Vertically', flip_ver)
    cv2.imshow('Flipped_Both_Vertically_Horizontally', flip_hor_ver)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print('Program Ended Successfully')

else:
    print('Error in loading image')


