# -*- coding: utf-8 -*-

import zipfile, os, datetime

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата


class LogParser:

    def __init__(self, file_inc=None, file_out=None):
        self.file_inc = file_inc
        if file_out:
            self.file_out = file_out
        else:
            self.file_out = file_inc + '.analyzed'
        print(self.file_out)
        self.stat = {}


    def line_parsing(self, line=None):
        date, res = line.split(']')
        date = date.replace('[', '')
        date, time = date.split(' ')
        dt = []
        dt.extend(date.split('-'))
        dt.extend(time.split(':'))
        sec = dt[-1].split('.')
        dt.pop()
        dt.extend(sec)
        dt = tuple(map(int, dt))
        dt = datetime.datetime(*dt)
        return dt, res

    def get_stat(self):
        for line in self.file_inc:
            dt, res = self.line_parsing(line)
            if dt.year in self.stat
if __name__ == '__main__':
    test = LogParser('lesson_009/events.txt')