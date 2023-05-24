import cv2
import numpy as np 
image= cv2.imread('Citizenship1.jpg', cv2.IMREAD_GRAYSCALE)
sobelx= cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobely= cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobelx=np.absolute(sobelx)
sobey= np.absolute(sobely)
gradient= cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv2.imshow("sobel X", sobelx)
cv2.imshow("sobel Y", sobely)
cv2.imshow("Gradient", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()