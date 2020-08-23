import	cv2 
import	numpy	as	np 
from	matplotlib	import	pyplot	as	grafico

imagemOriginal	=	cv2.imread("imagemTeste.jpg",	0) 

#escala Correto
imagemEscalada	=	cv2.resize( 
        imagemOriginal,	
        None,	
        fx	= 0.5,	
        fy	= 0.5,         
        interpolation	=	cv2.INTER_CUBIC 
    )

#adição de contraste
imagemClara	=	cv2.add(imagemEscalada,	40) 
imagemEscura	=	cv2.add(imagemEscalada,	-40)

#exibição da imagem
cv2.imshow("Imagem	Original",	imagemEscalada) 
cv2.imshow("Imagem	Clara",	imagemClara) 
cv2.imshow("Imagem	Escura",	imagemEscura)

#grafico de escalonamento de luz
grafico.hist(imagemEscalada.ravel(),	256,	[0,256])

grafico.figure()
grafico.hist(imagemClara.ravel(),	256,	[0,256])

grafico.figure()
grafico.hist(imagemEscura.ravel(),	256,	[0,256])

grafico.show()
cv2.waitKey(0) 
cv2.destroyAllWindows()