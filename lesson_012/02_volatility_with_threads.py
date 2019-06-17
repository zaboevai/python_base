# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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

import csv
import os
import time
from collections import OrderedDict
from utils import time_track
from threading import Thread

trade_files = './trades'


class TickerVolatility(Thread):
    tickers = {}
    zero_volatility = []
    completed_files = []

    def __init__(self, file_path, min_str_cnt=3, max_str_cnt=3, print_zero_tickers=True):
        super().__init__()
        self.min_str_cnt = min_str_cnt
        self.max_str_cnt = max_str_cnt
        self.print_zero_tickers = print_zero_tickers
        self.file_path = file_path

    def get_info_from_trades_files(self):
        for dirpath, dirnames, filenames in os.walk(self.file_path):
            for filename in filenames:
                file_name = os.path.join(dirpath, filename)
                if file_name in TickerVolatility.completed_files:
                    continue
                else:
                    TickerVolatility.completed_files.append(file_name)
                    with open(file=file_name, mode='r', encoding='utf8') as csv_file:
                        csv_dict = csv.DictReader(csv_file, delimiter=',')
                        prices = []

                        for line in csv_dict:
                            ticker = line['SECID']
                            prices.append(float(line['PRICE']))

                    yield ticker, prices

    def calculate_volatility(self):
        for ticker, prices in self.get_info_from_trades_files():
            if not TickerVolatility.tickers.get(ticker):
                max_price, min_price = max(prices), min(prices)
                average_price = (max_price + min_price) / 2
                volatility = ((max_price - min_price) / average_price) * 100

                if volatility == 0:
                    if ticker not in TickerVolatility.zero_volatility:
                        TickerVolatility.zero_volatility.append(ticker)
                else:
                    TickerVolatility.tickers[ticker] = volatility

        TickerVolatility.tickers = OrderedDict(sorted(TickerVolatility.tickers.items(), key=lambda x: x[1], reverse=True))
        TickerVolatility.zero_volatility = sorted(TickerVolatility.zero_volatility)

    def print_max_volatility(self):
        if self.max_str_cnt:
            i = 0
            print('Максимальная волатильность:')

            for secid, volatility in TickerVolatility.tickers.items():
                i += 1
                if i <= self.max_str_cnt:
                    print(f'\t{secid} - {volatility} %')

    def print_min_volatility(self):
        if self.min_str_cnt:
            i = 0
            print('Минимальная волатильность:')
            for secid, volatility in TickerVolatility.tickers.items():
                i += 1
                if i >= len(TickerVolatility.tickers.items()) - self.min_str_cnt + 1:
                    print(f'\t{secid} - {volatility} %')

    def print_zero_volatility(self):
        if self.print_zero_tickers:
            print('Нулевая волатильность:')
            print(f'\t{TickerVolatility.zero_volatility}')

    def run(self):
        self.calculate_volatility()

@time_track
def byThreads(threads_cnt):

    threads = [TickerVolatility(file_path=trade_files) for i in range(threads_cnt)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    thread.print_max_volatility()
    thread.print_min_volatility()
    thread.print_zero_volatility()

    thread.tickers.clear()
    thread.completed_files.clear()


@time_track
def byThread():
    report = TickerVolatility(file_path=trade_files)
    report.run()

    report.print_max_volatility()
    report.print_min_volatility()
    report.print_zero_volatility()

    report.tickers.clear()
    report.completed_files.clear()



if __name__ == '__main__':
    byThread()
    byThreads(threads_cnt=5)
