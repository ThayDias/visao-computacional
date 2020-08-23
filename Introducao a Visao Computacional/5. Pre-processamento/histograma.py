import cv2
#imagem em bitmap permite uma melhor fidelidade das cores 
#imagens em jpeg podem ter tons intermediarios de cinza 
#parametro 0 indica imagem em tons de cinza
imagem =  cv2.imread("imagemBMP.bmp", 0)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

totalPixelsPreto = 0 
totalPixelsBranco = 0

for x in range(0, 499):
    for y in range(0, 499):
        if imagem[x, y] == 255:
            totalPixelsBranco += 1
        else:
            totalPixelsPreto += 1

print(totalPixelsBranco)
print(totalPixelsPreto)
