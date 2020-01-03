# -*- coding: utf-8 -*-

#
# 15.02 Date and time
#

import time

###
# Модуль time

# Время в компьютере хранится как сумма секунд, прошедших с "начала эпохи"
# Проверить начало эпохи, заданное для вашей машины можно функцией из встроенного модуля time

print(time.gmtime(0))
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0,
#                  tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

# Зачастую результат будет одним: 1 января 1970 года 00:00
# Эту дату называют "Unix-эпохой" и она связана с написанием первой официальной версии операционной системы UNIX
# https://clck.ru/Gg6eY

# Получить сколько секунд прошло с начала эпохи можно с помощью функции
print(time.time())  # тип 'float'

# В модуле time есть несколько удобных методов
# Один из них -  поспать ХХХ секунд
print(time.sleep(3))
# программа спала 3 секунды и ничего не делала.

# В случае, если вам надо измерить время работы части кода, можно воспользоваться методом monotonic()
# Его главной особенностью является то, что он не может идти назад,
# если например ОС обновила через интернет свои часы для синхронизации.

start = time.monotonic()
huge_number = 2 ** 100000000
elapsed = time.monotonic() - start
print(f'потрачено {elapsed} секунд')


###
# Модуль datetime

import datetime

# Один из них класс date для манипуляций с датами.

# Пример:
# В недалеком будущем нас захватил искусственный интеллект, всем знакомый SkyNet
# И чтобы получить от нас хоть какую-то пользу, он пытается выяснить дату рождения Сары Коннор.

sarah_birthday = datetime.date(year=1965, month=10, day=28)
print(f'Сара Коннор родилась {sarah_birthday}')

# данный класс содержит в себе информацию о дате, без информации о времени.
# вспоминая модуль time, сразу можно отметить удобство, с которым задаётся нужная дата
# при желании можно воспользоваться и текущей датой

first_day_of_the_rest_of_your_life = datetime.date.today()

# обьект даты позволяет обращаться к отдельным своим составляющим

print(sarah_birthday.year)   # 1965 - тип 'int'
print(sarah_birthday.month)  # 10
print(sarah_birthday.day)    # 28
print(sarah_birthday.weekday())

# класс для работ только со временем - datetime.time

lunch_time = datetime.time(hour=12, minute=15, second=30, microsecond=5005)
print(f'Время обеда {lunch_time}')

# в конструкторе класса не обязательно указывать все поля

monday_lunch_time = datetime.time(hour=12, minute=15, second=30)
tuesday_lunch_time = datetime.time(hour=12, minute=15)
wednesday_lunch_time = datetime.time(hour=12)
print(f'Время обеда: понедельник {monday_lunch_time}, вторник {tuesday_lunch_time}, среда {wednesday_lunch_time}')

# Для обращения к отдельным полям можно использовать атрибуты:

print(lunch_time.hour)  # 12
print(lunch_time.minute)  # 10
print(lunch_time.second)  # 30
print(lunch_time.microsecond)  # 5005

# А что если нам нужно учитывать как дату, так и время? Для этого есть класс datetime.datetime

terminator_time_travel = datetime.datetime(year=1984, month=5, day=12, hour=1,
                                           minute=52, second=00, microsecond=1001)

print(f'Терминатор впервые появился в будущем в {terminator_time_travel}')

# как и в модуле time, здесь можно не указывать полностью данные о времени
rise_of_skynet_datetime = datetime.datetime(year=1997, month=8, day=29, hour=10, minute=14)
print(f'СкайНет начал войну {rise_of_skynet_datetime}')

# минимум нужно указать три параметра - год, месяц и день
# print(datetime.datetime(1997, 8)) выдаст ошибку
# TypeError: function missing required argument 'day' (pos 3)

# к отдельным полям объекта также можно обращаться используя методы из классов date и time
print(rise_of_skynet_datetime.year)  # 1997 - тип 'int'
print(rise_of_skynet_datetime.hour)  # 10 - тоже int

# для работы с текущим моментом можно использовать метод

print(datetime.datetime.now())  # 2019-06-15 13:56:00.020829

###
# Для того, чтобы отобразить время в другом формате существует метод strftime()

# Правила форматирования задаются с помощью строки, содержащей специальные символы.
#
# Они выделены знаком '%'.
# Вместо них, в зависимости от буквы, будет выведена та, или иная часть даты
# Например:

print(f'День, с которого всё началось {terminator_time_travel.strftime("%d.%m.%Y !")}')

# %d заменяется на 15 - номер дня в месяце
# %m на 06            - номер самого месяца
# %Y на 2019          - год
# Символы, не выделенные процентом (в данном случае '.') остаются без изменений
# Вывести мы можем только ту информацию, которая есть в объекте, к которому мы применяем этот метод.

print(f'И началось это всё в {terminator_time_travel.strftime("%H:%M:%S")}')

# %H %M %S - количество часов ( в 24 часовом формате), количество минут и количество секунд соответственно
# И теперь нам вернулась строка, которая содержит информацию исключительно о времени

# Подробнее о способах задания формата можно почитать в официальной документации
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

###
# Эти же правила использует метод strptime() По смыслу он противоположен strftime()
# Он получает строку + правила, по которым в ней написано время, а возвращает объект datetime

# Пример:
kyle_death = datetime.datetime.strptime('14.05.1985', '%d.%m.%Y')
print(f'Дата смерти Кайла Риза {kyle_death}')  # 1985-05-14 00:00:00 - type 'datetime.datetime'
# Так мы получили объект, в котором вся информация разложена по полочкам
# И мы можем использовать каждую её часть отдельно:
print(f'День, когда это случилось {kyle_death.day}')  # 14
print(f'Месяц {kyle_death.month}')  # 5
print(f'Год {kyle_death.year}')  # 1985

# кроме прочего, класс datetime обладает интересным методом combine(),
# получая в качестве аргументов объекты классов date и time, мы можем их соединить,
# создав объект класса datetime

sarah_birthday_lunch_time = datetime.datetime.combine(sarah_birthday, lunch_time)
print(f'Дата праздничного обеда родителей Сары Коннор {sarah_birthday_lunch_time}')  # <class 'datetime.datetime'>

# datetime так же позволяет производить арифметические операции с датами, для этого есть класс timedelta
# Так, например, мы можем узнать сколько времени продолжалась война против скайнета:

end_of_war = datetime.datetime(year=2029, month=7, day=11)

duration_of_the_war = end_of_war - rise_of_skynet_datetime  # помните о порядке вычитания (из будущего прошлое)
print(f'Война длилась {duration_of_the_war.days} дней и {duration_of_the_war.seconds} секунд')

# Сам же результат вычислений будет принадлежать новому классу timedelta
print(type(duration_of_the_war))  # <class 'datetime.timedelta'>
# Этот класс используется, как отрезок времени, который можно сложить с датой или умножить на константу

print(f'Закончилась война в {rise_of_skynet_datetime + duration_of_the_war}')

print(f'А ведь могла продлиться {duration_of_the_war * 2}')

# но мы также можем отнять нужный нам отрезов времени от указанной даты.
# Для этого создадим объект timedelta "вручную":

war_time = datetime.timedelta(weeks=40, days=11358, hours=13, minutes=36, seconds=600)

print(f'Воссозданная дата начала восстания машин {end_of_war - war_time}')

# полный перечень операций можно найти в официальной документации
# https://docs.python.org/3/library/datetime.html#timedelta-objects


###
# Примеры работы с датой:

# На вашем сайте создали страницу для регистрации пользователей на предстоящую конференцию
# по приготовлению маффинов. Событие важное, поэтому регистрация должна состояться до определенной даты.
# Это значит, что помимо прочих валидационных условий, вам нужно проверить дату регистрации участника
# и сверить эту дату с заданной датой окончания регистрации:

incoming_date = '30-11-2018'  # как принято в РФ - день, месяц, год
incoming_date_datetime = datetime.datetime.strptime(incoming_date, '%d-%m-%Y')

registration_end_time = datetime.datetime(year=2019, month=1, day=1)

if incoming_date_datetime > registration_end_time:
    print('Отказ в регистрации')
else:
    print('Регистрация одобрена')


###
# Как учитывать часовые пояса(тайм-зоны)?

# Стандартной тайм-зоной считается UTC (Всеми́рное координи́рованное вре́мя) (https://clck.ru/AfPY5)
# UTC заменил устаревшее время по Гринвичу (GMT).
# Это своеобразный "нулевой" часовой пояс, начальная точка отсчёта, от которой отмеряются все остальные тайм зоны.
#
# Например Московское время на 3 часа раньше UTC: +3 UTC.
# Это значит, что когда по UTC будет 10:00, в Москве будет 13:00
# А вот Лондон например расположен прямо в центре нулевого часового пояса.
# Поэтому для нахождения времени в Лондоне не придётся ничего прибавлять

# Объекты времени без явно заданной информации о таймзоне называют naive или "относительное время" на русском
# Примеры:

print(f'Текущая дата, без уточнения тайм-зоны {datetime.datetime.today()}')

# Объекты с заданной явно информацией называются aware, что иногда на русском называют "абсолютное время"
# Информация о часовых поясах часто меняется.
# Сбором и хранением таких обновлений занимается:
# Tzdata - глобальная база знаний о часовых поясах.
# Она же tz database, она же zoneinfo database, она же
# Olson database — в честь Артура Олсона, основателя этой базы знаний.

# Важной для нас особенностью является то, что она хранит не просто информацию о часовых поясах,
# а правила, по которым можно расчитать время для нужной тайм-зоны

# И пользоваться этой информацией нам помогает модуль pytz
import pytz  # $pip install pytz

print(f' Перечень всех доступных таймзон: {pytz.all_timezones}')
print(f' В перечне содержится информация о {len(pytz.all_timezones)} таймзонах')  # 592 на данный момент

# Как ими пользоваться?

print('Asia/Vladivostok' in pytz.all_timezones)  # True
vladivostok_time_zone = pytz.timezone('Asia/Vladivostok')

moscow_time = datetime.datetime.today()
print(f'Московское время {moscow_time}')
vladivostok_time = moscow_time.astimezone(vladivostok_time_zone)
print(f'Время во Владивостоке {vladivostok_time}')


# Пример.
# Из двух городов России (Владивосток и Калининград) пришли две заявки с датой и временем (в их местном часовом поясе)
# Нужно узнать кто из них первым совершил покупку.
print('Europe/Kaliningrad' in pytz.all_timezones)
kaliningrad_time_zone = pytz.timezone('Europe/Kaliningrad')
UTC_time_zone = pytz.utc

request_from_vladivostok_str = '2019-06-15T16:22:00 +1000'
request_from_kaliningrad_str = '2019-06-15T12:05:30 +0200'

vladivostok_request = datetime.datetime.strptime(request_from_vladivostok_str, '%Y-%m-%dT%H:%M:%S %z')
kaliningrad_request = datetime.datetime.strptime(request_from_kaliningrad_str, '%Y-%m-%dT%H:%M:%S %z')
print(f'Время отправки запроса по местному времени Владивостока {vladivostok_request}')
print(f'Время отправки запроса по местному времени Калининграда {kaliningrad_request}')

# Отформатированную информацию можно приведем к UTC для сравнения:
vladivostok_request_UTC = vladivostok_request.astimezone(UTC_time_zone)
kaliningrad_request_UTC = kaliningrad_request.astimezone(UTC_time_zone)
fisrt_request = vladivostok_request_UTC if kaliningrad_request_UTC > vladivostok_request_UTC else kaliningrad_request_UTC
print(f'Время первого запроса {fisrt_request}')

if vladivostok_request_UTC > kaliningrad_request_UTC:
    print('Первым запрос пришёл из Калининграда')
else:
    print('Первым запрос пришёл из Владивостока')


###
# Модуль calendar

import calendar

# Позволяет вывести календарь в виде простого текста или в HTML формате.

# Создание строчного календаря:
calendar_text = calendar.TextCalendar()  # 'str'
# далее, для отображения, нужно уточнить год и месяц
print(calendar_text.formatmonth(2025, 1))

# также можно создать HTML-версию календаря
calendar_HTML = calendar.HTMLCalendar()
print(calendar_HTML.formatmonth(2025, 1))  # 'calendar.HTMLCalendar'

# Помимо красивого отображения календаря по месяцам,
# можно также получить доступ к месяцам, неделям и дням заданного года.

# Например мы хотим посчитать сколько рабочих дней (не учитывая праздники) будет в январе 2025

day_iterator = calendar_text.itermonthdays2(2025, 1)
number_of_working_days = 0

for data, weekday in day_iterator:               # Итератор будет возвращать tuple из 2 цифр
    if data > 0 and weekday < 5:                 # Номер дня в месяце(0-31) и номер дня в неделе (0-6)
        number_of_working_days += 1              # 0-ми отмечаются дни из других месяцев,
                                                 # которые влезли в начало или конец
print(f'В январе 2025 {number_of_working_days} рабочих дней')

# Помимо итераторов, можно вытаскивать из календаря списки дней в месяце

print(f'Дни февраля 2025 года в списках по неделям {calendar_text.monthdayscalendar(2025, 2)}')

# Кроме прочего доступ есть к названиям месяцев или дней недели

for month in calendar.month_name:
    print(month)  # цикл последовательно выдаст английские названия месяцев

for day in calendar.day_name:  # тоже самое но с названиями дней недели
    print(day)

# Более подробно про календарь см https://docs.python.org/3/library/calendar.html
