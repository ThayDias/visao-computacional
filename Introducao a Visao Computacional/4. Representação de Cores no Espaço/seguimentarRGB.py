import cv2

# Carregando imagem RGB e segmentando canais
imagem = cv2.imread("imagemTeste.jpg")
azul, verde, vermelho = cv2.split(imagem)
# A biblioteca OpenCV trata o espaço de cor RGB como BGR invertendo a ordem dos canais

# Exibindo imagens dos canais separados
cv2.imshow("Canal R", vermelho)
cv2.imshow("Canal G", verde)
cv2.imshow("Canal B", azul)

# Salvando imagens dos canais separados
cv2.imwrite("araras-canal-vermelho.jpeg", vermelho)
cv2.imwrite("araras-canal-verde.jpeg", verde)
cv2.imwrite("araras-canal-azul.jpeg", azul)

# Combinando os três canais em uma única imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()