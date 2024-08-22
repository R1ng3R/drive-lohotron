import cv2
import numpy as np
import tensorflow as tf


def match_template(reference_image_path, camera_image_path):
    # Загрузка эталонного изображения и изображения с камеры
    reference_image = cv2.imread(reference_image_path, cv2.IMREAD_GRAYSCALE)
    camera_image = cv2.imread(camera_image_path, cv2.IMREAD_GRAYSCALE)

    # Преобразование изображений в формат, удобный для анализа
    reference_image = cv2.resize(reference_image, (100, 100))  # Измените размер по необходимости
    camera_image = cv2.resize(camera_image, (500, 500))  # Измените размер по необходимости

    # Выполнение корреляции шаблона
    result = cv2.matchTemplate(camera_image, reference_image, cv2.TM_CCOEFF_NORMED)

    # Нахождение максимального значения корреляции
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Определение порога совпадения
    threshold = 0.8

    if max_val >= threshold:
        print("Хорошо")
    else:
        print("Не найдено")


# Пути к изображениям
reference_image_path = 'path_to_reference_image.jpg'
camera_image_path = 'path_to_camera_image.jpg'

# Вызов функции
match_template(reference_image_path, camera_image_path)
