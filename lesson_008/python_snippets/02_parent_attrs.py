# -*- coding: utf-8 -*-

# Ко всем ли атрибутам родительского класса можно обратиться?


class Parent:
    class_var_1 = 12
    _class_var_2 = 23
    __class_var_3 = 34

    def __init__(self):
        self.var_1 = 45
        self._var_2 = 56
        self.__var_3 = 67

    def parent_method(self):
        print(self.class_var_1)
        print(self._class_var_2)
        print(self.__class_var_3)
        print(self.var_1)
        print(self._var_2)
        print(self.__var_3)


class Child(Parent):

    def method(self):
        print(self.class_var_1)
        print(self._class_var_2)
        # print(self.__class_var_3)
        print(self.var_1)
        print(self._var_2)
        # print(self.__var_3)


obj = Child()
# obj.parent_method()
obj.method()
