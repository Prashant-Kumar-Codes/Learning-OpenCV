import cv2

import time

'''
# resizing image 
### variable = cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=cv2.INTER_LINEAR)

# src  --> The input image you want to resize.

# dsize   --> Desired output size as a tuple (width, height).
        Example: (200, 300) means width = 200, height = 300.
        Set this to None if you want to use fx and fy.

# dst -->	Optional output image (usually not used — OpenCV creates one automatically).

# fx	--> Scale factor along the x-axis (horizontal scaling).
        Example: fx = 0.5 → width becomes half.

# fy	--> Scale factor along the y-axis (vertical scaling).
    Example: fy = 2 → height becomes double.

# interpolation	--> Algorithm used to calculate pixel values after resizing.
        Common values:
        • cv2.INTER_NEAREST → Fastest, low quality.
        • cv2.INTER_LINEAR → Default, good for enlarging.
        • cv2.INTER_AREA → Best for shrinking.
        • cv2.INTER_CUBIC → Better quality (but slower).
        • cv2.INTER_LANCZOS4 → Very high quality.

'''


img = cv2.imread(r'D:\Codes\Images\Grayninja.png')

if img is None:
    print('Error in loading image')
else:
    print('Image loaded successfully')

    x = time.time()

    resized_img = cv2.resize(img, dsize = (200,200), interpolation = cv2.INTER_LANCZOS4)

    y = time.time()

    resized_img = cv2.resize(img, dsize = (200,200), interpolation = cv2.INTER_NEAREST)

    z = time.time()

    cv2.imshow('resized_image', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(y-x)
    print(z-y)
