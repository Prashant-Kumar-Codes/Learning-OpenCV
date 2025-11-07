import cv2
import os

x = 0
 
opimg =  cv2.imread('D:/codes/images/Tree.jpg')

if opimg is None:
    print('Error in loading the image')
    x = 1
else:
    print('Images loaded successfully')
    x = 2
    cv2.imshow('Tree', opimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 


# Saving image

# cv2.imwrite(filename, image, params=None)
if x == 2:
    if os.path.exists('D:/codes/images/new_tree.jpg'):
        print('Image already exists')
    else:
        cv2.imwrite('D:/codes/images/new_tree.jpg', opimg)
        print('Image saved successfully')
else:
    print('Could not save the file because image cannot be')
    
