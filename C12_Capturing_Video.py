import cv2

'''
cv2.VideoCapture(0):    Opens the default webcam.
cv2.imshow():   Displays each video frame in a window.
cv2.waitKey(1): Waits 1 ms per frame (keeps video smooth).
ord('q'):   Quits the loop when you press Q or q.
cap.release():  Frees the webcam for other programs.
cv2.destroyAllWindows():    Closes all OpenCV windows.
cv2.waitKey(0): Keeps the last frame visible until you press any key (optional).
'''
cap = cv2.VideoCapture(0)

if cap.isOpened():
    print('Webcam opened successfully.')
else:
    print('Error in opening the webcam')
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print('Could not read frame')
        break
    
    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quitting.....')
        break

cap.release()
cv2.destroyAllWindows()
