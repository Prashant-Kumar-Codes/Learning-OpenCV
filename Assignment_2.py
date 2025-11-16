import cv2
import os
import numpy
from datetime import datetime


class user_drawing:
    def __init__(self):
        self.image_location = input('Enter the image location: ')
        self.img = cv2.imread(rf'{self.image_location}')
        
        if self.img is not None:
            print('Image successfully loaded')
        else:
            self.img = numpy.ones((500, 500, 3), dtype = 'uint8') * 255

            print('Image cannot be loaded\n...\nNumpy array a used to create a blank white page')


    def choice_display(self):
        self.draw_choice = input(
            '''Enter what you want to draw:
                l for line,
                c for circle,
                r for rectangle, and
                at for adding text.''')
        print(self.draw_choice)
        return 'choice_display working perfectly'

    def choice_input(self):
        self.choice = input('Enter your choice here: ').lower()
        return 'self.choice is working perfectly'
    

    def redirecting(self):
        if self.choice == 'l':
            print('Redirecting for line parameters...')
            self.line()
        elif self.choice == 'c':
            print('Redirecting for circle parameters...')
            self.circle()
        elif self.choice == 'r':
            print('Redirecting for rectangle parameters...')
            self.rectangle()
        elif self.choice == 'at':
            print('Redirecting for adding text parameters...')
            self.add_text()
        else:
            print('You typed wrong try again..')
        

    def line(self):
        #  cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
        pt1 = eval(input('Enter the start point /use brackets/ (x1, y1): '))
        pt2 = input('Enter the  end point /use brackets/ (x2, y2): ')

        while True:
            if pt1 is tuple:
                break
            pt1 = eval(input('Enter the start point /use brackets/ (x1, y1): '))
    

    def line(self):
        pass


    def line(self):
        pass


    def line(self):
        pass

        

    
x = user_drawing()
x.choice_display()