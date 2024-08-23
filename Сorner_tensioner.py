import cv2


def resize_image_to_larger(larger_image_path, smaller_image_path, output_path):
    # Загрузка изображений
    larger_img = cv2.imread('1.png')
    smaller_img = cv2.imread('2.png')

    # Проверка успешности загрузки
    if larger_img is None:
        raise ValueError("Не удалось загрузить большее изображение.")
    if smaller_img is None:
        raise ValueError("Не удалось загрузить меньшее изображение.")

    # Получение размеров большего изображения
    larger_height, larger_width = larger_img.shape[:2]

    # Изменение размера меньшего изображения до размеров большего
    resized_smaller_img = cv2.resize(smaller_img, (larger_width, larger_height), interpolation=cv2.INTER_LINEAR)

    # Сохранение результата
    cv2.imwrite(output_path, resized_smaller_img)
    print(f"Изображение сохранено как {output_path}")


# Пример использования
resize_image_to_larger('path_to_larger_image.jpg', 'path_to_smaller_image.jpg', 'path_to_output_image.jpg')
