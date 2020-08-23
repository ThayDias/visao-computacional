import cv2
import numpy as np

imagemOriginal =  cv2.imread("imagemTeste.jpg", 0)
totalLinhas, totalColunas = imagemOriginal.shape

#centro da imagem, angulo de rotacao, escala
matriz = cv2.getRotationMatrix2D(
    (totalColunas / 2, totalLinhas / 2), 90, 1
)

#parametros WarpAffine: matrix da imagem, matrix de rotacao, tamanho da imagem
imagemRotacionada = cv2.warpAffine(
    imagemOriginal, 
    matriz,
    (totalColunas, totalLinhas)
)

cv2.imshow("Resultado", imagemRotacionada)

cv2.waitKey(0)
cv2.destroyAllWindows()