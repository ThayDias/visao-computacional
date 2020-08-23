import	cv2 
imagem	=	cv2.imread("imagemTeste.jpg")
#valor RGB do pixel anterior a alteração
print	imagem[150,150] 
#atribuindo novo valor RGB a um pixel 
imagem[150,150]	=	[255,255,255]	
print(imagem[150,150])
