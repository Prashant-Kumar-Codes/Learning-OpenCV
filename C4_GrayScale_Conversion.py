import cv2

img = cv2.imread('D:\\Codes\\Images\\tree.jpg')

imgToGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('AI_GrayScale', imgToGray)
cv2.waitKey(0)
cv2.destroyAllWindows()