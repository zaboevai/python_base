# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.prime_numbers = []
        self.start = 1
        self.end = n

    def __iter__(self):
        self.start = 1
        self.prime_numbers = []
        return self

    def __next__(self):
        self.start += 1
        for number in range(self.start, self.end + 1):
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.start = number
                self.prime_numbers.append(self.start)
                return self.start

        raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


number_generator = prime_numbers_generator(n=10000)
for number in number_generator:
    print(number)


# Усложненное задание (делать по желанию)
# Преобразовать итератор/генератор так, чтобы он выдавал только "счастливые" простые числа
# у которых сумма первых цифр равна сумме последних
# Если простое число имеет нечетное число цифр (например 727 или 92083),
# то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#   727 -> 7(2)7 -> 7 == 7 -> True
#   92083 -> 92(0)83 -> 9+2 == 8+3 -> True


def lucky_prime_numbers_generator(n):

    for number in prime_numbers_generator(n):
        lucky_nmb_len = len(str(number))
        cnt = (lucky_nmb_len-1) // 2 if lucky_nmb_len % 2 != 0 else lucky_nmb_len // 2

        if cnt:
            left_path, right_path = str(number)[:cnt], str(number)[-cnt:]

            left_nmb_sum = sum([int(num) for num in left_path])
            right_nmb_sum = sum([int(num) for num in right_path])

            if left_nmb_sum == right_nmb_sum:
                yield number, left_path, right_path


number_generator = lucky_prime_numbers_generator(n=100000)
for number, l_path, r_path in number_generator:
    print(f'{number}')
