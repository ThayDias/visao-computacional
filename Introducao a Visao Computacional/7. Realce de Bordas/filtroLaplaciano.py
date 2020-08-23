import cv2

imgOriginal = cv2.imread("Train_2.jpg", 0)
imgLaplacian = cv2.Laplacian(imgOriginal, cv2.CV_8U)
imgRealcada = cv2.subtract(imgOriginal, imgLaplacian)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgLaplacian)
cv2.imshow("Realcada", imgRealcada)

cv2.waitKey(0)
cv2.destroyAllWindows()