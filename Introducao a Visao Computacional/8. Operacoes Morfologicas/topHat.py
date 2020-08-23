import cv2
import numpy as np

imagemOriginal = cv2.imread("Train_1.jpg", 0)

elementoEstruturante = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE, (25,25)
)

imagemProcessada = cv2.morphologyEx(
    imagemOriginal, cv2.MORPH_TOPHAT, elementoEstruturante
)

imagemTratada = cv2.add(imagemProcessada, imagemProcessada)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)
cv2.imshow("Final", imagemTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()