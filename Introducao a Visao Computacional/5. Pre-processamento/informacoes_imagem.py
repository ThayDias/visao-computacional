import	cv2 
imagem	=	cv2.imread("imagemTeste.jpg")
#RETORNANDO IMAGEM COLORIDA
#metodo shape retorna o nº de linhas, nº de colunas e canais de cor
print(imagem.shape) 
#retorno de um array 
#[714 linhas, 720 colunas, 3 canais de cor]



#RETORNANDO IMAGEM CINZA
imagemCinza	=	cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY) 
#metodo shape em imagens cinzas retorna somente linhas e colunas
print(imagemCinza.shape) 
#retorno de um array 
#[714 linhas, 720 colunas]

#o metodo size retorna a quantidade total de pixel da imagem (linhaxcoluna)
print(imagem.size) 