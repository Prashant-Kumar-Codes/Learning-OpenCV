import cv2

# Loading an image

# cv2.imread(filename, flags=cv2.IMREAD_COLOR)

# flags = 1 // for color (default)
# flags = 0 // for grayscale or black and white
# flags = -1 // load the image as it is
 
opimg =  cv2.imread('D:/codes/images/Tree.jpg')

if opimg is None:
    print('Error in loading the image')
else:
    print('Images loaded successfully')

#Showing image

    # cv2.imshow(window_name, image)
    cv2.imshow('Tree', opimg)

    # cv2.waitKey(delay=0)  
    cv2.waitKey(0)  # Wait until any key is pressed


    cv2.destroyAllWindows() 


