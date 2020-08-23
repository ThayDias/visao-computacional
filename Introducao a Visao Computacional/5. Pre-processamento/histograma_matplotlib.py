import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagem =  cv2.imread("imagemBMP.bmp", 0)
#parametros: imagem, quantidade de elementos, intervalo de elementos (0 a 255)
#ravel(): transforma a quantidade de pixels em um vetor
grafico.hist(imagem.ravel(), 256, [0, 256])
grafico.show()
