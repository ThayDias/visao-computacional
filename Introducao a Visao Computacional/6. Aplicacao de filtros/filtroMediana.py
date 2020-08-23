import cv2

imgOriginal = cv2.imread("Train_1.jpg")
#                                          intensidade, *impar
imgComFiltro = cv2.medianBlur(imgOriginal, 11)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Com Filtro", imgComFiltro)

cv2.waitKey(0)
cv2.destroyAllWindows()
