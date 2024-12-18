import cv2
from functions import *
from corn import *

#
# path = input('Введите путь к изображению, которое необходимо обработать:\n')
for i in range(7):
    path = 'data/' + str(i+1) + '.png'

    img_bgr = cv2.imread(path)
    img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # Перевод и bgr в rgb
    # x = float(input('Введите параметр x_distortion:\n'))
    # y = float(input('Введите параметр y_distortion:\n'))

    x, y = 0.2, 0.2

    # Запуск функции:
    output_img = distortion(img, x, y)

    # Отображение результатов:
    plot_result(img, output_img)

    # запуск окна настроек
    interctive_window(path, itr=i)
