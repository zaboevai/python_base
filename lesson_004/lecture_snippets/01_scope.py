# -*- coding: utf-8 -*-

# Пространство имен (namespace) - место где живут переменные

# Глобальное пространство имен
a, b = 1, 2
print('global:', a+b)


def simple():
    print('simple:', a + b)


simple()


# Локальное пространство - имена локальных в функции переменных
a, b = 1, 2
print('global:', a+b)


def simple():
    # Локальное пространство имен  имен появляется в момент вызова функции
    c, d = 3, 4
    print('simple:', c + d)


def simple_2():
    # Локальное пространство имен
    x, y = 3, 4
    print('simple_2:', x + y)
    # print('simple_2:', c + d)

simple()
simple_2()
print('global:', c + d)

# Операторы управления потоком не создают локального пространства имен
if 2 > 1:
    e, f = 5, 6
    print('if:', e + f)
# else:
#     e, f = 7, 8
print('global:', e + f)

for elem in [1, 2, 3]:
    print('for:', elem)
    e, f = 5, 6
print('global:', elem)
print('global:', e + f)
e, f = 0, 0


# перекрытие глобальных переменных
a, b = 1, 2
print('global:', a+b)


def simple():
    # Локальное пространство имен
    a, b = 3, 4
    print('simple:', a + b)


simple()
print('global', a+b)


# Если переменной нет в локальном namespace, то значение берется из глобального namespace
a, b = 1, 2
print('global:', a+b)

def simple():
    # Локальное пространство имен
    b = 4
    print('simple:', a + b)


simple()
print('global', a+b)


# если в функции есть присвоение - это будет локальная переменная
def simple():
    # Локальное пространство имен
    print('simple:', a + b)
    a = 9
    print('simple:', a + b)


# параметры - это локальные переменные
def simple_3(a, b):
    print('simple:', a + b)


a, b = 2, 2
print('global', a+b)
simple_3(a=3, b=4)


# будет целый урок посвященный пространствам имен и областям видимости
