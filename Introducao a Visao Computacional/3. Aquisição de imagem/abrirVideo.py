import cv2

captura = cv2.VideoCapture("video.mp4")

# é preciso fazer uma repetição para mostrar todos os frames do video
while True:
    try:
        ret, frame = captura.read()
        cv2.imshow("Video", frame)

        # quando apertado a letra "q" sairá da repetição para fechar o video
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # no fim do video, não há mais frames para serem mostrados
    # por isso fiz um try except para que quando dê algum erro ele saia do video             
    except:
        break

captura.release()
cv2.destroyAllWindows()