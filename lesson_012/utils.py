import os
import time
from collections import OrderedDict


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


def print_report(tickers_dict):
    zero_tickers = {}
    tickers = {}

    for ticker, volatility in tickers_dict.items():
        if volatility == 0:
            zero_tickers[ticker] = volatility
        else:
            tickers[ticker] = volatility

    ordered_tickers = OrderedDict(sorted(tickers.items(), key=lambda x: x[1], reverse=True))
    tickers_list = list(ordered_tickers.keys())

    print('Максимальная волатильность:')
    for secid in tickers_list[:3]:
        print(f'\t{secid} - {ordered_tickers[secid]:2.2f} %')

    print('Минимальная волатильность:')
    for secid in tickers_list[-3:]:
        print(f'\t{secid} - {ordered_tickers[secid]:2.2f} %')

    print('Нулевая волатильность:')
    print('\t', ', '.join(sorted(zero_tickers.keys())), sep='')


def get_next_file(file_path):
    for dirpath, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            file_name = os.path.join(dirpath, filename)
            yield file_name
