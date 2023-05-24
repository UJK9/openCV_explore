import cv2
import numpy as np 
import dil
import ero
import blu
output_path = 'D:/op/ou2/a.jpg'
image= cv2.imread('Citizenship2.jpg')
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
_,threshold= cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+ cv2.THRESH_OTSU)
contours,_ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
document_contour = max(contours, key = cv2.contourArea)
x,y,w,h= cv2.boundingRect(document_contour)
cropped_img= image[y: y+h, x: x+w]
cv2.imwrite(output_path, cropped_img)
print(f'Cropped document saved: {output_path}')

dil.dilate()
ero.erode()
blu.blur()
