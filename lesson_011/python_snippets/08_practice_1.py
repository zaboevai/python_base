# -*- coding: utf-8 -*-

# Погружаемся в функциональный стиль - За-заикальщик
# Написать функцию которая повторяет два первых символа у строки

animal = 'мишка'


def stutter(text):
    return text[:2] + '-' + text

print(stutter(animal))

# Написать функцию которая возвращет функцию повторения двух первых символов n раз


def stutter_factory(n):

    def stutter(text):
        return (text[:2] + '-') * n + text

    return stutter

stutter_2 = stutter_factory(n=2)
print(stutter_2(animal))
stutter_3 = stutter_factory(n=3)
print(stutter_3(animal))

# Создать массив функций и применить все функции поочередно к аргументу
stutters = [stutter_factory(n=n) for n in range(1, 4)]
print(stutters)
result = [func(animal) for func in stutters]
print(result)

# Применим все функции поочередно к массиву аргументов
animals = ['зайка', 'мишка', 'бегемотик']
mesh = [func(animal) for animal in animals for func in stutters]
print(mesh)
