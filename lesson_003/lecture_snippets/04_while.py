# -*- coding: utf-8 -*-

# Цикл while (повторение части кода)

# while <условие>:
#     <блок кода>

print('дратути!')
i = 1
while i < 10:
    i = i * 2
    print(i)
print('дотвидания!')

# последовательность Фибоначи 1, 1, 2, 3, 5, 8, 13, 21, ...
f1, f2 = 1, 1
while f2 < 1000:
    print(f2)
    next_f2 = f1 + f2
    next_f1 = f2
    f1, f2 = next_f1, next_f2

# else
i = 1
while i < 10:
    i *= 2
    print(i)
else:
    print('i >= 10')
print('дотвиданя!')

# break
my_pets = ['cat', 'dog', 'hamster']
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print('Проверяем ', pet)
    if pet == 'cat':
        print('Ура, кот найден!')
    i += 1
print('дотвиданя!')


# continue
my_pets = ['lion', 'dog', 'skunk', 'hamster', 'cat', 'monkey']
i = -1
while i < len(my_pets):
    i += 1
    if i == 2:
        continue
    pet = my_pets[i]
    print('Проверяем ', pet)
    if pet == 'cat':
        print('Ура, кот найден!')
        break
print('дотвиданя!')


# else, break and continue - все вместе
f1, f2, count = 0, 1, 0
while f2 < 10000:
    count += 1
    if count > 27:
        print('Итераций больше чем 27. Прерываюсь.')
        break
    f1, f2 = f2, f1 + f2
    if f2 < 1000:
        continue
    print(f2)
else:
    print('Было', count, 'итераций')


# корректный ввод пользователя
while True:
    user_input = input('Введите 42 >> ')
    result = int(user_input)
    if result == 42:
        print('Спасибо за сотрудничество!')
        break
    else:
        print('Я просил 42, а Вы ввели', result, 'Попробуйте еще раз...')


