import cv2
import mediapipe as mp
import time
q
previous_time = 0

# Set lower resolution for faster processing
#video_capture = cv2.VideoCapture(r"E:\Videos\142030-779071797_tiny.mp4")
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 900)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

mp_hands = mp.solutions.hands

# Optimized parameters for better FPS
hands_detector = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=0,        # Lighter modelq
    max_num_hands = 4,           # Track 4 hands only
    min_detection_confidence=0.5,
    min_tracking_confidence=0.3
)

mp_drawing = mp.solutions.drawing_utils

while True:
    success, frame = video_capture.read()
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Performance optimization
    rgb_frame.flags.writeable = False
    detection_results = hands_detector.process(rgb_frame)
    rgb_frame.flags.writeable = True
    
    if detection_results.multi_hand_landmarks:
        for hand_landmarks in detection_results.multi_hand_landmarks:
            print(detection_results.multi_hand_landmarks)
            # Draw landmarks without extra processing
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time
    
    cv2.putText(frame, f'FPS: {int(fps)}', (20, 50), 
                cv2.FONT_HERSHEY_DUPLEX, 0.7, (10, 50, 22), 1, cv2.LINE_AA)
    
    cv2.imshow('Hand Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()


'''
-----------HOW TO OPTIMIZE THE CODE AND MAKE IT FASTER----------

1. Reduce Model Complexity (Easiest - 30% FPS Increase)
Change model_complexity from 1 (default) to 0 for faster processing with minor accuracy loss :


hands_detector = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=0,  # Use lighter model (default is 1)
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
2. Reduce Webcam Resolution
Lower resolution means fewer pixels to process:


video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # Default is often 1280
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Default is often 720
3. Optimize Frame Processing (Performance Boost)
Set frame as non-writable during processing to pass by reference instead of copying :

 
# Convert BGR to RGB
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Mark frame as not writable to improve performance
rgb_frame.flags.writeable = False
detection_results = hands_detector.process(rgb_frame)
rgb_frame.flags.writeable = True  # Set back to writable
4. Adjust Tracking Parameters
Fine-tune confidence thresholds to favor tracking over detection :

 
hands_detector = mp_hands.Hands(
    static_image_mode=False,  # Enable tracking mode
    model_complexity=0,
    max_num_hands=2,
    min_detection_confidence=0.5,  # Lower = faster detection
    min_tracking_confidence=0.3    # Lower = more tracking, less re-detection
)
5. Reduce Maximum Hands Detected
If you only need one hand :


hands_detector = mp_hands.Hands(
    max_num_hands=1,  # Track only 1 hand instead of 2
    model_complexity=0
)
6. Remove Unnecessary Processing
Comment out print statements and circles inside the loop - they slow down execution significantly :

 
# Remove or comment these lines:
# print(f'Id: {landmark_id}\nLandmarks: {landmark}')
# print(landmark_id, x_pixel, y_pixel)
# if landmark_id == 0:
#     cv2.circle(...)
'''