#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

films     = []
start_pos = 0
text_len  = len(my_favorite_movies)
srt       = (0,4,1,3)

for num, key in enumerate(my_favorite_movies):
    if key == ',':
       films.append(my_favorite_movies[start_pos:num].lstrip())
       start_pos = num+1
    elif num == text_len-1:
       films.append(my_favorite_movies[start_pos:text_len].lstrip())

for i in srt:
    print(films[i])
