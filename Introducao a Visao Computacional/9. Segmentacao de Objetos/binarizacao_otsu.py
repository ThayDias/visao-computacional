import	cv2 
import	numpy	as	np

imgOriginal	=  cv2.imread("imagemTeste.jpg", 0)

imgEscalada	=	cv2.resize( 
        imgOriginal,	
        None,	
        fx	= 0.5,	
        fy	= 0.5,         
        interpolation	=	cv2.INTER_CUBIC 
    )
#objeto de interesse destacado em branco + algoritmo de otsu
tipo	=	cv2.THRESH_BINARY_INV	+	cv2.THRESH_OTSU

limiar,	imgBinarizada	=	cv2.threshold(
                                imgEscalada,	
                                0,	
                                255,	
                                tipo)

print(limiar)
#valor limiar de 125.0

cv2.imshow("Imagem	Original",	imgEscalada) 
cv2.imshow("Imagem	Tratada",	imgBinarizada)
cv2.waitKey(0) 
cv2.destroyAllWindows()