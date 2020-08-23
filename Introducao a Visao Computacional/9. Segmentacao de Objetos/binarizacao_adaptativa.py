import	cv2 
import	numpy	as	np

imagemOriginal =  cv2.imread("imagemTeste2.jpg", 0)

imgEscalada	=	cv2.resize( 
        imagemOriginal,	
        None,	
        fx	= 0.5,	
        fy	= 0.5,         
        interpolation	=	cv2.INTER_CUBIC 
    )

imgTratada	=	cv2.medianBlur(imgEscalada,	7)

imgBinarizada	=	cv2.adaptiveThreshold(		
                            imgTratada,	
                            255,
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,	
                            cv2.THRESH_BINARY_INV,	
                            11,	
                            5 )

cv2.imshow("Imagem	Original",	imgEscalada) 
cv2.imshow("Imagem	Tratada",	imgBinarizada)
cv2.waitKey(0)
cv2.destroyAllWindows() 