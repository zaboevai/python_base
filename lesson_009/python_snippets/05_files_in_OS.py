# -*- coding: utf-8 -*-

import os

# Все файлы лежат на диске и имеют путь в файловой системе. Как работать с файлами на уровне ОС?
# Есть встроенные модули для этого: os, os.path, shutil
# Пригодятся они для написания скриптов-аналогов bash (.bat файлов в Windows)

path = 'C:\\Windows\\help'

# Пройтись по всем файлам в директории.
for dirpath, dirnames, filenames in os.walk(path):
    print(dirpath, dirnames, filenames)

# В разных ОС путь записывается по разному: привести к нужному в этой ОС виду
os.path.normpath(path)

# Получить размер файла.
os.path.getsize(path)

# Получить дату модификации файла.
os.path.getmtime(path)

# вернет кол-во секунд с начала эпохи. преобразовать в года/месяца можно так
import time
time.gmtime(secs)  # вернет тьюпл со временем https://docs.python.org/3/library/time.html#time.struct_time

# сформирвать правильный путь к файлу с учетом особенностей ОС.
# os.path.join(path1[, path2[, ...]])

# получить родительскую директорию
os.path.dirname(path)
# получить родительскую директорию текущего модуля
os.path.dirname(__file__)

# это самые основние, остальные см https://goo.gl/AB6aDQ


# а теперь все вместе
import time
import os

path = 'C:/Windows/help'
path_normalized = os.path.normpath(path)
print(path_normalized)

count = 0
for dirpath, dirnames, filenames in os.walk(path_normalized):
    print('*' * 27)
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    count += len(filenames)
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        secs = os.path.getmtime(full_file_path)
        file_time = time.gmtime(secs)
        if file_time[0] == 2013:
            # выводим только файлы за 2013 год
            print(full_file_path, secs, file_time)
print(count)

print(__file__, os.path.dirname(__file__))