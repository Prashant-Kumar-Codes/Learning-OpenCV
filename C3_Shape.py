import cv2

openimg = cv2.imread('D:/codes/images/tree.jpg')

# imageVariable.shape : returns a tuple of hight, width, channel 

if openimg is not None:
    print(openimg.shape)
    height, width, channel = openimg.shape
else:
    print('Image is not loaded')

print(f'\nHeight: {height}\nWidth: {width}\nChannel: {channel}')