# подключение библиотеки numpy
import numpy as np
# подключение библиотеки opencv
import cv2
# задаем путь к файлу с картинкой
# если файл с картинкой и файл с программой находятся
# в одной папке, то это будет просто имя графического
# файла
fileName = 'pp.jpg'
# считываем данные графического файла в переменную
# image
image = cv2.imread(fileName)
# конвертируем исходное изображение в цветовую модель
# HSV
# результат записываем в переменную hsv_img
hsv_img = cv2.cvtColor( image, cv2.COLOR_BGR2HSV )
# подбираем параметры цветового фильтра для выделения
# нашего объекта (указанные числовые значения могут
# отличаться)
hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)
# применяем цветовой фильтр к исходному изображению,
# результат записываем в переменную hsv_msk
hsv_msk = cv2.inRange( hsv_img, hsv_min, hsv_max )
# ищем контуры и записываем их в переменную contours
# в режиме поиска всех контуров без группировки
# cv2.RETR_LIST для хранения контуров используем
# метод cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours( hsv_msk,
cv2.RETR_LIST,
cv2.CHAIN_APPROX_SIMPLE)
# отображаем все контуры поверх исходного изображения,
# цвет синий, толщина линии 3, сглаженная
cv2.drawContours( image, contours, -1, (255,0,0),
3, cv2.LINE_AA, hierarchy, 2)
# выводим итоговое изображение в окно contours
cv2.imshow('contours', image)
# ждем нажатия любой клавиши и закрываем все окна
cv2.waitKey()
cv2.destroyAllWindows()