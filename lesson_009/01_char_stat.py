# -*- coding: utf-8 -*-
import zipfile
import os
from termcolor import cprint


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
    def __init__(self, path_to_file=None, path_to_archive=None, filename_in_archive=None):
        self.stat = {}
        self.is_data_ready = False

        if path_to_file:
            self.path_to_file = path_to_file
            if self.check_path_to_file():
                self.file_name = os.path.basename(path_to_file)
                self.is_data_ready = True
        else:
            self.path_to_archive = path_to_archive
            self.filename_in_archive = filename_in_archive
            if path_to_archive or filename_in_archive:
                if self.check_archive():
                    self.zfile = None
                    self.path_to_file = path_to_archive
                    self.file_name = filename_in_archive
                    self.unzip()
                    self.is_data_ready = True
            else:
                cprint('Файл не найден', color='red')

        if self.is_data_ready:
            print('Данные готовы к обработке.')
        else:
            cprint('Не удалдось подготовить данные к обработке.', color='red')

    def check_path_to_file(self):
        if self.path_to_file:
            if os.path.isfile(self.path_to_file):
                cprint(f'Обработка файла {self.path_to_file}!', color='cyan')
                return True
            else:
                cprint('Файл не найден!', color='red')
        else:
            cprint('Не указан файл для анализа из архива!', color='red')
        return False

    def check_archive(self):
        if self.path_to_archive:
            if zipfile.is_zipfile(self.path_to_archive):
                if not self.filename_in_archive:
                    cprint('Не указан файл для анализа из архива!', color='red')
                else:
                    fn = os.path.join(os.path.dirname(self.path_to_archive), self.filename_in_archive)
                    cprint(f'Обработка файла {fn}!', color='cyan')
                    return True
            else:
                cprint(f'Указанный файл {path_to_archive} не архив !', color='red')
        else:
            cprint('Не указан путь к архиву!', color='red')

        return False

    def find_file(self, name):
        for filename in self.zfile.namelist():
            if name == filename:
                return True
            else:
                return False

    def unzip(self):
        self.zfile = zipfile.ZipFile(self.path_to_file, 'r')
        if self.find_file(os.path.join(os.path.dirname(self.path_to_file), self.file_name)):
            os.remove(os.path.join(os.path.dirname(self.path_to_file), self.file_name))
        self.zfile.extractall(os.path.dirname(self.path_to_file))

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

        for char, cnt in sorted(self.stat.items()):
            print('|', f'{char: ^9}', '|', f'{cnt: ^10}', '|', sep='')

    def print_stat(self):
        if self.is_data_ready:
            if not self.stat:
                self.get_stat()

            self.print_header()
            self.print_body()
            self.print_result()

    def get_stat(self):
        if self.is_data_ready:
            with open(os.path.join(os.path.dirname(self.path_to_file), self.file_name), mode='r',
                      encoding='CP1251') as file:
                for line in file:
                    for char in line:
                        if char.isalpha():
                            self.stat[char] = self.stat.setdefault(char, 0) + 1
            return self.stat


if __name__ == '__main__':
    src_file_path = './python_snippets/voyna-i-mir.txt'
    path_to_archive = './python_snippets/voyna-i-mir.txt.zip'
    filename_in_archive = 'voyna-i-mir.txt'

    war_and_peace = CharStat(path_to_file=src_file_path,
                             path_to_archive=path_to_archive,
                             filename_in_archive=filename_in_archive)

    war_and_peace.print_stat()

# Зачет!
