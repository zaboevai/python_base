# -*- coding: utf-8 -*-

# Простое определение функции

# def <имя_функции>(...):
#     <блок кода>


def some_func():
    print('Привет! Я функция')


some_func()

my_list = [3, 14, 15, 92, 6]
for element in my_list:
    some_func()


# Более сложное определение функции - параметры
def func_with_params(param):
    print('Функцию вызвали с параметром', param)


my_list = [3, 14, 15, 92, 6]
for element in my_list:
    print('Начало цикла')
    func_with_params(element)
    print('Конец цикла')

for element in my_list:
    print('Начало цикла')
    func_with_params(param=element)
    print('Конец цикла')


# возврат значения из функции

def power(number, pow):
    print('Функцию вызвали с параметрами', number, pow)
    power_value = number ** pow
    return power_value


my_list = [3, 14, 15, 92, 6]
for element in my_list:
    result = power(element, 10)
    print(result)

for element in my_list:
    result = power(number=element, pow=element)
    print(result)


# если нет return то возвращается None

def some_func():
    print("я ничего не верну")

result = some_func()
print(result)


# можно возвращать несколько значений
def create_default_user():
    name = "Василий"
    age = 27
    return name, age


user_name, user_age = create_default_user()


# документирование
def my_function():
    """Не делаем ничего, но документируем.

    Нет, правда, эта функция ничего не делает.
    """
    pass


print(my_function.__doc__)


# динамическая типизация
def multiplay(number_1, number_2):
    print('Функцию вызвали с параметрами', number_1, number_2)
    value = number_1 * number_2
    return value


print(multiplay(number_1=42, number_2=27))
print(multiplay(number_1='привет! ', number_2=34))


# Параметры передаются как ссылка

def elephant_to_free(some_list):
    elephant_found = 'elephant' in some_list
    if elephant_found:
        some_list.remove('elephant')
        print('Слон на свободе!!!')
    return elephant_found


zoo = ['lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant']

elephant_to_free(zoo)
print(zoo)

elephant_to_free(zoo)
print(zoo)

elephant_to_free(zoo)
print(zoo)

# это т.н. функции с побочными эффектами, они меняют контекст выполнения.
# можно заблокировать изменение параметров - передать тьюпл
zoo = ('lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant')
elephant_to_free(zoo)
print(zoo)

