import cv2
import numpy as np

kartinka = 'Леша.png'
img = cv2.imread(kartinka)
gray = cv2

dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None) #расширяем результат для разметки углов

img[dst > 0.01 * dst.max()] = [0, 0, 255]# тута диапозон порогового оптимального значения, завичит от изображения

cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()