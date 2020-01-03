# -*- coding: utf-8 -*-

#
# 15.01 Decimal
#

# Числа с плавающей точкой (float) имеют точность хранения в памяти

# Ограничения точности, которые они имеют
# могут приводить к очень странным для нас выводам.
# Например:

print(4.31 == 4.3099999999999996)  # True!

# Для человека результат подобного сравнения очевиден. Но не для машины,
# Оба числа, в битовой записи идентичны, что и говорит питону об их равенстве.

print(4.31.hex())
print(4.3099999999999996.hex())

# Как можно столкнуться с такой записью:

print(0.3 + 0.3 + 0.3 + 0.1)  # 0.9999999999999999

# Иногда это не проблема - точности хватает

print(round(0.3 + 0.3 + 0.3 + 0.1, 10))

# но есть области человеческой деятельности, где накопление ошибки округления числа очень даже критично.
# Одно из самых важных, не считая космоса - это бухгалтерия. Счета и накладные ведутся с точностью до копеек
# и счет на 99.999999999 рублей никто оплачивать не будет. Что же делать?

# Использовать тип данных Decimal - в нем можно контролировать нужную точность и способы округления.

from decimal import *

print(Decimal('0.3') + Decimal('0.3') + Decimal('0.3') + Decimal('0.1'))

# Этот тип данных хранит заранее заданное количество знаков после запятой
# и все вычисления делает ТОЧНО, без округлений
# В Decimal степень точности (до какого знака округлять число) можно изменять:

getcontext().prec = 50

# Пример:
# Бухгалтер Энди Дюфрейн, вернувшись к работе после долгого перерыва, обнаружил,
# что часть его рутинной работы можно отдать компьютеру.
# Одним из таких дел был расчёт налога на прибыль, которую Энди забрал, закрыв счета Ренделла Стивенса.
# Помогите же Энди посчитать сумму налога к выплате, чтобы его не посадили за финансовые махинации.

Andys_money_float = []
Andys_money_decimal = []

with open('external_data/Randalls_money.txt', 'r') as Randalls_money:
    for line in Randalls_money:
        Andys_money_float.append(float(line))
        Andys_money_decimal.append(Decimal(line))

exchange_rate_rubles_in_dollars = 1.2063   # курс 1972 года
profit_tax_rate = 0.13


def tax_calculation(income_in_dollars, exchange_rate, tax_rate):
    return tax_rate * exchange_rate * sum(income_in_dollars)


# Проблема №1 - Недостаточная точность при сведении баланса или подсчете налогов:

profit_tax_amount = tax_calculation(Andys_money_float, exchange_rate_rubles_in_dollars, profit_tax_rate)
print(f'Итоговая сумма налога {profit_tax_amount}')

d_profit_tax_amount = tax_calculation(Andys_money_decimal, Decimal(exchange_rate_rubles_in_dollars), Decimal(profit_tax_rate))
print(f'Ещё одная сумма налога {d_profit_tax_amount}')

# Зачастую разница незаметна, но она есть:
print(f'Разница в одном таком расчёте: {d_profit_tax_amount - Decimal(profit_tax_amount)}')

# Итог №1:
# Даже при относительно простых операциях с относительно небольшим количеством товаров,
# Появляется и копится разница в расчётах.
# Decimal позволяет контролировать точность расчета.

# Проблема №2 - Ценообразование и округления:

Andys_price_list_float = []
Andys_price_list_decimal = []
with open('external_data/Andys_goods.txt', 'r') as Andys_goods:
    for price in Andys_goods:
        Andys_price_list_float.append(float(price))
        Andys_price_list_decimal.append(Decimal(price))

print(f'Цены в магазинах не могут выглядеть так {Andys_price_list_float[:5]}')
rounded_list_for_pricing = []
for price in Andys_price_list_float:
    rounded_list_for_pricing.append(round(price, 2))
revenue_for_the_day = sum(rounded_list_for_pricing)
print(f'Но даже если цены выглядят ровно {rounded_list_for_pricing[:5]}')
print(f'Могут возникать странные остатки при их суммировании {revenue_for_the_day}')

decimal_rounded_list_for_pricing = []
for price in Andys_price_list_decimal:
    decimal_rounded_list_for_pricing.append(price.quantize(Decimal('1.00')))
decimal_revenue_for_the_day = sum(decimal_rounded_list_for_pricing)
print(f'Получаем округленные цены {decimal_rounded_list_for_pricing[:5]}')
print(f'Считаем дневную выручку {decimal_revenue_for_the_day}')
print(f'Равны ли значения? Ответ - {revenue_for_the_day == decimal_revenue_for_the_day}')  # False

# Итог №2:
# Работа с float требует постоянного и явного округления,
# даже при сложении чисел с одним знаком после запятой.
# Decimal позволяет один раз указать тип округления,
# автоматически применяя его ко всем остальным операциям.


# Насколько же сильно подобные проблемы округления могут повлиять на конечный результат?
#
# Для наглядного ответа на этот вопрос придумана формула, которая является эквивалентом
# рекуррентного соотношения Мюллера, задающего последовательность чисел:

def mullers_formula(z, y):
    return 108 - (815 - 1500/z) / y


# Сперва с помощью типа 'float'
float0 = 4.0
float1 = 4.25
# При таких начальных условиях, ряд должен сходится к 5,
# проверим это, вычислив 30-ый член ряда.

for _ in range(2, 31):
    float2 = mullers_formula(float0, float1)
    float0, float1 = float1, float2
print(f'(float) 30-ый член последовательности равен {float2}')

# А теперь попробуем использовать Decimal:
getcontext().prec = 35
dec0 = Decimal(4.0)
dec1 = Decimal(4.25)
for _ in range(2, 31):
    dec2 = mullers_formula(dec0, dec1)
    dec0, dec1 = dec1, dec2
print(f'(Decimal) 30-ый член последовательности равен {dec2}')

# Разница не так уж и велика. Но что будет, если мы увеличим точность вычислений?
# Скажем до 50 знаков:
getcontext().prec = 50
dec0_50 = Decimal(4.0)
dec1_50 = Decimal(4.25)
for _ in range(2, 31):
    dec2_50 = mullers_formula(dec0_50, dec1_50)
    dec0_50, dec1_50 = dec1_50, dec2_50
print(f'Теперь 30-ый член последовательности равен {dec2_50}')
print(f'Разница между первый и вторым вычислениями составила {dec2 - dec2_50}')


# Стандартное округление round() и округление quantize() в Decimal:

# Как работает round()?
# В пайтоне 2 round() подчинялся простым законам арифметического округления.
# Но в пайтоне 3 round() переделали и он стал работать по методу "банковского" округления.

# в чём проблема с простым арифметическим округлением?
# В большую сторону округляются 5,6,7,8,9
# В меньшую 1,2,3,4
# Выходит, что больше чисел округляется вверх.

# Изменения в "банковском" округлении касаются только случая с числами с 5 на конце.
# Банковский метод округляет такие числа до ближайших четных.
print(f'Округление 2.5 банковским методом - {round(2.5)}')
# Арифметическим метод в этом случае округлил бы число до 3
print(f'Округление 3.5 банковским методом - {round(3.5)}')
# Здесь результат совпадает с арифметическим методом - 4

# Зачем же нам тогда нужен Decimal и quantize()?
# Дело в том, что "банковский" метод удовлетворительно справляется со случайными числами,
# уменьшая погрешность арифметического метода почти вдвое.
# Но! В бухгалтерии одни числа могут встречаться чаще, чем другие,
# что требует более сложных и современных методов округления.

# Эта проблема рассматривается в мировом стандарте IEEE 754.
# В ней описаны пять способов округления.
# И все эти способы реализованы в Decimal:
# round-down - усечение по направлению к нулю
# round-half-up - арифметическое округление
# round-half-even - банковское округление
# round-ceiling - округление к плюс-бесконечности
# round-floor - округление к минус-бесконечности

# Примеры:
number = Decimal("10.025")
print(f'Банковский метод - {number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)}')
print(f'Арифметический метод - {number.quantize(Decimal("1.00"), ROUND_HALF_UP)}')
print(f'Метод "обрезания" чисел без округления {number.quantize(Decimal("1.00"), ROUND_FLOOR)}')

# Итог:
# набор различных методов округления в Decimals позволяет подобрать решение
# возникающих проблем с погрешностями округления, что делает метод quantize()
# более универсальным, чем стандартный round().
