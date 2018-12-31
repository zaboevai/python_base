# -*- coding: utf-8 -*-

# for <переменная цикла> in <список>:
#     <блок кода>


# Цикл for ("для каждого элемента")
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
print('Выход из цикла')

zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
letters_count = 0
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    letters_count += len(animal)
    pass
print('Всего букв', letters_count)

# принудительный останов цикла - break
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
print('Выход из цикла')

# опция else для цикла
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
else:
    print('Тут слона нет...')
print('Выход из цикла')

# пропуск остатка цикла - continue
zoo_pets = ['lion', 'skunk', 'elephant', 'monkey', 'horse']
for animal in zoo_pets:
    if animal == 'skunk':
        continue
    print('У нас в руках', animal)
print('Выход из цикла')

# полный пример

zoo_pets = [
    'lion', 'monkey', 'skunk',
    'elephant', 'horse',
]
for animal in zoo_pets:
    if animal == 'skunk':
        print('Фууу...')
        continue
    print('Сейчас переменная animal указывает на', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
else:
    print('Тут слона нет...')
print('Выход из цикла')


# Изменять содержимое последовательности, по которой проходит цикл, небезопасно
zoo_pets = [
    'lion', 'skunk',
    'elephant', 'horse',
]
for animal in zoo_pets:
    print(animal)
    del zoo_pets[0]
print(zoo_pets)


# автоматическая распаковка содержимого списка/тьюпла

a, b = 1, 2
(a, b) = (1, 2)

for element in [(1, 2), (3, 4)]:
    a, b = element[0], element[1]
    print(a + b)

for (a, b) in [(1, 2), (3, 4)]:
    print(a+b)

pair_list = [(1, 2), (3, 4), (5, 6)]

for a, b in pair_list:
    print(a+b)

triple_list = [(1, 2, 3), (4, 5, 6)]
for a, b, c in triple_list:
    print(a, b, c)

# в каждом элементе списка должно быть соотв кол-во элементов

for a, b in [(1, 2), (3, 4), (5, 6, 7)]:
    print(a, b)


# полезные функции

# for(i=0; i < 10; i++) {
#       animal = zoo_pets[i];
#       printf(i, animal);
# }

for i, animal in enumerate(zoo_pets):
    print(i, animal)

# генерация целочисленных последовательностей
for i in range(100, 600, 50):
    print(i)

# НЕ ДЕЛАЙТЕ ТАК!!!!
zoo_pets = ['lion', 'skunk', 'elephant', 'horse', ]
for i in range(len(zoo_pets)):
    animal = zoo_pets[i]
    print(i, animal)


# вложенные циклы
zoo_pets = [
    'lion', 'skunk',
    'elephant', 'horse',
]
for animal in zoo_pets:
    for char in animal:
        print(char)
    print(animal)


# цикл по словарям
zoo_pet_mass = {
    'lion': 300,
    'skunk': 5,
    'elephant': 5000,
    'horse': 400,
}
total_mass = 0
for animal in zoo_pet_mass:
    print(animal, zoo_pet_mass[animal])
    total_mass += zoo_pet_mass[animal]
print('Общая масса животных', total_mass)

total_mass = 0
for animal, mass in zoo_pet_mass.items():
    print(animal, mass)
    total_mass += mass
print('Общая масса животных', total_mass)

total_mass = 0
for mass in zoo_pet_mass.values():
    print(mass)
    total_mass += mass
print('Общая масса животных', total_mass)
