import cv2
import numpy as np

'''

cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)

    img:    The image on which the line will be drawn.
    pt1:    Starting point of the line (x₁, y₁).
    pt2:    Ending point of the line (x₂, y₂).
    color:  Line color in BGR format, e.g. (255, 0, 0) for blue.
    thickness:  Line thickness in pixels (default = 1).
    lineType:   Type of line — e.g. cv2.LINE_8, cv2.LINE_AA (anti-aliased), etc.
    shift:  Number of fractional bits in point coordinates (usually left 0).

'''

img = cv2.imread(r'D:/codes/images/White_Page.png') #size = (600, 600)

if img is None:
    print('Image cannot be loaded')
else:
    print('Image loaded successfully')

    #creating a blank white page using numpy array
    imgNumpy = np.ones((400,400,3), dtype = 'uint8') * 0

    #Drawing a line
    cv2.line(img, (50,50), (550,550), (255, 100, 50), thickness = 10)
    cv2.line(imgNumpy, (0,0), (400,400), (255, 255, 255), thickness = 5)
    cv2.imshow('Line_On_Image', img)
    cv2.imshow('Line_On_Numpy_Image', imgNumpy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    