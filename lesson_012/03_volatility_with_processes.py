# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/02_volatility_with_threads.py !!!

# TODO тут ваш код в многопроцессном стиле


import csv
import os
from multiprocessing import Process
from queue import Queue, Empty

from utils import time_track, print_report, get_next_file


class TickerVolatility(Process):

    def __init__(self, file_path, tickers_queue):
        super().__init__()

        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            raise FileExistsError('Каталог с файлами отсутствует')

        self.tickers_queue = tickers_queue

    def get_tickers_info_from_file(self):
        prices = []
        ticker = None

        with open(file=self.file_path, mode='r', encoding='utf8') as csv_file:
            csv_dict = csv.DictReader(csv_file, delimiter=',')
            for line in csv_dict:
                ticker = line['SECID']
                prices.append(float(line['PRICE']))

        return ticker, prices

    def run(self):
        try:
            self.calculate_volatility()
        except Exception as exc:
            print(f'Error - {self.name} - {exc}')

    def calculate_volatility(self):

        ticker, prices = self.get_tickers_info_from_file()
        max_price, min_price = max(prices), min(prices)
        average_price = (max_price + min_price) / 2
        volatility = ((max_price - min_price) / average_price) * 100

        self.tickers_queue.put((ticker, volatility))


@ time_track
def main(tickers_path):
    threads = []
    tickers = {}
    q = Queue()

    for fname in get_next_file(tickers_path):
        threads.append(TickerVolatility(file_path=fname,
                                        tickers_queue=q)
                       )

    [thread.start() for thread in threads]

        # print(thread.tickers_queue.get())

    while True:
        try:
            print(q.qsize())
            ticker, volatility = q.get(timeout=1)
            tickers[ticker] = volatility
        except Empty as exc:
            if not any(thread.is_alive() for thread in threads):
                break
            print(exc)

    print(tickers)
    [thread.join() for thread in threads]

    print_report(tickers)


if __name__ == '__main__':
    TRADE_FILES = './trades'

    main(tickers_path=TRADE_FILES)
