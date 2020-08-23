import cv2

# Carregando a imagem em RGB
imagem = cv2.imread("imagemTeste.jpg")

# Convertendo e exibindo a imagem em tons de cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # RGB "to" GRAY
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()