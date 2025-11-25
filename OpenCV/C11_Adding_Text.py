import cv2
import numpy

'''
## Adding Text in the Image: 

(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)

    img:       The image on which the text will be placed.
    text:      The string (text) to be written.
    org:    Bottom-left corner of the text in the image → (x, y) coordinates.
    fontFace:      Font type — choose from predefined fonts (see below 👇).
    fontScale:     Font size multiplier (controls the size of text).
    color:     Text color in BGR format (e.g., (0, 255, 0) for green).
    thickness:     Thickness of the text stroke (in pixels).
    lineType:      (Optional) Type of the line — usually cv2.LINE_AA for smooth text.
    bottomLeftOrigin:      (Optional, rarely used) If True, text origin is bottom-left (default False).

✳️ Available Fonts (FontFace Options):

Font Name	                Constant

Hershey Simplex:       cv2.FONT_HERSHEY_SIMPLEX
Hershey Plain:     cv2.FONT_HERSHEY_PLAIN
Hershey Duplex:    cv2.FONT_HERSHEY_DUPLEX
Hershey Complex:       cv2.FONT_HERSHEY_COMPLEX
Hershey Triplex:       cv2.FONT_HERSHEY_TRIPLEX
Hershey Complex Small:     cv2.FONT_HERSHEY_COMPLEX_SMALL
Hershey Script Simplex:    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
Hershey Script Complex:    cv2.FONT_HERSHEY_SCRIPT_COMPLEX
'''
# (img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)

img = numpy.ones((600, 600, 3), dtype= numpy.uint8) * 255

if img is None:
    print('Image cannot be formed')
else:
    print('Image created successfully')

    cv2.putText(img, 'Hello, This is the text i have put it on this image', (40,300), cv2.FONT_HERSHEY_DUPLEX, 0.9, (20,25,222), 2, cv2.LINE_AA)

    cv2.imshow('Image_Added_Text', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()