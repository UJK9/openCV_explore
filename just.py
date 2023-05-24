import cv2
def crop(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred= cv2.GaussianBlur(gray, (5, 5), 0)
    edges= cv2.Canny(blurred, 100 , 200)
    contours,_ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key= cv2.contourArea)
    x,y,w,h = cv2.boundingRect(contour)
    cropped_img= image[y:y+h, x:x+w]
    return cropped_img
image_path= 'D:/op/Citizenship1.jpg'
crop_image= crop(image_path)
cv2.imwrite('D:/op/ou3/jj.jpg', crop_image)
