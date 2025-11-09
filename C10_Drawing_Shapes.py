import cv2
import numpy


'''
1. Rectangle:

cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)

    img:    The image on which the rectangle is to be drawn.
    pt1:    Top-left corner coordinates → (x₁, y₁).
    pt2:    Bottom-right corner coordinates → (x₂, y₂).
    color:  Rectangle color in BGR format (e.g., (0, 255, 0) for green).
    thickness:  Border thickness in pixels.
        👉 Positive integer → border only.
        👉 -1 or cv2.FILLED → filled rectangle.
    lineType:   (Optional) Line type (e.g., cv2.LINE_8, cv2.LINE_AA).
    shift:  (Optional) Number of fractional bits in coordinates (default 0).


2. Circle:

cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None)

    img:    The image on which the circle will be drawn.
    center: Center coordinates of the circle → (x, y).
    radius: Radius of the circle in pixels.
    color:  Circle color in BGR format.
    thickness:  Border thickness in pixels.
        👉 Positive integer → border only.
        👉 -1 or cv2.FILLED → filled circle.
    lineType:   (Optional) Line type (e.g., cv2.LINE_8, cv2.LINE_AA).
    shift:  (Optional) Number of fractional bits in the center coordinates (default 0).


3. Ellipse

cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None)

    img:    Image on which ellipse is drawn.
    center: Center coordinates → (x, y).
    axes:   Length of major and minor axes → (axisX, axisY).
    angle:  Rotation angle of ellipse in degrees.
    startAngle: Starting angle of the arc (in degrees).
    endAngle:   Ending angle of the arc (in degrees).
    color:  Color in BGR format.
    thickness:  Line thickness or -1 for filled ellipse.
    lineType:   (Optional) Type of line (e.g., cv2.LINE_AA).
    shift:  (Optional) Fractional bits in coordinates (default 0).


4. Polygon

cv2.polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None)

    img:    Image on which polygon is drawn.
    pts:    Array of points (list or NumPy array) that make up the polygon’s vertices.
    isClosed:   True → closed shape; False → open shape.
    color:  Color of the polygon in BGR format.
    thickness:  Line thickness (use -1 with cv2.fillPoly() to fill).
    lineType:   (Optional) Type of the line (e.g., cv2.LINE_AA).
    shift:  (Optional) Fractional bits in coordinates (default 0).

'''


imgRec = numpy.ones((500,500,3), dtype = 'uint8') * 255
imgCir = numpy.ones((500,500,3), dtype = 'uint8') * 255

#creating rectangle
#cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
cv2.rectangle(imgRec, (100, 100), (400,400), (0,0,255), thickness = -1)
cv2.imshow('Rectangle_In_Image', imgRec)

#creating circle
# cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
(h,w) = imgCir.shape[:2]
cv2.circle(imgCir, (w//2, h//2), 50, (0,255,0), thickness = -1 )
cv2.imshow('Circle_In_Image', imgCir)


cv2.waitKey(0)
cv2.destroyAllWindows()
