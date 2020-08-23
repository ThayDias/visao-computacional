import	cv2 
import	numpy	as	np

imagemOriginal =  cv2.imread("imagemTeste.jpg")

#parametros resize: imagem, imagem de saida, fx = escala horizontal, fy = escala vertical, interpolacao 

imagemModificada	=	cv2.resize( 
        imagemOriginal,	
        None,	
        fx	= 0.5,	
        fy	= 0.5,         
        interpolation	=	cv2.INTER_CUBIC 
    )

cv2.imshow("Resultado",	imagemModificada)

cv2.waitKey(0) 
cv2.destroyAllWindows() 