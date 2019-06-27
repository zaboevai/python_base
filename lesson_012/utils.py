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


def print_report(tickers, zero_volatility_tickers):

    zero_volatility_tickers = sorted(zero_volatility_tickers)
    ordered_tickers = OrderedDict(sorted(tickers.items(), key=lambda x: x[1], reverse=True))
    tickers_list = list(ordered_tickers.keys())


    print('Максимальная волатильность:')
    for secid in tickers_list[:3]:
        print(f'\t{secid} - {ordered_tickers[secid]:2.2f} %')

    print('Минимальная волатильность:')
    for secid in tickers_list[-3:]:
        print(f'\t{secid} - {ordered_tickers[secid]:2.2f} %')

    print('Нулевая волатильность:')
    print('\t', ', '.join(zero_volatility_tickers), sep='')
