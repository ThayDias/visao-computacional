import cv2

imagem = cv2.imread("Train_2.jpg", 0)

sobelx = cv2.Sobel(imagem, cv2.CV_8U, 1, 0,	ksize = 5)
sobely = cv2.Sobel(imagem, cv2.CV_8U, 0, 1,	ksize = 5)

cv2.imshow("Original", imagem)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()