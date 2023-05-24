import cv2 
import numpy as np 

kernel = np.ones((3,3), np.uint8)
output_path= 'D:/op/ou2/dil.jpg'
def dilate():
    image = cv2.imread('Citizenship2.jpg')

    g= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dilated = cv2.dilate(image, kernel, iterations=1)
    cv2.imwrite(output_path, dilated)
    print(f'Dilated document saved: {output_path}')
