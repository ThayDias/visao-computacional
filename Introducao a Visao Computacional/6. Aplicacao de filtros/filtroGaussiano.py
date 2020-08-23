import cv2

imgOriginal = cv2.imread("Train_2.jpg")
#                                               1     2
imgComFiltro = cv2.GaussianBlur(imgOriginal, (21,21), 8)
# 1: Tamanho da matriz. A quantidade que será aplicada (quanto maior o numero, mais embaçado) 
# *É recomendado que a máscara seja uma matriz quadrada, com número ímpar de linhas e colunas
# 2: Grau de suavização

cv2.imshow("Original", imgOriginal)
cv2.imshow("Com Filtro", imgComFiltro)

cv2.waitKey(0)
cv2.destroyAllWindows()