# -*- coding: utf-8 -*-

# Существуют специальные методы, их вызов "встроен" в интерперетатор -
# он автоматически их вызывает в определенных ситуациях.
# Каких?
#   создание/удаление объектов
#   вызовы встроенных функций
#   преобразований объектов (приведения типов)
#   выполенение операторов языка
#   эмуляция вызова функции
#   работа с аттрибутами объектов

# Такие методы выглядят как __имя__()


# Рассмотрим онструктор __init__()
# автоматичекси вызывается при создании объекта-экземпляра
class Backpack:
    """ Рюкзак """

    def __init__(self):
        self.content = []

    def add(self, item):
        """ Положить в рюкзак """
        self.content.append(item)
        print("В рюкзак положили:", item)

    def inspect(self):
        """ Проверить содержимое """
        print("В рюкзак лежит:")
        for item in self.content:
            print('    ', item)


my_backpack = Backpack()
my_backpack.add(item='ноутбук')
my_backpack.add(item='зарядка для ноутбука')
my_backpack.inspect()


# __init__ может иметь параметры
class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        """ Положить в рюкзак """
        self.content.append(item)
        print("В рюкзак положили:", item)

    def inspect(self, ):
        """ Проверить содержимое """
        print("В рюкзак лежит:")
        for item in self.content:
            print('    ', item)


my_backpack = Backpack(gift='флешка')
my_backpack.add(item='ноутбук')
my_backpack.add(item='зарядка для ноутбука')
my_backpack.inspect()


# аналогичный метод
# object.__del__(self) - вызывается перед уничтожением объекта


# рассмотрим
# __str__ - вызывается при преобразовании объекта к строке str(obj)
# например print(my_backpack)

class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def add(self, item):
        """ Положить в рюкзак """
        self.content.append(item)
        print("В рюкзак положили:", item)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)


my_backpack = Backpack(gift='телефон')
my_backpack.add(item='ноутбук')
my_backpack.add(item='зарядка для ноутбука')
print(str(my_backpack))


# print(my_backpack)
# print(my_backpack.__str__())

# аналогичные методы
# __len__ - вызывается для получения "размера" объекта с помощью функции len()
# __hash__ - вызывается для получения уникального хэша объекта с помощью функции hash()
#               или для операций с хэширующими коллекциями - множества и словари
# __bool__ - вызывается для получения "истинности" объекта с помощью функции bool()


class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def add(self, item):
        """ Положить в рюкзак """
        self.content.append(item)
        print("В рюкзак положили:", item)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __bool__(self):
        return self.content != []

    def __len__(self):
        return len(self.content)


my_backpack = Backpack()
# my_backpack.add(item='ноутбук')
print(bool(my_backpack), len(my_backpack))
if my_backpack:
    print('Рюкзак не пуст!')
    print('В нем лежит', len(my_backpack), 'предметов')
else:
    print('Вот рюкзак пустой, он предмет простой...')


# все специальные методы перечислены в
#   https://docs.python.org/3/reference/datamodel.html#special-method-names
