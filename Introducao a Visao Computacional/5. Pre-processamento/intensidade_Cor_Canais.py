
#VERIFICANDO A INTENSIDADE DO CANAL AZUL - B
import	cv2 
imagem	= cv2.imread("imagemTeste.jpg")
valorPixelCanalAzul	=	imagem[150,150, 0] 
print(valorPixelCanalAzul)

#VERIFICANDO A INTENSIDADE DO CANAL VERDE - G
import	cv2 
imagem	= cv2.imread("imagemTeste.jpg")
valorPixelCanalVerde	=	imagem[150,150, 1] 
print(valorPixelCanalVerde)

#VERIFICANDO A INTENSIDADE DO CANAL VERMELHO - R
import	cv2 
imagem	= cv2.imread("imagemTeste.jpg")
valorPixelCanalVermelho	=	imagem[150,150, 2] 
print(valorPixelCanalVermelho)
