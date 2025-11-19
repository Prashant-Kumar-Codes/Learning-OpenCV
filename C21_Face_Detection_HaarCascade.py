import cv2

'''
cv2.CascadeClassifer / Haar Cascade

Definition: Haar Cascade is an object detection algorightm in OpenCV that uses pre-trained XML classifier to detect faces, eyes, cars, smiles, and other objects. It works by scanning the image using Haar-like features and a cascade of classifier that quickly decide whether a region contains the target object.

Usage:
    * Face Detection: Detect frontal faces, profile faces
    * Object Detection: Eyes, full body, licence plates, smile detection
    * Real-Time Application: CCTV surveillance, gesture detection
    * Preprocessing: Detect faces before recognition or tracking

Syntax
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image, scaleFactor, minNeighbors, flags, minSize, maxSize)

Parameters:

    * image: The grayscale image on which detection will run. Haar cascades always work on grayscale images.

    * scaleFactor: How much the image size is reduced at each scale. 
                Typical value: 1.1 - 1.3
                Smalller value: more accurate but slower
    * minNeighbors: How many neighbor rectangle must agree before it is considered a valid detection.
                Typical: 3 to 6
                Higher value: fewer false positives.
    
    * minSize: Minimum possible object size(width, height). Used to ignore very small detections.

    * maxSize: Maximum possible object size.

Limitations:
    Not very accurate on complex backgrounds
    Not good in low light
    Worse than deep-learning methods like DNN/YOLO

'''

face_cascade = cv2.CascadeClassifier(r'D:\Codes\GitHub_Data\Learning-OpenCV\Haar_Cascade_Files\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
    frame2GrayScale = cv2.blur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (50, 50), 1 )

    # faces = face_cascade.detectMultiScale(image, scaleFactor, minNeighbors, flags, minSize, maxSize)
    face = face_cascade.detectMultiScale(frame2GrayScale, scaleFactor = 1.2, minNeighbors = 5, minSize = (100, 100), maxSize = (800, 800))

    '''
    face_cascade return tuple of 4 elements (x-axis, y-axis, width, height) of the rectangle on teh face detected

    x = how far from left
    y = how far from top
    width = width of the face
    height = height of the face
    '''

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
    
    cv2.imshow('Face_Detected_Frames', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


