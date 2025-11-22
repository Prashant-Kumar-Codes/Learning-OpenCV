import cv2
import mediapipe as mp
import time


# Time tracking for FPS calculation
previous_time = 0

# Initialize video capture from default webcam (0 = default camera)
video_capture = cv2.VideoCapture(0)


# MediaPipe Hands solution for hand detection and tracking
mp_hands = mp.solutions.hands

# Initialize the Hands object with default parameters
# Customizable parameters: max_num_hands, min_detection_confidence, min_tracking_confidence
hands_detector = mp_hands.Hands()

# MediaPipe drawing utilities for visualizing hand landmarks and connections
mp_drawing = mp.solutions.drawing_utils


while True:
    # Capture frame-by-frame from webcam
    success, frame = video_capture.read()
    
    # Convert BGR (OpenCV format) to RGB (MediaPipe format)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect hands
    # Returns a result object containing hand landmarks if detected
    detection_results = hands_detector.process(rgb_frame)
    
    
    # Check if any hand landmarks were detected in the frame
    # multi_hand_landmarks contains a list of all detected hands
    if detection_results.multi_hand_landmarks:
        
        # Loop through each detected hand
        for hand_landmarks in detection_results.multi_hand_landmarks:
            
            # Each hand has 21 landmarks (0-20)
            # Landmarks include: wrist, thumb (4 points), index finger (4 points), etc.
            for landmark_id, landmark in enumerate(hand_landmarks.landmark):
                print(f'Id: {landmark_id}\nLandmarks: {landmark}')
                '''
                Each landmark has:
                - x: Horizontal position (0.0 to 1.0, normalized by frame width)
                - y: Vertical position (0.0 to 1.0, normalized by frame height)
                - z: Depth (relative to wrist, negative = closer to camera)
                '''
                
                # Get frame dimensions (height, width, channels)
                frame_height, frame_width, frame_channels = frame.shape
                
                # Convert normalized coordinates to pixel coordinates
                x_pixel = int(landmark.x * frame_width)
                y_pixel = int(landmark.y * frame_height)
                print(landmark_id, x_pixel, y_pixel)
                
                # Example: Draw a circle on landmark 0 (wrist)
                if landmark_id == 0:
                    cv2.circle(frame, (x_pixel, y_pixel), 10, (200, 20, 200), -1, cv2.LINE_AA)
            
            
            # Draw all 21 landmarks and connections between them on the frame
            # hand_landmarks: landmark positions for current hand
            # mp_hands.HAND_CONNECTIONS: predefined connections between landmarks (lines)
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    
    # Calculate and display FPS (frames per second)
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time
    
    # Display FPS on frame
    cv2.putText(frame, f'FPS: {int(fps)}', (20, 50), 
                cv2.FONT_HERSHEY_DUPLEX, 0.7, (10, 50, 22), 1, cv2.LINE_AA)
    
    # Show the processed frame in a window
    cv2.imshow('Hand Detection', frame)
    
    
    # Exit loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
