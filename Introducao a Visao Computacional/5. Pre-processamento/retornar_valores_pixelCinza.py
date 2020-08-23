
import	cv2 
imagem	= cv2.imread("imagemTeste.jpg")

#modificando a cor para cinza
imagem	=	cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY) 

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

#retonando o valor atraves de uma coordenada de pixels
valorPixel	=	imagem[150,150] 

#o valor retornado refere-se a quantidade de luz do pixel
print(valorPixel)
