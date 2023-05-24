import cv2 
import numpy as np 

kernel = np.ones((3,3), np.uint8)
output_path= 'D:/op/ou2/ero.jpg'
def erode():
    image = cv2.imread('Citizenship2.jpg')

    g= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eroded = cv2.erode(image, kernel, iterations=1)
    cv2.imwrite(output_path, eroded)
    print(f'Eroded document saved: {output_path}')
