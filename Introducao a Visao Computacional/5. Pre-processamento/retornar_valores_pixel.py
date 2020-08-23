#retornando valores de pixels 

import cv2
imagem = cv2.imread("imagemTeste.jpg") 

#valor da coordenada da matrix em pixels
valorPixel = imagem[150,150] 
print(valorPixel)
