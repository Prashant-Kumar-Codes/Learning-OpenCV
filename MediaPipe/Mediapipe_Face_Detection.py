import cv2
import mediapipe as mp
import time
import numpy as np


'''
**1) `mpFaceDetection = mp.solutions.face_detection`**

### **Definition*
This loads the **Face Detection module** from MediaPipe's solutions package.

### **Meaning**

You are importing the **full face detection solution**, which contains:

* The detection model
* Pre-processing functions
* Utility classes
* Configurations

It acts like a **folder** that stores everything related to face detection.

---

**2) `mpDraw = mp.solutions.drawing_utils`**

### **Definition**

This imports MediaPipe's **drawing utilities**.

### **Usage**

Used to draw:

* Face landmarks
* Detection bounding boxes
* Keypoints

Functions inside this include:

* `draw_detection()`
* `draw_landmarks()`

So this is responsible for **visualizing** detection results.

---

**3) `faceDetection = mpFaceDetection.FaceDetection()`**

### **Definition**

This creates an **instance of the Face Detection model**.

### **Meaning**

You are **activating the face detector** with default parameters.

Internally, MediaPipe loads:

* The pretrained face-detection model
* The configuration (min detection confidence, model type, etc.)

### **Result**

`faceDetection` becomes your **detector object**.
You will call methods on it—for example:

```python
results = faceDetection.process(imgRGB)
```

---

**4) What does `process()` do?**

### **Definition**

`process()` sends the image to the MediaPipe model for **inference (prediction).**

### **Meaning**

It performs:

1. Image preprocessing
2. Neural network face detection
3. Post-processing of bounding boxes
4. Returning the results

---

**5) What is stored in `results`?**

`results` is a **MediaPipe object** that contains all detection outputs.

### **Important properties:**

#### **1) `results.detections`**

List of all detected faces.

Each detection contains:

* Bounding box (xmin, ymin, width, height)
* Confidence score
* Keypoints (eye, nose, ear positions)

Example:

```python
for detection in results.detections:
    print(detection.location_data.relative_bounding_box)
```

#### **2) `results` when no face found**

If no face:

```python
results.detections == None
```

---

# 🟦 **Summary Table**

| Line                                              | Meaning                          |
| ------------------------------------------------- | -------------------------------- |
| `mpFaceDetection = mp.solutions.face_detection`   | Loads the Face Detection module  |
| `mpDraw = mp.solutions.drawing_utils`             | Loads drawing utilities  module  |
| `faceDetection = mpFaceDetection.FaceDetection()` | Creates face detector object     |
| `results = faceDetection.process(imgRGB)`         | Runs face detection on the image |


'''



cap = cv2.VideoCapture(0)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
capFPS = int(cap.get(cv2.CAP_PROP_FPS))
ptime = 0



mp_face_detection = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
faceDetection = mp_face_detection.FaceDetection(0.8)

while True:
    ret, frame = cap.read()
    
    if ret == True:
        
        ''' Error because cannot use \n in putText text parameter'''
        # cv2.putText(frame, f'FPS = {fps}\nHeight = {height}\nWidth = {width}\n, Brightness = {brightness}\nContrast = {contrast}\nSaturation = {saturation}', (width//2, height//2), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 233, 45), 2, cv2.LINE_AA)
        cv2.putText(frame, f'Height = {height}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (100,233,45), 2)
        cv2.putText(frame, f'Width = {width}', (20, 100), cv2.FONT_HERSHEY_PLAIN, 1.5, (100,233,45), 2)
        cv2.putText(frame, f'CFPS = {capFPS}', (20, 130), cv2.FONT_HERSHEY_PLAIN, 1.5, (100,233,45), 2)
        
        frame2RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = faceDetection.process(frame2RGB)
        #THIS RESULT IS A CLASS WHICH HAVE ALL THE IMPORMATION OF THE DETECTED FACES
        
        if results.detections:
            for id, detection in enumerate(results.detections):
                #mp_draw.draw_detection(frame, detection)
                # print(id, detection)
                # print('detection.score:: ', detection.score)
                # print('detection.location_data.relative_boundary_box: ', detection.location_data.relative_bounding_box)     #give normalized values to get actual(pixel) value need to multiply by width and height.
                
                bboxC = detection.location_data.relative_bounding_box
                
                frameHeight, frameWidth, frameChannel = frame.shape
                
                bbox = int(bboxC.xmin * frameWidth), int(bboxC.ymin * frameHeight), \
                        int(bboxC.width * frameWidth), int(bboxC.height * frameHeight)
                        
                cv2.putText(frame, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] + -5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 1, lineType = cv2.LINE_AA )        
                cv2.rectangle(frame, bbox, (0, 0, 255), 2, cv2.LINE_AA )
                
                
        ctime = time.time()
        fps = np.round(1/(ctime-ptime))
        ptime = ctime
        cv2.putText(frame, f'FPS = {fps}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 1.5, (100,233,45), 2)
                
                
                
        

        cv2.imshow('Frames', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        print('Cannot capture video')
        break

cap.release()
cv2.destroyAllWindows()