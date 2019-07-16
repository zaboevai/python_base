# -*- coding: utf-8 -*-

# Логирование
#
# Всегда полезно знать что происходило с нашей программой в процессе выполнения
# Это осуществляется с помощью стандартной библиотеки логирования

# Существует 5 уровней логирования

# DEBUG 	Детальная информация, интересная только при отладке
#
# INFO 	    Подтверждение, что все работает как надо
#
# WARNING 	Индикация того, что что-то пошло не так, и возможны проблемы в будущем
#           (заканчивается место на диске, етс)
#           Программа продолжает работать как надо.
#
# ERROR 	Относительно серьезная проблема, программа не смогла выполнить некоторый функционал.
#
# CRITICAL 	Реально серьезная проблема, программа не может работать дальше.
#
# Уровень WARNING стоит по умолчанию.

import logging


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        logging.debug(f'number {number}')
        for prime in prime_numbers:
            if number % prime == 0:
                logging.debug(f'делится на {prime}')
                break
        else:
            logging.debug(f'найдено новое простое {number}')
            prime_numbers.append(number)
            yield number


logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)

for prime in prime_numbers_generator(100):
    logging.info(f'Простое из генераторв {prime}')

# Легко перенаправить вывод в файл
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.FileHandler('primes.log', 'w', 'utf-8')],
)

for prime in prime_numbers_generator(100):
    logging.info(f'Простое из генераторв {prime}')

# Так же легко сделать логирование в нескольких модулях

from primes import prime_numbers_generator

logging.basicConfig(level=logging.DEBUG, filename='primes.log')

for prime in prime_numbers_generator(100):
    logging.info(f'Простое из генераторв {prime}')


# Для логирования ошибок есть специальный метод .exception()
# Он выводит (вдобавок к сообщению) само исключение и место, где оно произошло

def perky(param):
    return param / 0


logging.basicConfig(filename='errors.log', level=logging.INFO)

number = 42
try:
    logging.info('Посмотрим как у него получится...')
    perky(number)
    logging.info('Он смог!')
except Exception:
    logging.exception(f'Дерзкий не справился c {number}')

# В больших программах практически всегда необходимо разделять сообщения в логах
# по некоторому признаку - типы сообщений, места возникновения, используемый модуль, етс
# Для этого можно создавать обьекты логирования и конфигурировать их

log = logging.getLogger('perky')
log.setLevel(logging.INFO)
fh = logging.FileHandler("perky.log", 'w', 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# все возможные аттрибуты см https://docs.python.org/3.5/library/logging.html#logrecord-attributes
fh.setFormatter(formatter)
log.addHandler(fh)

number = 42
try:
    log.info('Посмотрим как у него получится...')
    perky(number)
    log.info('Он смог!')
except Exception:
    log.exception(f'Дерзкий не справился c {number}')


# посмотрим как это работает в проекте
from primes_package.main import print_primes

print_primes(30)


# Можно и нужно создавать общие конфигурации для всех логгеров

import logging
import logging.config

log_config = {
    "version": 1,
    "formatters": {
        "my_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "my_formatter",
            "filename": "perky.log"
        },
    },
    "loggers": {
        "perky": {
            "handlers": ["file_handler"],
            "level": "INFO",
        }
    },
}


logging.config.dictConfig(log_config)
log = logging.getLogger('perky')


def perky(param):
    return param / 0


number = 42
try:
    log.info('Посмотрим как у него получится...')
    perky(number)
    log.info('Он смог!')
except Exception:
    log.exception(f'Дерзкий не справился c {number}')

# На один логгер можно повесить несклько хэндлеров,
# полный список см https://docs.python.org/3.5/howto/logging.html#useful-handlers


# Подводя итог.
# Средства логирования в пайтона весьма мощные и повсеместно используются в промышленных проектах
