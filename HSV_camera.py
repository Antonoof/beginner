# подключение библиотеки numpy
import numpy as np
# подключение библиотеки opencv
import cv2
# создаем «пустую» функцию
def nothing(*arg):
    pass
# создаем окно настроек с именем Set
cv2.namedWindow('Set')
# создаем 6 ползунков для настройки цветового фильтра
# для компонент H,S,V соответственно
cv2.createTrackbar('h1', 'Set', 0, 180, nothing)
cv2.createTrackbar('s1', 'Set', 0, 255, nothing)
cv2.createTrackbar('v1', 'Set', 0, 255, nothing)
cv2.createTrackbar('h2', 'Set', 180, 180, nothing)
cv2.createTrackbar('s2', 'Set', 255, 255, nothing)
cv2.createTrackbar('v2', 'Set', 255, 255, nothing)
# связываем видеопоток файла video.avi с переменной
# capImg
capImg = cv2.VideoCapture(0)
# открываем файл с видео
while True:
    # получаем кадр из видеопотока файла,
    # кадры по очереди считываются в переменную frame
    ret, frame = capImg.read()
    # если кадры закончились, то прерываем цикл
    if frame is None:
        break
    # переводим кадр в цветовое пространство HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
    # вводим логическую переменную для выхода из
    # программы
    cl_pr = False
    # запускаем цикл со стоп-кадром по настройке
    # фильтра
    # считываем значения бегунков для H,S,V
    # соответственно
    h1 = cv2.getTrackbarPos('h1', 'Set')
    s1 = cv2.getTrackbarPos('s1', 'Set')
    v1 = cv2.getTrackbarPos('v1', 'Set')
    h2 = cv2.getTrackbarPos('h2', 'Set')
    s2 = cv2.getTrackbarPos('s2', 'Set')
    v2 = cv2.getTrackbarPos('v2', 'Set')
    # формируем нижнюю и верхнюю границы цветового
    # фильтра
    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)
    # накладываем фильтр на кадр в цветовом
    # пространстве HSV,
    # результат записываем в RealTimeMask
    RealTimeMask = cv2.inRange(frame_hsv, h_min,h_max)
    # показываем исходный кадр в окне Original
    cv2.imshow('Original', frame)
    # показываем фильтрованный кадр в окне result
    cv2.imshow('result', RealTimeMask)
    # организуем управление программой по нажатию
    # клавиши, ждем 30 миллисекунд нажатия,
    # записываем код нажатой клавиши
    key_press = cv2.waitKey(10)
    # если код клавиши равен коду символа «n»
    if key_press == ord('n'):
    # прерываем цикл показа текущего кадра
    # для перехода к следующему
        break
        # если код клавиши равен коду символа «q»
    elif key_press == ord('q'):
    # переменной выхода из программы присваиваем
    # True
        cl_pr = True
    # прерываем цикл показа текущего кадра
        break
    # если переменная выхода из программы True
    if cl_pr:
    # прерываем цикл считывания кадров
        break
capImg.release()
cv2.destroyAllWindows()