# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.

import csv
import os
from collections import OrderedDict
from utils import time_track

# TODO Для того, чтобы скрипт был более гибкий лучше реализовать динамические
# TODO вычисление пути до папки trades (при вычислении необходимо опираться на
# TODO предположение, что папка будет лежать рядом с запускаемым скриптом)
trade_files = '/home/andrey/PycharmProjects/python_base/lesson_012/trades'


class TickerVolatility:

    def __init__(self, file_path, min_str_cnt, max_str_cnt, print_zero_tickers=False):
        self.min_str_cnt = min_str_cnt
        self.max_str_cnt = max_str_cnt
        self.print_zero_tickers = print_zero_tickers
        # TODO Необходимо добавить проверку того, что путь существует и если
        # TODO он не существует, то выбрасывать исключение
        self.file_path = file_path
        # TODO В атрибуты экземпляра класса стоит выносить только то, что
        # TODO используется в нескольких методах класса или то, что
        # TODO характеризует конкретный экземпляр класса (на пример у класса
        # TODO Person, логично сделать name атрибутом экземляра класса).
        # TODO В данном случае лучше объявить переменные ticker, prices и
        # TODO tickers просто внутри функции _get_file_from_file_list, потому
        # TODO  что доступ к атрибутам класса дорогой.
        self.ticker, self.prices = set(), []
        self.tickers = {}
        self.ordered_tickers = {}
        self.zero_volatility = []

    def _get_file_from_file_list(self):
        for dirpath, dirnames, filenames in os.walk(self.file_path):
            for filename in filenames:
                file_name = os.path.join(dirpath, filename)
                yield file_name

    def calculate_volatility(self):

        for file_name in self._get_file_from_file_list():
            with open(file=file_name, mode='r', encoding='utf8') as csv_file:
                csv_dict = csv.DictReader(csv_file, delimiter=',')
                self.prices = []

                for line in csv_dict:
                    self.ticker = line['SECID']
                    self.prices.append(float(line['PRICE']))

                max_price, min_price = max(self.prices), min(self.prices)
                average_price = (max_price + min_price) / 2
                volatility = ((max_price - min_price) / average_price) * 100

            self.tickers[self.ticker] = volatility

        self.ordered_tickers = OrderedDict(sorted(self.tickers.items(), key=lambda x: x[1], reverse=True))
        self.zero_volatility = []

        # TODO Лучше дать переменным цикла названия, которые будут отражать их
        # TODO назначение
        for k, v in list(self.ordered_tickers.items()):
            if v == 0:
                self.zero_volatility.append(k)
                del self.ordered_tickers[k]

    def print_max_volatility(self):
        i = 0
        for secid, volatility in self.ordered_tickers.items():
            i += 1
            if i <= self.max_str_cnt:
                print(f'\t{secid} - {volatility} %')

    def print_min_volatility(self):
        i = 0
        for secid, volatility in self.ordered_tickers.items():
            i += 1
            if i >= len(self.ordered_tickers.items()) - self.min_str_cnt + 1:
                print(f'\t{secid} - {volatility} %')

    def print_zero_volatility(self):
        if self.print_zero_tickers:
            print(f'\t{sorted(self.zero_volatility)}')

    @time_track
    def run(self):

        self.calculate_volatility()

        if self.max_str_cnt:
            print('Максимальная волатильность:')
            self.print_max_volatility()

        if self.min_str_cnt:
            print('Минимальная волатильность:')
            self.print_min_volatility()

        if self.print_zero_tickers:
            print('Нулевая волатильность:')
            self.print_zero_volatility()


if __name__ == '__main__':
    #  Лучше форматировать создание класса вот так
    tickers_report = TickerVolatility(
        file_path=trade_files, min_str_cnt=3, max_str_cnt=3,
        print_zero_tickers=True
    )
    tickers_report.run()
