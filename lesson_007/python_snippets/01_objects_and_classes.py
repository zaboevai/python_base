# -*- coding: utf-8 -*-

# Одинаковые объекты описываются одним классом
my_car = Toyota()

# Объекты имеют свойства, к которым можно доступиться с помощью точки
print(my_car.color)
"Бордовый металлик"
print(my_car.price)
"1 000 000 руб"
print(my_car.max_velocity)
"200 км/ч"
print(my_car.engine_rpm)
0
print(my_car.current_velocity)
"0 км/ч"

# Объекты имеют действия, которые с ними можно производить.
# Некоторые свойства объектов могут менятся после действий над объектами
my_car.start()  # завели машину
print(my_car.engine_rpm)
900
my_car.go()  # поехали
print(my_car.engine_rpm)
2000
print(my_car.current_velocity)
"20 км/ч"


# В Python свойства называются атрибутами, а действия - методами
# Ссылки на атрибуты и методы используют синтаксис,
# использующийся для всех ссылок на атрибуты в Python: объект.имя.


# Простейшая форма определения класса
# class ClassName:
#     < выражение - 1 >
#     .
#     .
#     .
#     < выражение - N >


# например
class Toyota:

    def __init__(self):
        self.color = "Бордовый металлик"
        self.price = "1 000 000 руб"
        self.max_velocity = "200 км/ч"
        self.current_velocity = "0 км/ч"
        self.engine_rpm = 0

    def start(self):
        self.engine_rpm = 5000

    def go(self):
        self.current_velocity = "20 км/ч"


# Класс - это как лекало для производства объектов.
produced, plan = 0, 10000
stock = []
while produced < plan:
    new_car = Toyota()
    stock.append(new_car)
    produced += 1
# мы можем произвести сколько угодно объектов


# еще пример
class Robot:
    """Простой пример класса"""

    def __init__(self):
        self.name = 'R2D2'

    def hello(self):
        print('привет мир! Я -', self.name)


# создаем новый объект (экземпляра класса)
# и присваиваем локальной переменной robot ссылку на него
robot = Robot()
robot.hello()

# Помним, что переменные только ссылаются на объект

some_var = robot
some_var.hello()

some_robot = some_var
some_robot.hello()

some_robot.name = 'C-3PO'
some_robot.hello()

robot.hello()
