# -*- coding: utf-8 -*-

# Отличительная особенность методов объектов от простых функций состоит в том,
# что методу всегда передаётся ссылка на объект-экземпляр.
# Эта первый параметр метода и обычно он называется self.
# Название - не более чем соглашение: имя self не имеет абсолютно никакого
# специального смысла для языка Python. Но так принято :)


class Backpack:
    """ Рюкзак """

    def add(self, item):
        """ Положить в рюкзак """
        print("В рюкзак положили ", item)
        self.content = item


my_backpack = Backpack()
my_backpack.add(item='ноутбук')

my_son_backpack = Backpack()
my_son_backpack.add(item='учебник')

# то есть аналогия такая, что были вызовы типа таких
# add(self=my_backpack, item='ноутбук')
# add(self=my_son_backpack, item='учебник')

# на самом деле так и есть, просто есть понятие "связанный метод"
# это метод, который привязан к объекту, жестко фиксирован self
print(Backpack.add)
print(my_backpack.add)


# то есть следующие два вызова аналогичны
my_backpack.add(item='ноутбук')
Backpack.add(self=my_backpack, item='ноутбук')


