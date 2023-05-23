import cv2
import numpy as np
import os 

kernel= np.ones((3,3), np.uint8)
def crop(input_folder, out_folder):
    
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('jpg', 'png', 'jpeg'))]
    print(f"Processing {len(image_files)} image files.")
    for file in image_files:
        image_path = os.path.join(input_folder, file)
        output_path = os.path.join(out_folder, file)
        crop_document(image_path, output_path)
        crop_erode(image_path, output_path)
        crop_dilate(image_path, output_path)
        crop_blur(image_path, output_path)
    
def crop_document(image_path, output_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #Find contours in the binary image
    contours,_ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0 :
        print(f'No document found in the image: {image_path}')
        return
    #Find largest area contours 
    document_contour = max(contours, key= cv2.contourArea)
    x,y,w,h = cv2.boundingRect(document_contour)
    cropped_image = image[y:y+h, x:x+w]
    cv2.imwrite(output_path, cropped_image)
    print(f'Cropped document saved: {output_path}')

def crop_erode(image_path, output_path):
    imag = cv2.imread(image_path)
    gre = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)
    eroded = cv2.erode(imag, kernel, iterations = 1)
    cv2.imwrite(output_path+ '.jpg', eroded)
def crop_dilate(image_path, outp_path):
    ima = cv2.imread(image_path)
    gr= cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY )
    dilated = cv2.dilate(ima, kernel, iterations = 1)
    cv2.imwrite(outp_path+ '.jpg', dilated)
def crop_blur(image_path, ou_path):
    ima = cv2.imread(image_path)
    blurred = cv2.GaussianBlur(ima, (5,5), 0)
    cv2.imwrite(ou_path+ '.jpg', blurred)

image_folder = 'D:\openCV_explore\images'
output_folder= 'D:\openCV_explore\ouput'
crop(image_folder, output_folder)

