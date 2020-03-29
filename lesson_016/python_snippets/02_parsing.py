# -*- coding: utf-8 -*-

#
# 16.02 Парсинг сайтов
#

# Парсинг сайта позволяет автоматизировать сбор информации с нужных нам источников.
# Какие могут быть цели для такого сбора?
# 1) Сбор данных для анализа
# 2) Исследование рынка - можно например следить за изменением цен конкурентов
# 3) Получение контента - кто-то использует парсинг, чтобы наполнить свой сайт или приложение контентом
# 4) Самопарсинг - способ структурировать данные с вашего ресурса, для их переноса
# 5) Личное пользование - вы можете собрать разные информационные источники и получать обновления в удобном вам виде
# 6) Извлечение персональной информации - способ наполнить базу данных клиентов

# Первым делом для парсинга нам потребуется HTML-документ с какого-нибудь сайта
# чтобы его получить, воспользуемся библиотекой requests

import requests

response = requests.get('https://yandex.ru/')

# Посмотреть весь документ мы сможем командой
print(response.text)


# В большинстве случаев мы увидим структуру данных,
# схожую с XML, со сложной вложенной иерархией
# Но основная структура зачастую выглядят так:
# <html>
# <head>...</head>
# <body>...</body>
# </html>
# Элементы, заключенные в <> называются теги,
# и с их помощью мы сможем ориентироваться в документе и производить поиск.

# Стандратный инструмент Python для парсинга - html.parser:
# - https://docs.python.org/3/library/html.parser.html

from html.parser import HTMLParser

# Главным инструментом библиотеки явялеятся класс HTMLParser,
# функционал которого можно переписать:

# Базовый класс имеет несколько важных методов:
# -- handle_starttag вызывается каждый раз, когда наш парсер натыкается на открывающий тег
# -- handle_endtag тоже самое но с закрывающим тегом
# -- handle_data так же, но с данными внутри тегов
# Привяжем к этим событиям вывод тегов или данных через print:


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Encountered a start tag: <{tag}>')

    def handle_endtag(self, tag):
        print(f'Encountered an end tag : </{tag}>')

    def handle_data(self, data):
        print(f'Encountered some data  : "{data}"')


# Для примера скормим нашему парсеру пару простых строк:
parser = MyHTMLParser()
parser.feed('''
<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1>Parse me!</h1>
    </body>
</html>
''')

# В итоге, каждый раз, встречая открывающий тег, данные или закрывающий тег,
# будут запускаться соответствующие методы, выполняя те функции, которые мы укажем.

# html.parser является самодостаточным, но довольно сложным инструментом.


# Сторонние библиотеки:

# Одна из популярных библиотек пайтона для парсинга - BeautifulSoup
# - https://www.crummy.com/software/BeautifulSoup/

from bs4 import BeautifulSoup

# Попробуем с её помощью получить актуальную
# информацию о курсе доллара, евро и нефти с сайта yandex.ru:

import requests
response = requests.get('https://yandex.ru/')

if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features='html.parser')
    list_of_values = html_doc.find_all('span', {'class': 'inline-stocks__value_inner'})
    list_of_names = html_doc.find_all('a', {'class': 'home-link home-link_black_yes inline-stocks__link'})

    for names, values in zip(list_of_names, list_of_values):
        print(names.text, values.text)

# Чтобы узнать, какие теги нам нужны, нужно проанализировать саму страницу
# Для этого можно открыть её в браузере и посмотреть код всей страницы или нужного элемента.

# В нашем случае это теги 'span' и 'a' c атрибутами 'class:...'
# Пример того, как это выглит внутри документа:
# <a class="home-link home-link_black_yes inline-stocks__link" href="https://news.yandex.ru/quotes/2002.html"
# data-statlog="news_rates_manual.id2002" data-statlog-showed="1">USD&nbsp;MOEX</a>


# lxml и XPath

# lxml - это быстрая и гибкая библиотека для обработки разметки XML и HTML
# одним из её плюсов является возможность разложения элементов документа в дерево.

# XPath - мощный инструмент для навигации по документам HTML/XML
# Чем то он напоминает регулярные выражения.
# Следуя некоторым правилам синтаксиса, составляется шаблон.
# И учитывая правила, наложенные шаблоном, мы сможем вытащить
# необходимую информацию из документа.
# -- https://www.w3schools.com/Xml/xpath_syntax.asp

import lxml.html

# Пример:
# попробуем вытащить актуальное время по UTC
# 1. Получаем HTML-документ
time_response = requests.get('https://www.utctime.net/')
# 2. Преобразуем его в дерево
html_tree = lxml.html.document_fromstring(time_response.text)
# 3. Вытаскиваем нужное по шаблону
list_of_matches = html_tree.xpath("//*[@id='time2']")
print(f'Время по UTC: {list_of_matches[0].text}')


# Динамические сайты.

# Некоторые сайты формируют страницы, показываемые пользователю, динамически, на стороне сервера
# Что и осложняет процесс парсинга подобных страниц.
# Один из популярных приемов на таких сайтах использует "бесконечную прокрутку"
# В итоге, при достижении "конца" страницы, страница изменяется и добавляется новый контент.
# Попробуем решить эту задачу, использую ещё одну стороннюю библиотеку - Scrapy
# - https://scrapy.org/
# Её интересной особенностью является то,
# что для каждой определенной задачи мы создаём своего "паука"
# Указываем ему диапазон страниц, которые он должен посетить
# Наделяем методами, организующими сбор информации,
# И запускаем.

# Первым делом (после установки) нам понадобится создать отдельный проект для него:
# scrapy startproject <name>
# далее написать самого "паука", создав файл в директории spiders
# Код нашего паучка:

import json
import scrapy


class SpidyQuotesSpider(scrapy.Spider):
    name = 'spidyquotes'
    quotes_base_url = 'http://spidyquotes.herokuapp.com/api/quotes?page=%s'
    start_urls = [quotes_base_url % 1]
    download_delay = 1.5

    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('quotes', []):
            yield {
                'text': item.get('text'),
                'author': item.get('author', {}).get('name'),
                'tags': item.get('tags'),
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(self.quotes_base_url % next_page)

# запустить его можно из каталога с файлом scrapy.cfg
# с помощью команды scrapy crawl <name_of_spider>
# важно, что при запуске нужно указать не имя файла
# а имя паучка, указанное в классе
# name = 'spidyquotes'

# В нашем случае паучок решает задачу получения информации с динамического сайта
# путем генерации запросов scrapy.Request(self.quotes_base_url % next_page)
# до тех пор, пока поле has_next не примет значение False.

# Интересно так же то, что паучок извлекает целевые данные в JSON-формате,
# который мы получаем в ответе от сервера.


# Большинство современных сайтов общаются с клиентами, следуя правилам REST API
# REST API (Representational State Transfer application programming interface)
# - это не протокол, а архитектурный стиль к написанию прикладных интерфейсов.
# Для веб-служб, построенных с учетом REST, применяется термин RESTful
# Однако полностью учесть все правила и ограничения REST
# в реальных условиях очень сложно.
# Поэтому чем более она соответствует этим критерием, тем более она RESTful
# Кроме того большинство RESTful-реализацией пользуются JSON-форматом

# Однако важно помнить, что нет единой уникальной формулы для работы с разными сайтами
# каждый сайт нужно проанализировать, прежде чем приступать к парсингу.
