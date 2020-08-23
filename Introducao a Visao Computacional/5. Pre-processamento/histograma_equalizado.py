import	cv2 
import	numpy	as	np 
from	matplotlib import	pyplot	as	grafico

#o processo de equalizar uma imagem aumenta a sua nitidez
imagemOriginal =  cv2.imread("imagemBMP.bmp", 0)

#função de equalização da imagem
imagemEqualizada = cv2.equalizeHist(imagemOriginal)

#exibição da imagem
cv2.imshow("Imagem	Original",	imagemOriginal) 
cv2.imshow("Imagem	Equalizada",	imagemEqualizada)

grafico.hist(imagemOriginal.ravel(),	256,	[0,256])

grafico.figure(); 
grafico.hist(imagemEqualizada.ravel(),	256,	[0,256])

grafico.show() 