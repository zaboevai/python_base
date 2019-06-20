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
from collections import OrderedDict
from utils import time_track
from threading import Thread

trade_files = './trades'


class TickerVolatility(Thread):
    completed_files = []
    isReportPrepare = False
    tickers = {}
    zero_volatility = []
    THREADS_COUNT = 5

    def __init__(self, file_path, min_str_cnt, max_str_cnt, print_zero_tickers=False):
        super().__init__()
        self.min_str_cnt = min_str_cnt
        self.max_str_cnt = max_str_cnt
        self.print_zero_tickers = print_zero_tickers
        self.threads = []
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            raise FileExistsError('Каталог с файлами отсутствует')

    def create_threads(self):
        self.threads = [TickerVolatility(
            file_path=trade_files,
            min_str_cnt=self.min_str_cnt,
            max_str_cnt=self.max_str_cnt,
            print_zero_tickers=True
        ) for thread in range(0, TickerVolatility.THREADS_COUNT)]

    def run_report(self):

        self.create_threads()

        for thread in self.threads:
            thread.start()
            # print(thread)

        for thread in self.threads:
            thread.join()

        #self.threads[0].print_volatility()

    def get_tickers_info_from_files(self):
        ticker, prices = set(), []

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
        for ticker, prices in self.get_tickers_info_from_files():
            max_price, min_price = max(prices), min(prices)
            average_price = (max_price + min_price) / 2
            volatility = ((max_price - min_price) / average_price) * 100

            if volatility == 0:
                TickerVolatility.zero_volatility.append(ticker)
            else:
                TickerVolatility.tickers[ticker] = volatility

    def print_volatility(self):

        ordered_tickers = OrderedDict(sorted(TickerVolatility.tickers.items(), key=lambda x: x[1], reverse=True))
        TickerVolatility.isReportPrepare = True
        ticker = list(ordered_tickers.keys())

        if self.max_str_cnt:
            print('Максимальная волатильность:')
            for secid in ticker[:self.max_str_cnt]:
                print(f'\t{secid} - {ordered_tickers[secid]:2.2f} %')

        if self.min_str_cnt:
            print('Минимальная волатильность:')
            for secid in ticker[-self.min_str_cnt:]:
                print(f'\t{secid} - {ordered_tickers[secid]:2.2f} %')

        if self.print_zero_tickers:
            print('Нулевая волатильность:')
            print(f'\t{sorted(TickerVolatility.zero_volatility)}')

    def run(self):
        if not TickerVolatility.isReportPrepare:
            self.calculate_volatility()


@time_track
def main():
    try:
        report = TickerVolatility(
            file_path=trade_files,
            min_str_cnt=3,
            max_str_cnt=3,
            print_zero_tickers=True
        )

        report.run_report()
        report.print_volatility()

    except FileExistsError as exc:
        print(f'Ошибка! {exc}.')


if __name__ == '__main__':
    main()
