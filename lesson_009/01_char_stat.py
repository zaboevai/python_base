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
src_dir = './python_snippets'
unzip_src_dir = os.path.join(src_dir, 'unzip_files')
file_name = 'voyna-i-mir.txt'

for dir_path, dir_names, file_names in os.walk(src_dir):
    for file_name in file_names:
        if zipfile.is_zipfile(os.path.join(dir_path, file_name)):
            src_file = os.path.join(dir_path, file_name)
            print(src_file)
            zip_file = zipfile.ZipFile(src_file)
            zip_file.extractall(unzip_src_dir)

symbols = {}

a, b = 'буква', 'кол-во'
c = None
print(f'')
print('+',  f'{chr(45):-^9}',  '+',  f'{chr(45):-^10}',  '+', sep='')
print('|',  f'{a: ^9}'      ,  '|',  f'{b: ^10}'      ,  '|', sep='')
print('+',  f'{chr(45):-^9}',  '+',  f'{chr(45):-^10}',  '+', sep='')

with open(os.path.join(unzip_src_dir, file_name), mode='r', encoding='CP1251') as file: #
    for line in file:
        for char in line:
            if ord(char) in symbols:
                symbols[ord(char)] += 1
            else:
                symbols[ord(char)] = 1
    # print(sorted(symbols.items()))
    # symbols['перенос'] = symbols.pop(10)
    # TODO подумать как правильно выводить chr(10)
    for char, cnt in sorted(symbols.items()):

        print(f'|{chr(char): ^9}', '|', f'{cnt: ^10}|', sep='')
        # break
print(f'+{chr(45):-^9}', '+', f'{chr(45):-^10}+', sep='')
# print(os.path.abspath('./'))
