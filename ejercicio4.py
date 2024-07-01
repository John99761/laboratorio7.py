import cv2


img = cv2.imread("madera.jpeg")  


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow('Imagen en Blanco y Negro', gray)
cv2.waitKey(0)  
cv2.destroyAllWindows()  
