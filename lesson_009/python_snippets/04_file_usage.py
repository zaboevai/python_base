# -*- coding: utf-8 -*-

# Простые формы работы с файлами

# Чтение построчно - символ окончания строки - \n
file_name = 'pushkin.txt'
file = open(file_name, mode='r', encoding='utf8')
for line in file:  # если файл огромный - будет читать только строку
    print(line)
file.close()


# еще вариант
file_name = 'pushkin.txt'
file = open(file_name, mode='r', encoding='utf8')
for line in file.readlines():  # если файл огромный - все прочитает в память, не делайте так!
    print(line)
file.close()

# еще вариант
file_name = 'pushkin.txt'
file = open(file_name, mode='r', encoding='utf8')
line = True
while line:
    line = file.readline()
    if 'красавица' in line:
        print('Красавица найдена в строке', line)
        break
else:
    print('Тут красавиц нет')
file.close()

# Надо всегда следить что бы файл был закрыт при выходе из программы
# Есть оператор with - полезный для работы с файлами. Он автоматически закроет файл
file_name = 'pushkin.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line)
print(file.closed)


# with в общем случае работает с контекстными менеджерами https://goo.gl/J2TZRq
class InOutBlock:

    def __enter__(self):
        print('Входим в блок кода')
        # TODO обратите внимание что тут надо вернуть обьект - в видео это пропущено
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Выходим из блока кода')

    def some_method(self):
        print('Выполяем метод обьекта InOutBlock')


with InOutBlock() as in_out:
    # in_out = InOutBlock()
    print('Некоторый код')
    in_out.some_method()

# то есть обьект файла реализует интерфейс контекстного менеджера
# и закрывает файл при выходе из блока кода
