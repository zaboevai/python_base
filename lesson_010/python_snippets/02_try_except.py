# -*- coding: utf-8 -*-

# Ловля и обработка исключений-ошибок

# код, который _может_ содержать ошибки помещают в спецкапсулу try/except
try:
    i = 0
    print(10 / i)
    print('сделано')
except:
    # ловим все ошибки
    print('нельзя делить на ноль!')

# нужно указывать конкретную ошибку
try:
    i = 0
    print(10 / i)
    print('сделано')
except ZeroDivisionError:  # указываем имя класса
    print('нельзя делить на ноль!')

# можно перечислять классы ошибок, если обработка их одинаковая
try:
    truba = a + b
    truba = 10/0
except (ZeroDivisionError, NameError):  # указываем имена классов
    print('что-то пошло не так, но мы устояли')

# или на каждый класс ошибки писать свой обработчик
try:
    truba = a + b
    truba = 10/0
except ZeroDivisionError:
    print('Они -убили Кенни- хотели делить на ноль, но мы не упали')
except NameError:
    print('Нет такой переменной, кто писал этот код?!')

# можно ловить сам обьект класса ошибки
try:
    a = 10/0
except ZeroDivisionError as exc:
    print(f'вот что пошло не так - {exc}, но мы еще на плаву')

# или для группы исключений
try:
    truba = a + b
except (ZeroDivisionError, NameError) as exc:
    print(f'вот что пошло не так - {exc}, но мы еще на плаву')
# имя переменной для указание на обьект исключения произвольное, но принято использовать exc

# с ошибкой прилетают параметры ошибки - Exception.args
try:
    file = open('blabla.txt')
except OSError as exc:
    print(f'вот что пошло не так - {exc} параметры {exc.args}, но мы еще на плаву')

# некоторые ошибки (OSError) содержат доп информацию, для остальных args это просто сообщение для вывода.
try:
    a = 10/0
except ZeroDivisionError as exc:
    print(f'вот что пошло не так - {exc} параметры {exc.args}, но мы еще на плаву')
# вообще, состав обьекта исключения зависит от ошибки, надо смотреть документацию.


# ошибки летят по стеку вызовов функций
def f1(number):
    return 10 / number


def f2():
    summ = 0
    for i in range(2, -1, -1):
        summ += f1(number=i)
        print(summ)
    return summ

# total = f2()
try:
    total = f2()
except ZeroDivisionError as exc:
    print(f'вот что пошло не так - {exc}, но мы устояли')


# и ловить их можно на разных уровнях
def f1(number):
    return 10 / number


def f2():
    summ = 0
    for i in range(2, -1, -1):
        try:
            summ += f1(number=i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'внутри f1 что-то пошло не так: {exc}, но мы устояли')
    return summ / 0


try:
    f2()
except ZeroDivisionError as exc:
    print(f'внутри f2 что-то пошло не так: {exc}, но мы устояли')


# если ошибка не поймана, она падает до дна стека и разбивается об консоль. а программа умирает...
def f1(number):
    return total / number


def f2():
    summ = 0
    for i in range(2, -1, -1):
        try:
            summ += f1(number=i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'внутри f1 что-то пошло не так: {exc}, но мы устояли')
    return summ / 0


try:
    f2()
except ZeroDivisionError as exc:
    print(f'внутри f2 что-то пошло не так: {exc}, но мы устояли')


# Действия, если исключений не было - else
try:
    10 * (1/0)
except ZeroDivisionError:
    print('нельзя делить на ноль!')
else:
    print('неужели?!')

# действия по подчистке - выполняется всегда - finally
try:
    10 * (1/0)
except ZeroDivisionError:
    print('нельзя делить на ноль!')
else:
    print('неужели?!')
finally:
    print('Прощай, мир!')


# обобщенный пример
try:
    # тут мы пишем код, как буд-то ошибок не будет... наивные...
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
# а потом обрабатываем возможные ошибки
except IOError as exc:
    print("I/O error: ", exc)
except ValueError:
    print("Не могу преобразовать данные в целое!")
except Exception as exc:
    print("Неожиданная ошибка:", exc)
else:
    print('прочитано i=', i)
finally:
    f.close()


# Кстати в методе __exit__ для контекстного менеджера параметры отвечают за исключения

with open('myfile.txt') as ff:
    first_line = ff.readline()
print(first_line)


class InOutBlock:

    def __enter__(self):
        print('Входим в блок кода')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Выходим из блока кода {exc_type}, {exc_val}, {exc_tb}')
        return True  # возвращаем истину, что бы погасить полет исключения


with InOutBlock() as in_out:
    print('Работаем...')
    a = bla_bla / number
    print('Вычислили значение')
print('После контекстного менеджера')
