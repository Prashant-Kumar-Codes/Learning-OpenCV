import cv2

img_location = input('Enter image location you want to open: ')
print('Image location : ',img_location)

img = cv2.imread(rf'{img_location}')

if img is not None:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print('Image converted to grayscale')

    option = input('Enter you want to show(show) or save(save): ')

    if option == 'show':
        cv2.imshow('GrayScaled_Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    elif option == 'save':
        name = input('Enter name of image for saving: ')
        
        # try:
        #     lastSlashIndex = img_location.rfind('/')
        # except -1 or '-1':
        #     lastSlashIndex = img_location.rfind('\\')
        # finally:
        #     print(lastSlashIndex)

        # name = img_location[:lastSlashIndex + 1] + name + img_location[len(img_location)-4:]

        lastSlashIndex = max(img_location.rfind('/'), img_location.rfind('\\'))

        name = img_location[:lastSlashIndex + 1] + name
        print(name)

        cv2.imwrite(f'{name}', img)
        print('Image saved successfully')

    else:
        print('Typing mistake')

else:
    print('Image cannot be loaded.\nCheck the file location and try again.')

