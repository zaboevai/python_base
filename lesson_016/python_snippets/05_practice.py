# -*- coding: utf-8 -*-

#
# 16.05 Практика
#

# Задача: взять изображения коллег с сайта, пририсовать им усы и сохранить в базу данных
import cv2
import bs4
import peewee
import requests

# Шаг 1 - выкачиваем картинки с https://course.skillbox.ru/profession-python

html = requests.get('https://course.skillbox.ru/profession-python').text

soup = bs4.BeautifulSoup(html, 'html.parser')
all_images = soup.find_all('img')
# print('\n'.join(str(t.get('data-original', t.get('src'))) for t in all_images if 'Mask_Group' in str(t)))

downloaded_files = set()
for tag in all_images:
    url = tag.get('data-original', tag.get('src'))
    if url:
        filename = url.split('/')[-1]
        filename_full = f'external_data/photos/{filename}'
        if filename_full in downloaded_files:
            filename_full = f'external_data/photos/1{filename}'
        downloaded_files.add(filename_full)
        with open(filename_full, 'wb') as f:
            f.write(requests.get(url).content)


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_mustache(image, x, y, w, h):
    mw = w * 2 // 5
    mh = h // 10
    mx = x + w // 2 - mw // 2
    my = y + h * 2 // 3
    # cv2.rectangle(image, (mx, my), (mx+mw, my+mh), (255, 255, 0), 10)
    hair_w = max(mw // 20, 1)
    for dx in range(mw // hair_w):
        cv2.line(image, (mx + hair_w * dx, my), (mx + hair_w * (dx + 1), my + mh), (0, 0, 0), 1)
        cv2.line(image, (mx + hair_w * dx, my + mh), (mx + hair_w * (dx + 1), my), (0, 0, 0), 1)


database = peewee.SqliteDatabase("external_data/Mustached.db")


class Mustached(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = database


Mustached.create_table()


# Шаг 2 - распознаем лица

for image_path in downloaded_files:
    face_cascade = cv2.CascadeClassifier('external_data/haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)

    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        # print('FAIL', image_path)
        continue

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10)
    )
    if len(faces):
        print(image_path)

# Шаг 3 - рисовка усов

        for (x, y, w, h) in faces:
            draw_mustache(image, x, y, w, h)

# Шаг 4 - пишем в файл и базу

        mustached_image_path = image_path.replace('photos', 'photos_results')
        cv2.imwrite(mustached_image_path, image)
        Mustached.create(name=mustached_image_path)


print(list(Mustached.select()))
