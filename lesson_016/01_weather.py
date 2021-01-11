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

import cv2 as cv
import numpy as np
import requests
from PIL import ImageFont, Image, ImageDraw
from bs4 import BeautifulSoup

from lesson_016.db import Database

DATABASE_PATH = 'forecast.db'

YELLOW = (0, 255, 255)
GRAY = (90, 90, 90)
BLUE = (255, 255, 0)
DARK_BLUE = (255, 0, 0)
WHITE = (255, 255, 255)

WEATHER_CARDS = {
    'sun': {
        'path': 'weather_cards/SUN.jpg',
        'background_gradient': (YELLOW, WHITE),
        'tokens': ['солн', 'ясн'],
    },
    'cloud': {
        'path': 'weather_cards/CLOUD.jpg',
        'background_gradient': (GRAY, WHITE),
        'tokens': ['пасм', 'обл'],
    },
    'snow': {
        'path': 'weather_cards/SNOW.jpg',
        'background_gradient': (BLUE, WHITE),
        'tokens': ['сне', 'метел'],
    },
    'rain': {
        'path': 'weather_cards/RAIN.jpg',
        'background_gradient': (DARK_BLUE, WHITE),
        'tokens': ['дожд', ],
    }
}


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
                day_forecast = {'date': day_date, 'temp': day_temp, 'desc': day_condition}
                self.DAYS_FORECAST.append(day_forecast)

    def is_in_delta_date(self, date_):
        return date.today() <= date_ < date.today() + timedelta(days=self.days_delta)


class ImageMaker:
    FONT_PATH = "python_snippets/external_data/fonts/Aller Cyrillic.ttf"
    IMAGE_TEMPLATE_PATH = 'python_snippets/external_data/probe.jpg'

    def create_weather_card(self, forecast):
        """
        Создаеть и показывает карточку на основании прогноза погоды
        """
        current_card = self.get_weather_card(forecast)
        bg_image = cv.imread(self.IMAGE_TEMPLATE_PATH)

        if current_card:
            bg_image = self.create_bg_gradient_by_weather_card(bg_image, current_card)

            weather_img = cv.imread(current_card['path'])
            self.set_weather_img(bg_image, weather_img)

        image = self.set_forecast_text(bg_image, forecast)
        self.view_image(image, 'Weather')

    def set_forecast_text(self, image, forecast):
        """
        Вставляет текст в прогноза погоды
        """
        black_color = (0, 0, 0)
        weather_date = forecast['date'].strftime('%d.%m.%Y')

        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)

        font = ImageFont.truetype(self.FONT_PATH, 34)
        draw.text((160, 20), weather_date, font=font, fill=black_color)
        draw.text((40, 80), forecast['temp'], font=font, fill=black_color)

        font = ImageFont.truetype(self.FONT_PATH, 100)
        draw.text((330, 100), forecast['desc'], font=font, fill=black_color)

        image = np.array(img_pil)
        return image

    @staticmethod
    def set_weather_img(bg_image, weather_img):
        """
        Вставляет картинку прогноза погоды на фон выбранного участка карточки
        """
        rows, cols, channels = weather_img.shape
        weather_bg_img = bg_image[130:130 + rows, 100:100 + cols]
        img2gray = cv.cvtColor(weather_img, cv.COLOR_BGR2GRAY)
        _, mask = cv.threshold(img2gray, 220, 255, cv.THRESH_BINARY)
        mask_inv = cv.bitwise_not(mask)
        weather_bg_img = cv.bitwise_and(weather_bg_img, weather_bg_img, mask=mask)
        weather_img = cv.bitwise_and(weather_img, weather_img, mask=mask_inv)
        weather_img = cv.add(weather_bg_img, weather_img)
        bg_image[130:230, 100:200] = weather_img

    def create_bg_gradient_by_weather_card(self, bg_image, current_card):
        """
        Создает градиентный фон на основании кпрогноза погоды
        """
        _bg_image = bg_image
        y, x, _ = _bg_image.shape
        for line in range(y):
            color = self.next_color(color=current_card['background_gradient'][0],
                                    to_color=current_card['background_gradient'][1],
                                    step=line)
            _bg_image[line, :] = [color for _ in range(x)]
        return _bg_image

    @staticmethod
    def next_color(color, to_color, step=0):
        """
        Возвращает следующей оттенок цвета по направлению градиента
        """
        compared_colors = zip(color, to_color)
        _next_color = []
        for color_, to_color in compared_colors:
            if color_ + step >= to_color:
                _next_color.append(to_color)
                continue
            _next_color.append(color_ + step)
        return _next_color

    @staticmethod
    def get_weather_card(forecast):
        """
        Возвращает настройки прогноза погоды
        """
        current_card = {}
        for card, card_info in WEATHER_CARDS.items():
            for token in card_info['tokens']:
                if token.lower() in forecast['погода'].lower():
                    current_card = WEATHER_CARDS[card]
        return current_card

    @staticmethod
    def view_image(image, name_of_window):
        """
        Показывает карточку погоды
        """
        cv.namedWindow(name_of_window, cv.WINDOW_NORMAL)
        cv.imshow(name_of_window, image)
        cv.waitKey(0)
        cv.destroyAllWindows()


weather_maker = WeatherMaker()
weather_maker.get_weather()
pass
image_maker = ImageMaker()
image_maker.create_weather_card(weather_maker.DAYS_FORECAST[0])
image_maker.create_weather_card({'дата': datetime.today(), 'температура': '−9°', 'погода': 'облач'})
