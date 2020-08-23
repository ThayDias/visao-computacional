import	cv2

imagemFolhaDoente	=	cv2.imread("imagemBMP.bmp") 
imagemFolhaSaudavel	=	cv2.imread("imagemBMP2.bmp")

#subtrai a primeira da segunda imagem
imagem	=	cv2.subtract(imagemFolhaDoente,	imagemFolhaSaudavel)

cv2.imshow("Resultado",	imagem)
cv2.waitKey(0) 
cv2.destroyAllWindows()