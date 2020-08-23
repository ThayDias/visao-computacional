import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagem =  cv2.imread("imagemBMP.bmp")
azul, verde, vermelho = cv2.split(imagem)

grafico.hist(azul.ravel(), 256, [0, 256])
#figure(): geração de uma nova figura 
grafico.figure()
grafico.hist(verde.ravel(), 256, [0, 256])

grafico.figure()
grafico.hist(vermelho.ravel(), 256, [0, 256])

grafico.show()

