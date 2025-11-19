import cv2

'''
Definition:
    approxPolyDP() is a contour-approximation function that simplifies a curve by reducing the number of points.
    It finds a polygon that approximates the contour with fewer vertices while maintaining the overall shape.

Usage:
    Shape detection — identify triangles, squares, rectangles, pentagons, circles
    Simplifying contours — reduce unnecessary points
    Improving performance — fewer points → faster calculations
    Object classification — number of sides helps determine shape type

Syntax:
    cv2.approxPolyDP(curve, epsilon, closed)

Parameters:
curve

The contour you want to approximate.
Usually taken from:

contours, hierarchy = cv2.findContours(...)

epsilon

Maximum distance between original contour and approximated curve.
Controls smoothness of shape.

Common values:

epsilon = 0.01 * arcLength(curve, True) → very accurate

epsilon = 0.02 * arcLength(curve, True) → slightly simplified

Larger epsilon → fewer points → simpler shape

closed

Whether the output should form a closed polygon

True → closed shape (triangle, rectangle, pentagon etc.)

False → open curve

'''



img = cv2.imread(r'D:\Codes\Images\Triangle.png')

img2Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#converting to black and white
_, thresh_img = cv2.threshold(img2Gray, 120, 255, cv2.THRESH_BINARY)

#finding the contours
# contours, hierarchy = cv2.findContours(image, mode, method)
contours, _ = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 230, 20), 3, cv2.LINE_AA)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    corner = len(approx)
    
    if corner == 3:
        shape_name = 'Triangle'
    elif corner == 4:
        shape_name = 'Rectangle/Square'
    elif corner == 5:
        shape_name = 'Pentagon'
    elif corner > 5:
        shape_name = 'Circle'
    else:
        shape_name = 'Cannot Be Determined'

    cv2.drawContours(img, [approx], -1, (0, 255, 0), 2, cv2.LINE_AA)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(img, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 0, 0), 1, cv2.LINE_AA)

cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()