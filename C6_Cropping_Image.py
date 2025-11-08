import cv2

'''
as we know image is stored as a numpy array.
For cropping the image we need to slice the array (containing data of pixels)
'''

img = cv2.imread(r'D:\Codes\Images\Tony_Stark.jpg')

#crop_var = image_variabl[startY:endY, startX:endX]
cropped_img = img[30:630, 260:860]

if cropped_img is not None:
    cv2.imshow('cropped_tony', cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Error in cropping the image')