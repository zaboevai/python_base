# -*- coding: utf-8 -*-
import io
from pprint import pprint

# Файл - это упорядоченная совокупность байтов, которая хранится на диске
# и/или занимает отдельную область внешней памяти


# Файл можно представить как ленту на шоколадной фабрике, только вместо конфет - байты.
# Лента имеет начало и конец, каждая конфета пронумерована.
# И мы можем ходить вдоль ленты - брать или класть конфеты.
# Если файл открыт только для чтения (посмотреть на конфеты)
# - то при открытии файла стоим вначале ленты, на 0 месте,
# А при самом чтении - сдвигаемся вдоль ленты на количество прочитанных конфет.
# file.tell() говорит нам текущую позицию

file_name = 'byron.txt'
# file_name = 'pushkin.txt'
file = open(file_name, mode='r', encoding='utf8')
print(file.tell())

print('читаем 100 символов')
file_content = file.read(100)  # в символах
print(file_content)
print(file.tell())  # в байтах!

print('читаем остальное')
file_content = file.read()
print(file_content)
print(file.tell())  # в байтах!

file.close()

# Позицию чтения можно менять - переходить в начала или в коннец
file_name = 'pushkin.txt'
file = open(file_name, mode='r', encoding='utf8')

file_content = file.read(100)  # в символах
print(file_content)

new_position = file.seek(0, io.SEEK_SET)
# io.SEEK_SET - начало файла
# io.SEEK_CUR - текущая позиция
# io.SEEK_END - конец файла

file_content = file.read(100)  # в символах
print(file_content)

file.close()
# аналогично для записи


# Свойства и функции у обьекта файл
pprint(file.name)
pprint(file.mode)
pprint(file.encoding)
pprint(file.closed)

pprint(file.readable())  # файл можно читать
pprint(file.writable())  # файл можно писать
pprint(file.seekable())  # файл поддерживает произвольный доступ

pprint(file.truncate(size=None))
pprint(file.flush())  # обычно файл буферезирован, флаш записвыает весь буфер на диск

# Файлы по сути являются потоками байтов - streams. https://docs.python.org/3/library/io.html


