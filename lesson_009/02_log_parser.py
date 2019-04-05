# -*- coding: utf-8 -*-

import os

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
        self.log_stat = {}
        if not self.file_out:
            self.file_out = self.file_in + '.nok'

    def line_parsing(self, line=None):
        date, time, res = line.split(' ')
        # TODO Между арфметическими операциями всегда должны присутствовать пробелы
        dt = date+' '+time[:5]+time[-1:]
        return dt, res

    def parse(self):
        with open(self.file_in, 'r') as file:
            for line in file:
                dt, res = self.line_parsing(line)
                # TODO Лучше использовать экранированные последовательности,
                # TODO (\n). Не все могут помнить коды символов, но все знают,
                # TODO что значит \n
                res = res.replace(chr(10), '')
                if res == 'NOK':
                    if dt in self.log_stat.keys():
                        # TODO Необходимо использовать setdefault, чтобы упросить код
                        self.log_stat[dt] += 1
                    else:
                        if self.log_stat:
                            self.write()
                            self.log_stat = {}
                        self.log_stat[dt] = 1

    def write(self):
        with open(file=self.file_out, mode='a', encoding='utf8') as file:
            for date, cnt in self.log_stat.items():
                # TODO Лучше будет использовать f строки, тогда будет нагляднее
                file.write(date + ' ' + str(cnt) + '\n')


if __name__ == '__main__':
    log = LogParser('events.txt')
    log.parse()
