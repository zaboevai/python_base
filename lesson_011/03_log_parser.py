# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

import os


class LogParser:

    def __init__(self, file_in=None, file_out=None):
        self.file_in = file_in
        self.file_out = file_out
        self.log_stat = {}

        if not self.file_out:
            self.file_out = self.file_in + '.nok'

        if os.path.exists(self.file_out):
            os.remove(self.file_out)

    def line_parsing(self, line=None):
        date, time, res = line.split(' ')
        res = res.replace('\n', '')
        dt = date + ' ' + time[:5] + time[-1:]
        return dt, res

    def parse(self):
        self.log_stat = {}
        with open(self.file_in, 'r') as file:
            for line in file:
                dt, res = self.line_parsing(line)

                if res == 'NOK':
                    if dt not in self.log_stat.keys():
                        for k, v in self.log_stat.items():
                            yield k, v
                        self.log_stat = {}
                    self.log_stat[dt] = self.log_stat.setdefault(dt, 0) + 1

    def write_result(self):
        with open(file=self.file_out, mode='a', encoding='utf8') as file:
            for date, cnt in self.parse():
                file.write(f'{date} {cnt} \n')


if __name__ == '__main__':

    log_file_in = 'events.txt'
    log_file = LogParser(file_in=log_file_in)

    grouped_events = log_file.parse()
    for group_time, event_count in grouped_events:
        print(f'[{group_time}] {event_count}')

    log_file.write_result()
