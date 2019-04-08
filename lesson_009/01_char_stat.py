# -*- coding: utf-8 -*-
import zipfile
import os
import pprint


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
# Ширину таблицы подберите по своему вкусу

class CharStat:
    def __init__(self, path_to_file, path_to_archive, filename_in_archive):
        self.path_to_file = path_to_file
        self.stat = {}
        if zipfile.is_zipfile(path_to_file):
            self.zfile = zipfile.ZipFile(self.path_to_file, 'r')
            if self.find_file(filename_in_archive):
                self.path_to_archive = path_to_archive
                self.file_name = filename_in_archive
                self.zfile.extractall(self.path_to_archive)
        else:
            self.file_name = os.path.basename(path_to_file)

    def find_file(self, name):
        for filename in self.zfile.namelist():
            if name == filename:
                return True
            else:
                return False

    def print_header(self):
        print(f'')
        print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')
        print('|', '  Буква  ', '|', '  Кол-во  ', '|', sep='')
        print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')

    def print_result(self):
        print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')
        print('|', '  Итого  ', '|', f'{sum(self.stat.values()): ^10}', '|', sep='')
        print('+', f'{chr(45):-^9}', '+', f'{chr(45):-^10}', '+', sep='')

    def print_body(self):
        if not self.stat:
            self.get_stat()

        for char, cnt in sorted(self.stat.items()):
            print('|', f'{char: ^9}', '|', f'{cnt: ^10}', '|', sep='')

    def print_stat(self):
        self.print_header()
        self.print_body()
        self.print_result()

    def get_stat(self):
        with open(os.path.join(self.path_to_archive, self.file_name), mode='r', encoding='CP1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if self.stat.setdefault(char, 0) == self.stat[char]:
                            self.stat[char] += 1
        return self.stat


if __name__ == '__main__':
    src_file_path = './python_snippets/voyna-i-mir.txt.zip'
    path_to_archive = './python_snippets/arch'
    filename_in_archive = 'voyna-i-mir.txt'

    war_and_peace = CharStat(path_to_file=src_file_path,
                             path_to_archive=path_to_archive,
                             filename_in_archive=filename_in_archive)
    war_and_peace.print_stat()
