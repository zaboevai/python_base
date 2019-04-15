# -*- coding: utf-8 -*-

# Порождение исключений
# Зачастую нужно самим создавать исключение, если код не может справиться с данными


def greet_person(person_name):
    """
    says hello
    """
    if person_name == 'Robert':
        # создаем обьект исключения и райзим его
        raise BaseException("We don't like you, Robert")
    print(f'Hi there {person_name}')


greet_person('Dolly')
# greet_person('Robert')


##################
# Варианты порождения исключений
def greet_person(person_name):
    """
    says hello
    """
    if person_name == 'Robert':
        # можно указать только класс исключения,
        # тогда автоматически создастся обьект исключения без параметров
        raise BaseException
    print(f'Hi there {person_name}')


greet_person('Robert')
# но так лучше не делать - старый стиль

# в сети иногда попадаются старинные варианты
# raise BaseException, "message" - валидно для 2.х пайтона, не делайте так
# или даже
# raise "message" - валидно для <2.4 пайтона, не делайте так


##################
# Проброс исключений
try:
    raise NameError('Привет Там')
except NameError as exc:
    print(f'Исключение типа {type(exc)} пролетело мимо! его параметры {exc.args}')
    # обратите внимание на "пустой" оператор - будет переброшено исключение текущего скоупа.
    raise
# используется для зачистки возможно порушенных данных и/или логирования ошибки
# и передачи отвественности вовне - пусть там решают что делать дальше

# можно формировать другое исключение
try:
    raise NameError('Привет Там')
except NameError as exc:
    print(f'Поймано исключение типа {type(exc)}')
    raise TypeError('Привет и тут')
# автоматом прицепляется обьект породившего исключения, в атрбибут __cause__

# можно явно указать
try:
    raise NameError('Привет Там')
except NameError as exc:
    print(f'Поймано исключение типа {type(exc)}')
    raise TypeError('Привет и тут') from exc


##################
# Кастомные исключения
# Можно определять свои исключения - например исключения нашего пакета
class HeroDiedError(Exception):
    pass


class GameOverError(Exception):
    pass


try:
    raise HeroDiedError('Рядовой Райан')
except HeroDiedError as exc:
    print(f'Поймано исключение {exc}')
    raise GameOverError('Миссия провалена')
# первый параметр, как говорилось, сообщение на консоль,
# остальные параметры можно использовать для уточнения самой ошибки
# (входные данные, которые к ней привели, к примеру)


# можно переопределить содержимое обьекта исключения
class DivisionError(Exception):

    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message


def division(a, b):
    if a < b:
        raise DivisionError('Нельзя делить меньшее на большее', input_data=dict(a=a, b=b))
    return a/b


try:
    division(1, 2)
except DivisionError as exc:
    print(f'Поймано моё исключение {exc}, входные данные при ошибке {exc.input_data}')


# Наверно, наиболее частые случаи принудительного выброса исключений:
#   - проверка типов параметров методов/функций
#   - проверка совместности параметров методов/функций
#   - нарушение возможности работы кода (неправильные данные)
