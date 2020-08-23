import	cv2 
import	statistics


imgBinaria	=	cv2.imread("imagemTesteBinariaBMP.bmp",	0) 
imgTonsDeCinza	=	cv2.imread("imagemTesteCinza.jpg",	0)
imgRGB	=	cv2.imread("imagemTeste.jpg")


#predominancia da cor
rolBinaria	=	imgBinaria.ravel() 
rolTonsDeCinza	=	imgTonsDeCinza.ravel()

print(statistics.mode(rolBinaria)) 
print(statistics.mode(rolTonsDeCinza)) 

#media dos pixels da imagem
# a função mean processa até 4 canais de cor
valorMedioRGB	=	cv2.mean(imgRGB) 
valorMedioCinza	=	cv2.mean(imgTonsDeCinza)

print(valorMedioRGB) 
print(valorMedioCinza) 