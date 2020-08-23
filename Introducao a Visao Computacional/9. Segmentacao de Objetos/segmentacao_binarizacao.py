import	cv2 
import	numpy	as	np

#DUVIDAS: tentativa e erro? teria um jeito mais facil?
# como selecionar o machucado da folha?
#dessa forma é somente um pixel fixo? seria necessario criar um
#algoritmo q calculasse essa função sozinho?

imagemOriginal =  cv2.imread("imagemTeste.jpg", 0)

imgEscalada	=	cv2.resize( 
        imagemOriginal,	
        None,	
        fx	= 0.5,	
        fy	= 0.5,         
        interpolation	=	cv2.INTER_CUBIC 
    )

#objeto de interesse destacado em branco 
metodo	=	cv2.THRESH_BINARY_INV 

ret, imgBinarizada	=	cv2.threshold(imgEscalada,	135,	255,	metodo)

cv2.imshow("Imagem	Original",	imgEscalada) 
cv2.imshow("Imagem	Tratada",	imgBinarizada)

cv2.waitKey(0) 
cv2.destroyAllWindows()