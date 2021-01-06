# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import re
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, date
from typing import List

# import cv2 as cv
import requests
from bs4 import BeautifulSoup


class Weather(ABC):
    DAYS_FORECAST: List[dict] = []

    def __init__(self, content=None):
        self._content = content
        self.days_delta = None

    @abstractmethod
    def get_weather(self, days):
        self.days_delta = days
        pass


class WeatherMaker(Weather):
    CITY = 'kirov'
    URL = f'https://yandex.ru/pogoda/{CITY}'

    def get_weather(self, days=7):
        super().get_weather(days)
        self.get_content_from_site()
        self.get_weather_from_site_content_by_days()

    def get_content_from_site(self):
        if not self._content and self.URL:
            got = requests.get(url=self.URL, verify=True, )
            if not got.ok:
                raise requests.RequestException('Не удалось получить прогноз погоды')

            self._content = got.content

    def get_weather_from_site_content_by_days(self):

        re_day_template = re.compile('\w+day')
        re_condition_template = re.compile('\w+condition')

        content = BeautifulSoup(self._content, 'html.parser')
        days = content.findAll('div', {'class': 'forecast-briefly__day'})
        for day in days:
            day_date = day.findAll('time', {'class': 'forecast-briefly__date'})[0]['datetime']
            day_date = datetime.strptime(day_date, '%Y-%m-%d %H:%M%z').replace(tzinfo=None).date()
            day_temp = day.findAll('div', attrs={'class': re_day_template})[0]
            day_temp = ''.join([value.string for value in day_temp][1:])
            day_condition = day.findAll('div', attrs={'class': re_condition_template})[0].text

            if self.is_in_delta_date(date_=day_date):
                day_forecast = {'дата': day_date, 'температура': day_temp, 'погода': day_condition}
                self.DAYS_FORECAST.append(day_forecast)

    def is_in_delta_date(self, date_):
        return date.today() <= date_ < date.today() + timedelta(days=self.days_delta)
    #
    #
    # class ImageMaker:
    #
    #     def create_weather_card(self):
    #         image = cv.imread('lesson_016/python_snippets/external_data/probe.jpg')
    #         name = cv.namedWindow('weather', cv.WINDOW_NORMAL)
    #         cv.imshow(name, image)
    #         cv.waitKey()
    #         cv.destroyAllWindows()
    #         pass


weather_maker = WeatherMaker()
weather_maker.get_weather()
pass
# image_maker = ImageMaker()
# image_maker.create_weather_card()
