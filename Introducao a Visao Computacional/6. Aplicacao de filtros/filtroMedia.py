import cv2

imgOriginal	= cv2.imread("Train_1.jpg")
#                                    Tamanho da matriz. A quantidade que será aplicada (quanto maior o numero, mais embaçado)
imgComFiltro = cv2.blur(imgOriginal, (20,20))

cv2.imshow("Original", imgOriginal)
cv2.imshow("Com Filtro", imgComFiltro)

cv2.waitKey(0)
cv2.destroyAllWindows()