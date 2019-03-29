# -*- coding: utf-8 -*-

import datetime

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

    def __init__(self, file_in=None, file_out=None):
        self.file_in = file_in
        self.file_out = file_out
        self.nok_stat = {}

    def _line_parsing(self, line=None):
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

    def get(self):
        with open(self.file_in, 'r') as file:
            for line in file:
                dt, res = map(str, self._line_parsing(line))
                res = res.replace(chr(10), '')
                if res == 'NOK':
                    if dt in self.nok_stat:
                        self.nok_stat[dt] += 1
                    else:
                        self.nok_stat[dt] = 1

        return self.nok_stat

    def print(self):
        for date, cnt in self.nok_stat.items():
            print(date, '  ', cnt)

    def write(self):
        if not self.nok_stat:
            self.get()

        if not self.file_out:
            self.file_out = self.file_in + '.nok'

        with open(file=self.file_out, mode='w', encoding='utf8') as file:
            for date, cnt in self.nok_stat.items():
                file.write(date + ' ' + str(cnt) + '\n')


if __name__ == '__main__':
    parsed_log = LogParser('events.txt')
    parsed_log.write()
