# -*- coding: utf-8 -*-

# А теперь поймаем за хвост другого зверя - генератора.
#
# Мы видели генераторные сборки, но обычную функцию тоже можно превратить в генератор.


def fibonacci_v1(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
# Как уже говорили - нерационально: в памяти создается большой список...
# Решение  - оператор yield (производить, выдавать значение)


# Он приостанавливает выполнение функции и ждет следующего вызова __next__
# и функция превращается в генератор
def fibonacci_v2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib = fibonacci_v2(n=10)
print(fib)
for value in fib:
    print(value)


# Можно вообще сделать бесконечный "список" значений
def fibonacci_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for value in fibonacci_v3():
    print(value)
    if value > 10 ** 6:
        break


# В генераторах можно использовать return - он воспринимается, как завершение итерирования
# и аналогичен raise StopIteration()
def fibonacci_v4():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if a > 10 ** 30:
            return


for val in fibonacci_v4():
    print(val)
# Если у return есть значение, оно помещается в StopIteration - то есть _практически_ не видимо снаружи

# Генераторы используются для тяжеловесных операций - они вычисляют следующее значение по требованию

# Еще одно приятное использование - прерывание вложенных циклов.
# Пусть нам надо найти какие два числа из списков дадут в результате попарного перемножения 56
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

# can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            # can_continue = False
            break
    # if not can_continue:
    #     break

# В пайтоне нет возможности прерывать вложенные циклы, Пришлось вводить переменную-флаг - некрасиво :(
# а если бы циклов было 3?


# С генераторами это решается элегантно
def get_next_result(list_1, list_2):
    for x in list_1:
        for y in list_2:
            yield x, y, x * y


for x, y, result in get_next_result(list_1, list_2):
    print(x, y, result)
    if result == to_find:
        print('Found!!!')
        break


# Есть еще одна возможность у генераторов - они могут принимать значения
#
# Создадим генератор очереди
def queue(*args):
    data = list(args)
    while data:
        next = data.pop(0)
        new_value = (yield next)
        # обратите внимание, что yield возвращает значение и скобки
        if new_value is not None:
            data.append(new_value)


shop_queue = queue('Вася', 'Марина', 'Владислав', 'Эльвира')
for name in shop_queue:
    print(f'К кассе приглашается {name}')
    if name == 'Марина':
        print('А кто последний?')
        name = shop_queue.send('Маргарита Иванна')
        print(f'К кассе приглашается {name}')


# Такие генераторы называются сопрограммами (coroutines)
# - они могут как отдавать значения, так и получать.
# И хранят свое состояние. Сопрограммы можно передавать в качестве параметров в другие функции
# и устраивать цепочки обработки.
# Вот пример промышленного использования сопрограмм https://goo.gl/SHAPNk
