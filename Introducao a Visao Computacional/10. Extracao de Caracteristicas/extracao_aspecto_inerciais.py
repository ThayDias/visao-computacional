import	cv2 
import	numpy	as	np

imagem	=	cv2.imread("imagemBMP.bmp",	0) 
momentos	=	cv2.moments(imagem)

print(momentos)

#momentos de HU (retornam 7 momentos)

momentos	=	cv2.moments(imagem) 
momentosDeHu	=	cv2.HuMoments(momentos)

print(momentosDeHu)

#	Aplicando	a	transformação	logarítmica
 
print(-np.sign(momentosDeHu)	*	np.log10(np.abs(momentosDeHu)))

# centro geométrico

momentos	=	cv2.moments(objeto) 
cx	=	int(momentos['m10']	/	momentos['m00']) 
cy	=	int(momentos['m01']	/	momentos['m00'])

print(cx,	cy) 