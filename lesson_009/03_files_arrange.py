# -*- coding: utf-8 -*-

import os, time, shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)

class FileSorter:
    """
    Программа для сортировки файлов из каталога источника(src) в каталог назначения(dst).
    Сортировка происходит по дате модификации файла в виде "/dst/year/month"
    Сортировка происходит с учетом подкаталогов.
    """
    def __init__(self, src, dst):
        if src:
            self.src = os.path.normpath(src)
        else:
            print('Не указан каталог источник.')
        if dst:
            self.dst = os.path.normpath(dst)
        else:
            print('Не указан каталог назначения.')

    def get_dirs(self, mtime=None):
        file_mdate = time.gmtime(mtime)
        year, mon = str(file_mdate.tm_year), str(file_mdate.tm_mon)
        file_dest = os.path.join(self.dst, *(year, mon if len(mon) != 1 else '0' + mon))
        return file_dest

    def make_dirs(self, dir=None):
        if not os.path.exists(dir):
            os.makedirs(dir)

    def copy_file(self, src=None, dst=None):
        if not os.path.exists(dst):
            shutil.copy2(src=src, dst=dst)

    def arrange(self):
        for dir_path, dir_names, file_names in os.walk(self.src):
            for file in file_names:
                file_mtime = os.path.getmtime(os.path.join(dir_path, file))
                file_dst = self.get_dirs(file_mtime)
                self.make_dirs(file_dst)

                file_dst = os.path.join(file_dst, file)
                file_src = os.path.join(dir_path, file)
                self.copy_file(src=file_src, dst=file_dst)

        if os.path.exists(self.dst):
            print('Сортировка завершена успешно.', self.dst)
        else:
            print('Ошибка! Проверьте пути к каталогам.', self.src, self.dst)


if __name__ == '__main__':
    src_dir = '/home/andrey/Pictures'
    dst_dir = '/home/andrey/Pictures/sorted'
    files = FileSorter(src=src_dir, dst=dst_dir)
    files.arrange()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
