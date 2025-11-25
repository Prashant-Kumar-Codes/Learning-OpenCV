import cv2

#-------------------------------------------------------------------------------
#-------------------------------findContours()----------------------------------
#-------------------------------------------------------------------------------

'''
Definition:
    cv2.findContours() is a function used to detect contours(simply - the position of the borders/boundaries) in an image.
    A contour is a curve(stored as a array) that joins continuous points having the same intensity, usually used to detect shapes, edges, and object boundaries.

Note:   It works only on binary images, meaning you should first apply thresholding or edge detection.

Usage:
    * Shape Detection - Detect circles, rectangles, polygons, human outlines, etc.
    * Object Counting - Count objects in an image (coins, shapes, parts).
    * Boundary Extraction - Extract outer/inner boundaries of objects.
    * Contour-Based Measurements - Calculate area, perimeter, shape features.
    * Input for drawContours() - The contours returned here are used in cv2.drawContours() draw them.

Syntax:
    contours, hierarchy = cv2.findContours(image, mode, method)

    
--- Parameters:

1) image:
    MUST be a binary image (from cv2.threshold() or cv2.Canny()).
    Contours are extracted from white objects on black background.

2) mode - Contour Retrieval Mode that controls which contours are returned.
    Mode	            Meaning
    cv2.RETR_EXTERNAL:  Returns only outermost contours
    cv2.RETR_LIST:      Returns all contours without hierarchy
    cv2.RETR_TREE:      Returns all contours + full hierarchy (parent-child)
    cv2.RETR_CCOMP:     Returns contours in 2 levels (external + internal)

3) method - Contour Approximation Method that controls how contour points(with how much precision) are stored.
    Method	                    Meaning
    cv2.CHAIN_APPROX_NONE:      Stores every single point on the contour (very detailed, large output)
    cv2.CHAIN_APPROX_SIMPLE:    Compresses the contour by removing redundant points (most commonly used)

    
--->Return Values:

    1) contours:
        A list of contour points.
        Each contour is an array of shape (N, 1, 2):
        N = number of points in the contour
        2 = (x, y) coordinate
            Example:
            contours[0]  # first detected contour

    2) hierarchy
        Describes relationships:
            Parent contour
            Child contour
            Next contour
            Previous contour
            Hierarchy shape → (1, number_of_contours, 4)
            You can ignore it if you don't need contour relationships.

Summary Table:
    image:     Binary image (10% important — must be binary)
    mode:      Controls which contours are returned
    method:    Controls how contour points are stored
    contours:  List of detected contour points
    hierarchy: Relationship structure between contours

'''



#-------------------------------------------------------------------------------
#-------------------------------drawContours()----------------------------------
#-------------------------------------------------------------------------------

'''
Definition:
    Contours are curves that connect continuous points having the same color initensity.
    --- Contours detect shapes, boundaries and outlines in an image.

Usage:  1) Outline detection: Shapes, Human Outline, Logos or objects
        2) Shape Analysis: Count objects, Measure Size, Track movements
        3) Visualize output of findCountours()

Syntax:
    cv2.drawContours(image, contours, contour_index, color, thickness, lineType )

image:  The image on which contours will be drawn
contours:   A list of contour points returned by cv2.findContours()
contour_index	Which contour to draw:
                0 → first contour
                -1 → draw all contours
                2 → second countors and so on
color:  Color of contour (BGR)
thickness:   Line thickness (-1 → fill the contour)
'''

#  cv2.drawContours(image, contours, contour_index, color, thickness, lineType )


img = cv2.imread(r'D:\Codes\Images\Tony_Stark.jpg')

threshold_value, threshold_img_array = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),100, 255, cv2.THRESH_BINARY)



#FIND COUNTORS
# contours, hierarchy = cv2.findContours(image, mode, method)
contours, heirarchy = cv2.findContours(threshold_img_array, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#DRAWING THE CONTOURS
# cv2.drawContours(image, contours, contour_index, color, thickness, lineType )
cv2.drawContours(img, contours, -1, (20, 255, 20), 3, cv2.LINE_AA)

cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
