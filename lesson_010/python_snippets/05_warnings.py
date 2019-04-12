# -*- coding: utf-8 -*-

# Предупреждения - Warnings
#
# Обычно используются для сообщений пользователю о ситуациях в ходе выполнения программы,
# которые не должны приводить к остановке программы.
#
# Часто можно видеть в библиотеках - они предупреждают что, пока работают,
# но в будущем могут сломаться...


# Бросить предупреждение - функция warnings.warn()
import warnings


def greet_person(person_name):
    if person_name == 'Robert':
        warnings.warn('Опять этот Роберт...')
    print(f'Hi there {person_name}')


greet_person('Robert')
print('Выполнение продолжается')
for i in range(10):
    print(f'i={i}')


# функция warn() может принимать категорию предупреждения
#
# Warning - This is the base class of all warning category classes.
#           It is a subclass of Exception.
# UserWarning - The default category for warn().
# DeprecationWarning - Base category for warnings about deprecated features
#           (ignored by default).
# SyntaxWarning - Base category for warnings about dubious syntactic features.
# RuntimeWarning - Base category for warnings about dubious runtime features.
# FutureWarning  - Base category for warnings about constructs that will change
#           semantically in the future.
# PendingDeprecationWarning - Base category for warnings about features that will be
#           deprecated in the future
#           (ignored by default).
# ImportWarning 	Base category for warnings triggered during
#           the process of importing a module
#           (ignored by default).
# UnicodeWarning 	Base category for warnings related to Unicode.
# BytesWarning 	Base category for warnings related to bytes and bytearray.
# ResourceWarning 	Base category for warnings related to resource usage.

def greet_person(person_name):
    if person_name == 'Robert':
        warnings.warn('Опять этот Роберт...', category=RuntimeWarning)
    print(f'Hi there {person_name}')


greet_person('Robert')

# ловить варгинги нельзя! многие путаются
try:
    greet_person('Robert')
    print('Выполнение продолжается')
except RuntimeWarning:
    print('поймали RuntimeWarning!!!')
for i in range(10):
    print(f'i={i}')


# Но можно фильтровать предупреждения, выводимые программой. Существуют такие действия фильтров:
#
# "error" 	turn matching warnings into exceptions
# "ignore" 	never print matching warnings
# "always" 	always print matching warnings
# "default" 	print the first occurrence of matching warnings for each location where the warning is issued
# "module" 	print the first occurrence of matching warnings for each module where the warning is issued
# "once" 	print only the first occurrence of matching warnings, regardless of location

# как временно отключить предупреждения?
#  - запустить скрипт с параметром -W "ignore"
#  - вызвать функцию simplefilter("ignore")


def greet_person(person_name):
    if person_name == 'Robert':
        warnings.warn('Опять этот Роберт...', category=RuntimeWarning)
    print(f'Hi there {person_name}')


warnings.simplefilter("ignore")
greet_person('Robert')


# более подробно см https://docs.python.org/3.6/library/warnings.html
