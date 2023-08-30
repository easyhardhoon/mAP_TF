import cv2

image_path = '1022.jpg'
img = cv2.imread(image_path)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

