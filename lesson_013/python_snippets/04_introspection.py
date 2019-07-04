# -*- coding: utf-8 -*-

# Зачастую при работе с чужим кодом и/или со сторонними библиотеками возникает проблема:
# Как узнать что из себя представляют и что могут сторонние обьекты?
# Свои обьекты мы знаем, но другие - зачастую загадка...
# Хорошо, если есть документация. А если нет? Нам помогут инструменты интроспекции!


### Как мы помним - есть встроенная помощь
import requests
help(requests)
help(requests.get)

### Интроспекция объектов

# Если у вас произвольный объект, возможно, тот, который был передан в качестве аргумента в функцию,
# вы, наверное, захотите что-нибудь узнать об этом объекте.
#     * Какое у тебя имя?
#     * Какого ты типа?
#     * Что ты знаешь/можешь?
#     * Что ты за объект?
#     * Кто твои предки?

# создадим несколько обьектов

some_string = 'i am a string'
some_number = 42
some_list = [some_string, some_number]


def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)


class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()

### Какое у тебя имя?
# Не все объекты имеют имя, но у тех, у которых оно есть, имя хранится в их атрибуте __name__.
# Имя выводится из объекта, а не из переменной, которая указывает на этот объект.

print(some_function.__name__)
print(SomeClass.__name__)
print(requests.__name__)
# print(some_string.__name__)
# print(some_object.__name__)

rq = requests
print(rq.__name__)

# имя текущего модуля
print(__name__)

### Какого ты типа?
print(type(some_number))

print(type(some_number) is int)
print(type(some_number) is list)


def check_param(value):
    if type(value) is str:
        print('Обрабатываем строку', value)
    else:
        print('Это не строка!')


check_param(value=some_string)
check_param(value=some_list)

print(type(requests))


### Что ты знаешь/можешь?
# Функция dir() возвращает отсортированный список имен атрибутов для переданного в нее объекта

from pprint import pprint

pprint(dir(some_number))
pprint(dir(some_list))
pprint(dir(some_function))
pprint(dir(SomeClass))
pprint(dir(some_object))
# Без указания аргумента dir() возвращает имена в текущей области видимости
pprint(dir())

pprint(dir(requests))


# Встроенная функция hasattr() - проверка на существования атрибута
attr_name = 'attribute_2'
print(hasattr(some_object, attr_name))

# Встроенная функция getattr - получение атрибута
print(getattr(some_object, attr_name))
print(getattr(some_object, attr_name, 'нет такого атрибута'))

print(hasattr(requests, 'get'))
http_get = getattr(requests, 'get')
print(type(http_get))

for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))


# С помощью функции callable() мы можем установить, вызываемый ли это объект
print(callable(some_string))
print(callable(some_function))
print(callable(some_object.attribute_1))
print(callable(some_object.some_class_method))

print(callable(http_get))

###  Что ты за объект?
# с помощью функции isinstance() мы можем выяснить, является ли объект экземпляром определенного типа
# или определенного пользователем класса

print(isinstance(some_number, str))
print(isinstance(some_number, int))
print(isinstance(some_number, SomeClass))
print(isinstance(some_object, SomeClass))

response = requests.get(url='http://skillbox.ru')
print(response)
print(isinstance(response, requests.Response))
print(isinstance(response, requests.NullHandler))


### Кто твои предки?
# Функция issubclass() позволяет установить, наследуется ли один класс от другого

class DerivedClass(SomeClass):
    pass


some_object_2 = DerivedClass()

print(issubclass(SomeClass, DerivedClass))
print(issubclass(DerivedClass, SomeClass))
print(isinstance(some_object_2, SomeClass))
print(isinstance(some_object_2, DerivedClass))

print(issubclass(requests.ConnectTimeout, requests.HTTPError))
print(issubclass(requests.ConnectTimeout, requests.RequestException))

### Модуль inspect - https://docs.python.org/3/library/inspect.html
# собирает удобные методы и классы для отображения интроспективной информации
import inspect

# самые употребимые
print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.isbuiltin(requests))

some_function_module = inspect.getmodule(some_function)
print(type(some_function_module), some_function_module)

signature = inspect.signature(some_function)
print(type(signature), signature)
# pprint(dir(signature))
print(type(signature.parameters), signature.parameters)
for param_name, param in signature.parameters.items():
    print(type(param), param, param.name, param.default)
    # pprint(dir(param))

get_signature = inspect.signature(requests.get)
for param_name, param in get_signature.parameters.items():
    print(param_name, param.name, param.default)


### Полезный системный пакет - sys

import sys
pprint(dir(sys))

# путь к интерпретатору Python
print(sys.executable)

# какой операционной системе мы работаем
print(sys.platform)

# Текущая версия Python
print(sys.version)
print(sys.version_info)

# список, содержащий параметры командной строки, если она была задана
print(sys.argv)

# путь поиска модуля, список каталогов, в которых Python будет искать модули во время импорта
print(sys.path)

# словарь, который отображает имена модулей в объекты модулей для всех загруженных в текущий момент модулей
print(sys.modules)

# Стоит упомянуть __builtins__ - псевдо-модуль, содержащий встроенные в интерпретатор обьекты
# (константы, исклчения, функции)
print(__builtins__)
pprint(dir(__builtins__))

