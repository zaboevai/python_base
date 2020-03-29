# -*- coding: utf-8 -*-

#
# 16.03 Работа с изображениями
#

# Изображение является набором пикселей, которые в свою очередь представляют
# из себя ячейку с 1-3 значениями (в зависимости от цветовой модели, у RGB например 3 значения),
# отвечающими за цвет пикселя.
# Изменив значения пикселей, мы можем менять и само изображение.

# Pillow - одна из библиотек пайтона, позволяющая нам работать с изображениями
# pip install pillow

from PIL import Image, ImageDraw

image = Image.open("external_data/mm_andy.jpg")  # Загружаем изображение
pixels = image.load()  # Загружаем значения пикселей
draw = ImageDraw.Draw(image)  # Создаем кисточку
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту.

print(f'Ширина изображения - {width}, высота - {height}')


# Попробуем испортить известную работу Энди Уорхолла,
# получив негатив одного из Микки Маусов.
# Для этого нам необходимо пройтись по всем пикселям
# и вычесть их значение из 255


def negativ(pix):
    for i in range(width//2):
        for j in range(height//2 - 75):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))


# Второму Микки добавим эффект оттенки серого
# для этого нужно "усреднить" каждый пиксель:


def gray_shapes(pix):
    for i in range(width//2, width):
        for j in range(height//2 - 75):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = (a + b + c) // 3
            draw.point((i, j), (s, s, s))


# Третьему Микки наложим эффект Сепия
# Помимо усреднения, мы добавим коэффициент
# depth к значениям пикселей.
# + проверка, чтобы значения не вышли за границу 255


def sepia(pix):
    depth = 30
    for i in range(width//2):
        for j in range(height//2 - 75, height - 75):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = (a + b + c) // 3
            a = s + depth * 2
            b = s + depth
            c = s
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))


# Проверим скорость работы наших функций:

import time
start = time.monotonic()
negativ(pixels)
sepia(pixels)
gray_shapes(pixels)
result = time.monotonic() - start
print(f"Все три функции выполнились за : {result} секунд")

# Обработка изображений требует много ресурсов
# Т.к. нам необходимо провести операции над 3133х3200х3(в данном примере) значениями
# и это только одно изображение.

# Одним из решений этой проблемы являются обертки к быстрым C/C++ библиотекам

# В конце концов удалим "кисть" и сохраним результат
del draw
image.save('external_data/mm_effects.jpg', 'JPEG')

# Обрезка изображений:
img_to_crop = image.crop((150, 75, width//2, height//2 - 75))
img_to_crop.save('external_data/mm_cropped.jpg', 'JPEG')

# Ресайз + поворот:
img_to_resize = img_to_crop
img_to_resize.thumbnail((1024, 1024))
img_to_resize.rotate(180)
img_to_resize.save('external_data/mm_resize_rotate.jpg', 'JPEG')

# Наложение одного изображения на другое:
# Координатами задаётся положение левого верхнего угла
# изображения, которое вставляют, на бОльшем изображении.

img_to_paste = Image.open('external_data/mm_effects.jpg')
img_to_paste.paste(img_to_resize, (width//2 - 512, height//2 - 588))
img_to_paste.save('external_data/mm_paste.jpg', 'JPEG')


#
# OpenCV - более продвинутая библиотека для редактирования изображений и видео,
# очень популярна в областях машинного обучения связанных с изображениями.
# https://opencv.org

# pip install opencv-contrib-python - установка из заранее собранных пакетов

import cv2

image_cv2 = cv2.imread('external_data/girl.jpg')
# Загрузка происходит не в привычном нам RGB,а в BGR!


# Добавим небольшую функцию для отображения изображений в окнах windows:
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Возможности OpenCV:

# Ресайз слайсами:
cropped = image_cv2[250:2000, 100:1500]
viewImage(cropped, 'Cropped version')

# Процентное изменение размера:

scale_percent = 20  # Процент от изначального размера
width = int(image_cv2.shape[1] * scale_percent / 100)
height = int(image_cv2.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image_cv2, dim, interpolation=cv2.INTER_AREA)
viewImage(resized, 'Resized version')

# Изменение цветовой гаммы:

gray_image = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)
viewImage(gray_image, 'Gray version')
# Интересно, что gray_image — это одноканальная версия изображения
# Что заметно уменьшает количество значений для обработки

# Рисование на изображениях:

image_with_line = image_cv2.copy()
cv2.line(image_with_line, (1000, 100), (1000, 2000), (0, 255, 0), 10)
# Для отрисовки линии необходимы координаты начала и конца, цвет и ширина линии
viewImage(image_with_line, 'Line')

image_with_rectangle = image_cv2.copy()
cv2.rectangle(image_with_rectangle, (100, 100), (1500, 2000), (0, 255, 255), 10)
# Для отрисовки прямоугольника необходимы координаты левого верхнего и правого нижнего углов
# + цвет линии и её ширина
viewImage(image_with_rectangle, 'Rectangle')

# И немного магии!
# Пример с распозаванием лиц:

image_path = 'external_data/girl.jpg'
face_cascade = cv2.CascadeClassifier('external_data/haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10)
)
# Рисуем квадраты вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 10)
viewImage(image, 'Detected face')
