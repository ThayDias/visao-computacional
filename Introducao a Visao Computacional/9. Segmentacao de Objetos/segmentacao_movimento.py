import cv2
import numpy as np

imagemA =  cv2.imread("imagemTeste.jpg")
imagemB =  cv2.imread("imagemTeste3.jpg")

imgEscaladaA	=	cv2.resize( 
        imagemA,	
        None,	
        fx	= 0.5,	
        fy	= 0.5,         
        interpolation	=	cv2.INTER_CUBIC 
    )

imgEscaladaB	=	cv2.resize( 
    imagemB,	
    None,	
    fx	= 0.5,	
    fy	= 0.5,         
    interpolation	=	cv2.INTER_CUBIC 
)

#nova imagem da diferença da imagem A para imagem B 
#as duas imagens devem ser posições diferentes do mesmo objeto observado
imgRGB	=	cv2.subtract(imagemA, imagemB) 

#montagem de uma nova imagem com a diferença e retirando o segundo plano
imgHSV	=	cv2.cvtColor(imgRGB,	cv2.COLOR_BGR2HSV)


tomClaro	=	np.array([0,	120,	120]) 
tomEscuro	=	np.array([180,	255,	255])


imgSegmentada	=	cv2.inRange(imgHSV,	tomClaro,	tomEscuro)

imgSegmentadaEscalada	=	cv2.resize( 
    imgSegmentada,	
    None,	
    fx	= 0.5,	
    fy	= 0.5,         
    interpolation	=	cv2.INTER_CUBIC 
)


cv2.imshow("Segmentada",	imgSegmentadaEscalada)

cv2.waitKey(0) 
cv2.destroyAllWindows()