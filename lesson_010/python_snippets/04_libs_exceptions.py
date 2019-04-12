# -*- coding: utf-8 -*-

# Зачастую библиотеки/пакеты пайтона определяют свои исключения, специфичные для их работы.

# Например, для библиотеки работы с http запросами
import requests

url = 'http://ya.ru'
try:
    data = requests.get(url)
    print(data.text)
except requests.ConnectionError as exc:
    print(f'не могу соединится с {url} потому что {exc}')
# то есть мы можем обрабатывать нештатные ситуации,
# с которой библиотека не справилась (изменить адрес, к примеру, или перейти к следующему)


# или для django
from my_app.models import Blog

try:
    Blog.objects.get(id=27)
except Blog.DoesNotExist:
    print('нет такой записи блога')


# или для pygame (движок диплома)
import pygame


def load_image(name, colorkey=None):
    """
        Load image from file
    """
    fullname = os.path.join(theme.PICTURES_PATH, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as exc:
        print("Cannot load image:", fullname)
        raise SystemExit(exc)
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

# Таким способом мы может поймать специфичные для библиотек исключения
# и принять решение что делать дальше
