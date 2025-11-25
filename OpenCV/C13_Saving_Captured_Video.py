import cv2
import os
from datetime import datetime

'''
fourcc:
    4-character code of the codec used to compress the frames.
    Example → cv2.VideoWriter_fourcc(*'mp4v') for MP4 files or cv2.VideoWriter_fourcc(*'XVID') for AVI files.
'''

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
camera_fps = cap.get(cv2.CAP_PROP_FPS)

print('frame_width = ', frame_width, 'frame_height = ', frame_height, 'camera_fps = ', camera_fps)

codec_avi = cv2.VideoWriter_fourcc(*'XVID')
codec_mp4 = cv2.VideoWriter_fourcc(*'mp4v')
codec_mkv = cv2.VideoWriter_fourcc(*'X264')

##### IF I PROVIDE FPS MORE THEN THE CAPTURING FPS OF THE CAMERA. THE SPEED OF THE VIDEO WILL CHANGE ACCORDINGLLY TO ADJUST THE FRAME RATE.

# cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=True)
if os.path.exists('E:\\videos\\My_Captured_Video.avi'):

    curr_datetime = str(datetime.now()).replace(' ', '-')
    curr_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    recorder = cv2.VideoWriter(rf'E:\videos\My_Captured_Video-{curr_datetime}.avi', codec_avi, camera_fps, (frame_width,frame_height), isColor = True)
    
else:
    recorder = cv2.VideoWriter('E:\\videos\\My_Captured_Video.avi', codec_avi, 30, (frame_width,frame_height), isColor = True)


while True:
    ret, frame = cap.read()

    if not ret:
        print('Cannot capture the video')
        break
    
    recorder.write(frame)
    cv2.imshow('Recoding_for_Saving_In_mp4', frame)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        print('quiting...')
        break

cap.release()
recorder.release()
cv2.destroyAllWindows()
