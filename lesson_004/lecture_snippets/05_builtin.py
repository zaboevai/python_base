# -*- coding: utf-8 -*-

# Есть множество функций, которые встроены в интерпретатор

# известные нам
# input() - ввод из консоли
# print() - вывод на консоль
# enumerate() - выдать пары (номер элемента, значение) для списков
# range() - выдать последовательность целых чисел

# другие, наиболее употребляемые

# --- Приведение типов ---
int()
float()
bool()
str()
list()
tuple()
dict()
set()

int('123')
int(123.45)
float('123')
float('123.45')
float(123)

bool(123)
bool(0)
bool(123.45)
bool(0.0)
bool('123')
bool('0')
bool('')
bool(None)

str(123)
str(123.45)
str(True)

my_tuple = (1, 2, 3, 3, 2, 1)
list(my_tuple)
set(my_tuple)

dict([('a', 2), ('b', 3), ])


# --- Числа ---

# abs() - абсолютное значение числа
abs(1)
abs(-1)

# round() - округление до нужного знака
round(3.1425926, 2)
round(3.1425926, 3)
round(3.1425926, 0)

# --- Cписки ---

profit = [100, 20, 5, 1200, 42, ]

# len() - размер списка
len(profit)

# max() - максимальный элемент
max(profit)

# min() - минимальный элемент
min(profit)

# sorted() - отсортированный список
sorted(profit)

# sum() - сумма элементов списка
sum(profit)

# zip() - попарная компоновка элементов двух списков
profit = [100, 20, 5, 1200, 42, ]
days = ['пн', 'вт', 'ср', 'чт', 'пт', ]
res = zip(profit, days, )
print(list(res))

# --- Логические ---

# all() - True если ВСЕ элементы списка/множества True
all([True, True, True, True, ])
all([1, 0, 1, ])
all([1, '0', 1, ])

# any() - True если ХОТЯ БЫ ОДИН элемент списка True
any([True, False, True, True, ])
any([1, 0, None, ])

# --- Интроспекция ---

# dir() - список всех аттрибутов обьекта
dir(profit)
dir([])

# help() - встроенная помощь по функции/обьекту
help(profit)
help(print)

# id() - внутренний идентификатор обьекта
a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
c = [1, 2, 3]
print(id(c))
print(a == b, a is b, id(a) == id(b))
print(a == c, a is c, id(a) == id(c))
print(id(None))
print(id(False))
print(id(True))

# --- Общего назначения ---

# hash() - значение хэша для обьекта. Что такое хэш-функции см https://goo.gl/gZLM4o
hash('Кржижановский')
hash(profit)

# isinstance() - является ли обьект обьектом данного класса
isinstance(profit, list)

# type() - тип(КЛАСС) обьекта
type(profit)

# open() - открыть файл на файловой системе
ff = open('lesson_004/lecture_snippets/05_builtin.py', 'r')
for line in ff.readlines():
    print(line, end='')
ff.close()
# будет целый урок по работе с файлами, пока просто ознакомились
