import	cv2 
import	numpy	as	np

imagemRGB	=	cv2.imread("imagemBMP.bmp") 
imagemTonsDeCinza	=	cv2.imread("imagemTesteBinariaBMP.bmp",	0)

tipo	=	cv2.THRESH_BINARY 
ret,	imgBinarizada	=	cv2.threshold(imagemTonsDeCinza,	127,	255,	tipo )

modo	=	cv2.RETR_TREE 
metodo	=	cv2.CHAIN_APPROX_SIMPLE

contornos,	hierarquia	=	cv2.findContours(imgBinarizada,	modo,	metodo )

objeto	=	contornos[0]

#	Obtendo	a	elipse 

ellipse	=	cv2.fitEllipse(objeto)

#	Desenhando	a	elipse	na	imagem	imagemRGB 

cv2.ellipse(imagemRGB,	ellipse,	(0,	255,	0),	2) 

cv2.imshow("Elipse	ajustada",	imagemRGB)

print(ellipse)

cv2.waitKey(0) 
cv2.destroyAllWindows() 