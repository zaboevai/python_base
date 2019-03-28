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
            self.file_out = file_inc
        print(self.file_out)
        self.stat = {}

    def line_parsing(self, line=None):
        date, res = line.split('] ')
        date = date.replace('[', '')
        date, time = date.split(' ')
        dt = []
        dt.extend(date.split('-'))
        dt.extend(time.split(':'))
        dt.pop()
        dt = tuple(map(int, dt))
        dt = datetime.datetime(*dt)
        return dt, res

    def get_stat(self):
        with open(self.file_inc, 'r') as file:
            for line in file:
                dt, res = map(str, self.line_parsing(line))
                res = res.replace(chr(10), '')
                if res == 'NOK':
                    if dt in self.stat:
                       self.stat[dt] += 1
                    else:
                       self.stat[dt] = 1

        return self.stat

    def print_stat(self):
        for date, cnt in self.stat.items():
            print(date, '  ', cnt)

    def write_stat(self, file_out=None):
        if not file_out:
            self.file_out = file_out
        # TODO доделать запись результата в файл
        with open(file=self.file_out, mode='w+') as file:
            for date, cnt in self.stat.items():
                print(date, '  ', cnt)
                file.write(date+' '+cnt)


if __name__ == '__main__':
    test = LogParser('events.txt', 'res.txt')
    test.get_stat()
    test.print_stat()
    test.write_stat()