import	cv2
#mescla/mistura as duas imagens com fator de perda/transparencia

imagemFolhaDoente	=	cv2.imread("imagemBMP.bmp") 
imagemFolhaSaudavel	=	cv2.imread("imagemBMP2.bmp")

#src1: imagem1, alpha: intensidade img1, src2: imagem2, beta: intensidade img2, gamma: valor escalar
imagem	=	cv2.addWeighted(
                    imagemFolhaDoente,	
                    0.2, 
                    imagemFolhaSaudavel,	
                    1.0,	
                    0 
                )

cv2.imshow("Resultado",	imagem)
cv2.waitKey(0) 
cv2.destroyAllWindows() 