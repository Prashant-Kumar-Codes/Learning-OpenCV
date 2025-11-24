import cv2
import mediapipe as mp
import time

previousTime = 0

mp_detection = mp.solutions.pose
pose = mp_detection.Pose(
    static_image_mode = False,
    #upper_body_only = False,
    model_complexity = 0,
    smooth_landmarks = True,
    min_detection_confidence = 0.6,
    min_tracking_confidence = 0.4
)

# hands_detector = mp_hands.Hands(
#     static_image_mode=False,
#     model_complexity=0,        # Lighter modelq
#     max_num_hands = 4,           # Track 1 hand only
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.3
# )

mp_drawing = mp.solutions.drawing_utils

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)


while True:
    success, frame = capture.read()
    frame2rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame2rgb)
    print(results.pose_landmarks)
    
    currentTime = time.time()
    fps = int(1 / (currentTime - previousTime))
    previousTime = currentTime
    
    cv2.putText(frame, f'FPS = {fps}', (20,50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 90), 1, cv2.LINE_AA)
        
    cv2.imshow('Posture Detection', frame)


    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
capture.release()
cv2.destroyAllWindows()