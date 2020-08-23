import cv2

#FUNÇÃO QUE LÊ A IMAGEM CARREGADA
#parametro 1: imagem a carregar
imagem = cv2.imread("imagemTeste.jpg")

#FUNÇÃO QUE EXIBE NUMA JANELA A IMAGEM CARREGADA
#parametro 1: nome da janela que vai exibir a imagem, variavel que recebeu a imagem
cv2.imshow("Imagem", imagem)

#FUNÇÃO QUE ESPERA O USUARIO REALIZAR UMA AÇÃO PARA FECHAR A TELA
#parametro 1: tempo de milisegundos em espera do usuario apertar uma tecla
cv2.waitKey(0)

#destroi as janelas criadas pelo programa e encerra
cv2.destroyAllWindows()