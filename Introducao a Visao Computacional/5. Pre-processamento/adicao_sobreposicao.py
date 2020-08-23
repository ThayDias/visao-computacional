import	cv2

imagemFolhaDoente = cv2.imread("imagemBMP.bmp") 
imagemFolhaSaudavel	= cv2.imread("imagemBMP2.bmp")

#operacao de sobreposicao
imagem	=	cv2.add(imagemFolhaDoente,	imagemFolhaSaudavel)

cv2.imshow("Resultado",	imagem)

cv2.waitKey(0) 
cv2.destroyAllWindows()
