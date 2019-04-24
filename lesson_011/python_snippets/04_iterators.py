# -*- coding: utf-8 -*-

# Что же это за зверь такой - итератор?
#
# В python можно проходить циклом по любому обьекту, если он - итерируемый.
# А что бы обьект стал итерируемым, он должен содержать два метода - __iter__ и __next__


class Family:

    def __init__(self):
        self.dad = 'Вадим'
        self.mom = 'Татьяна'
        self.son = 'Алексей'
        self.i = 0

    def __iter__(self):
        # обнуляем счетчик перед циклом
        self.i = 0
        # возвращаем ссылку на себя - я буду итератором!
        return self

    def __next__(self):
        # а этот метод возвращает значения по требованию python
        self.i += 1
        if self.i == 1:
            return f'Папа - {self.dad}'
        if self.i == 2:
            return f'Мама - {self.mom}'
        if self.i == 3:
            return f'Я - {self.son}'
        if self.i == 4:
            return f'Счастливая семья :)'
        raise StopIteration()  # признак того, что больше возвращать нечего


my_family = Family()
print(my_family)
for value in my_family:
    print(value)

# То есть интерпретатор вызывает метод __next__ при каждом проходе цикла
# а если в __next__ возникает исключение StopIteration - то значит в обьекте нет больше элементов
# и цикл прекращается

# То есть под капотом у for происходит _как_бы_ следующее
try:
    while True:
        value = my_family.__next__()
        print(value)
except StopIteration:
    pass

# Такой же алгоритм срабатывает при вычислении вхождения в последовательность - оператор in
print('Я - Алексей' in my_family)


# Еще пример: последовательность Фибоначчи - https://goo.gl/PoqS7
# Последовательность, в которой каждое последующее число равно сумме двух предыдущих чисел:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


for value in fibonacci(n=10):
    print(value)
# Для больших N функция создаст в памяти огромный список и вернет его - нерационально!


# Сделаем итератор, который будет вычислять следующее значение по требованию (lazy evaluation https://goo.gl/7fzXuA)
class Fibonacci:
    """Итератор последовательности Фибоначчи до N элементов"""

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a


fib_iterator = Fibonacci(10)
print(fib_iterator)
for value in fib_iterator:
    print(value)
print(13 in fib_iterator)
# Каждое значение вычисляется "по месту" - тогда, когда оно понадобилось.

