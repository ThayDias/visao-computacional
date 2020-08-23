import cv2
import numpy as np

imagemOriginal = cv2.imread("Train_1.jpg", 0)

elementoEstruturante = cv2.getStructuringElement(
    cv2.MORPH_CROSS, (100, 100)
)

imagemProcessada = cv2.morphologyEx(
    imagemOriginal, cv2.MORPH_OPEN, elementoEstruturante
)

imagemSubtraida = cv2.subtract(imagemOriginal, imagemProcessada)
imagemTratada = cv2.add(imagemSubtraida, imagemSubtraida)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)
cv2.imshow("Subtraida", imagemSubtraida)
cv2.imshow("Tratada", imagemTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()