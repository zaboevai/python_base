# -*- coding: utf-8 -*-


# Способы вызова функций
def vector_module(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# позиционные параметры
res = vector_module(2, 3, 4)
print(res)

# именованные параметры
res = vector_module(x=2, y=3, z=4)
print(res)

# если параметры именованные, то порядок неважен
res = vector_module(z=4, x=2, y=3)
print(res)

# можно совмещать
res = vector_module(2, 3, z=4)
print(res)


# можно потребовать, что бы при вызове некоторые параметры указывались явно
# это будут все параметры, которые идут после *
def vector_module(x, y, *, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# не пройдёт
res = vector_module(2, 3, 4)
# все нормально
res = vector_module(2, 3, z=4)
res = vector_module(z=4, x=2, y=3)


# можно потребовать указание всех параметров явно
def vector_module(*, x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# не пройдёт
res = vector_module(2, 3, 4)
res = vector_module(2, 3, z=4)
# все нормально
res = vector_module(z=4, x=2, y=3)


# неправильные вызовы функций
# res = vector_module()  # не передали ни одного параметра
# res = vector_module(2, 3)  # передали мало параметров
# res = vector_module(2, 3, 3, 4)  # передали много параметров
# res = vector_module(x=2, y=3, x=4)  # повтор параметра
# res = vector_module(2, 3, x=4)  # повтор параметра
# res = vector_module(2, y=3, 4)  # позиционный параметр идет после именованного
# res = vector_module(x=2, y=3, z=5, dist=4)  # неизвестное имя параметра


# распаковка параметров (аргументов)
def vector_module(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# распаковка позиционных параметров
some_list = [2, 3, 4]
res = vector_module(*some_list)
# x, y, z = some_list
# vector_module(2, 3, 4)
print(res)


# распаковка именованных параметров
some_dict = {'x': 2, 'y': 3, 'z': 4}
res = vector_module(**some_dict)
# vector_module(x=2, y=3, z=4)
print(res)

# можно совмещать
some_list = [2, 3]
some_dict = dict(z=4)
res = vector_module(*some_list, **some_dict)
# vector_module(2, 3, z=4)
some_list = [3, 4]
res = vector_module(2, *some_list)
print(res)

# самый лучший и устойчивый вызов - именованными параметрами
res = vector_module(x=2, y=3, z=4)
print(res)


# параметры по умолчанию
def process(subject, action='мыла', object='раму'):
    print("Кто - ", subject)
    print("Делал(а) - ", action)
    print("Над чем - ", object)
    print("Получается :", subject, action, object)


process(subject='Мама')
process(subject='Папа', action='сломал')
process(subject='Кржижановский', action='видел', object='Ленина')  # https://goo.gl/My5Wx7


# значения по умолчанию вычисляются в точке определения функции, при компиляции
# обычная ошибка - изменяемый обьект в качестве параметра по умолчанию
def add_element_to_list(element, list_to_add=[]):
    """добавляем элемент к списку"""
    list_to_add.append(element)
    return list_to_add


my_list = [3, 4, 5]
add_element_to_list(element=1, list_to_add=my_list)
print(my_list)

# new_list = add_element_to_list(element=1)
# print(new_list)
# add_element_to_list(element=7, list_to_add=new_list)
# print(new_list)

# other_new_list = add_element_to_list(element=2)
# print(other_new_list)
# print(new_list)


# решение проблемы
def add_element_to_list(element, list_to_add=None):
    """добавляем элемент к списку"""
    if list_to_add is None:
        list_to_add = []
    list_to_add.append(element)
    return list_to_add


my_list = [3, 4, 5]
add_element_to_list(element=1, list_to_add=my_list)
print(my_list)

# new_list = add_element_to_list(element=1)
# print(new_list)
# add_element_to_list(element=7, list_to_add=new_list)
# print(new_list)

# other_new_list = add_element_to_list(element=2)
# print(other_new_list)
# print(new_list)
