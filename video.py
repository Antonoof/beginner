import cv2

# связываем файл video.avi с переменной capImg
capImg = cv2.VideoCapture('выживший.mp4')

while(capImg.isOpened()):
    # получаем кадр из видеопотока файла
    # кадры по очереди считываются в переменную frame
    ret, frame = capImg.read()
    # если кадры закончились
    if frame is None:
        break # прерываем работу цикла
    # показываем кадр из файла в окне video_fi le
    cv2.imshow(f"video_file", frame)
    # организуем выход из цикла по нажатию клавиши,
    # ждем 30 миллисекунд нажатия, записываем код
    # нажатой клавиши
    key_press = cv2.waitKey(30)
    # если код нажатой клавиши совпадает с кодом «q»,
    if key_press == ord('q'):
        break # то прервать цикл while
# освобождаем память от переменной capImg
capImg.release()
# закрываем все окна opencv
cv2.destroyAllWindows()