# -*- coding: utf-8 -*-

# Когда в программе что-то идет не так - то возникает ошибка (я люблю ошибки!)
# Поведением программы в случае ошибки можно управлять.
# Но для начала - что есть ошибка?

# Cинтаксические ошибки
# >>> while True print('Hello world')
# File "<stdin>", line 1, in ?
# while True print('Hello world')
# ^
# SyntaxError: invalid syntax

# Исключительные ситуации
# >>> 10 * (1/0)
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# ZeroDivisionError: integer division or modulo by zero

# >>> 4 + spam*3
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# NameError: name 'spam' is not defined

# >>> '2' + 2
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# TypeError: cannot concatenate 'str' and 'int' objects

# обратите внимание на эти слова SyntaxError ZeroDivisionError NameError TypeError
# все это - исключительные ситуации, exceptions. Это обьекты класса с таким названием.

# все исключения - классы, порожденные от BaseException
# BaseException
#     +-- SystemExit
#     +-- KeyboardInterrupt
#     +-- GeneratorExit
#     +-- Exception
#     +-- StopIteration
#     +-- StopAsyncIteration
#     +-- ArithmeticError
#     |   +-- FloatingPointError
#     |   +-- OverflowError
#     |   +-- ZeroDivisionError
#     +-- AssertionError
#     +-- AttributeError
#     +-- BufferError
#     +-- EOFError
#     +-- ImportError
#     |   +-- ModuleNotFoundError
#     +-- LookupError
#     |   +-- IndexError
#     |   +-- KeyError
#     +-- MemoryError
#     +-- NameError
#     |   +-- UnboundLocalError
#     +-- OSError
#     |   +-- BlockingIOError
#     |   +-- ChildProcessError
#     |   +-- ConnectionError
#     |   |   +-- BrokenPipeError
#     |   |   +-- ConnectionAbortedError
#     |   |   +-- ConnectionRefusedError
#     |   |   +-- ConnectionResetError
#     |   +-- FileExistsError
#     |   +-- FileNotFoundError
#     |   +-- InterruptedError
#     |   +-- IsADirectoryError
#     |   +-- NotADirectoryError
#     |   +-- PermissionError
#     |   +-- ProcessLookupError
#     |   +-- TimeoutError
#     +-- ReferenceError
#     +-- RuntimeError
#     |   +-- NotImplementedError
#     |   +-- RecursionError
#     +-- SyntaxError
#     |   +-- IndentationError
#     |       +-- TabError
#     +-- SystemError
#     +-- TypeError
#     +-- ValueError
#     |   +-- UnicodeError
#     |       +-- UnicodeDecodeError
#     |       +-- UnicodeEncodeError
#     |       +-- UnicodeTranslateError
#     +-- Warning
#         +-- DeprecationWarning
#         +-- PendingDeprecationWarning
#         +-- RuntimeWarning
#         +-- SyntaxWarning
#         +-- UserWarning
#         +-- FutureWarning
#         +-- ImportWarning
#         +-- UnicodeWarning
#         +-- BytesWarning
#         +-- ResourceWarning

# полное описание здесь - https://docs.python.org/3/library/exceptions.html

# То есть в момент нештатной ситуации интерпретатор создает обьект нужного класса и "бросает" его (raise)
# Куда бросает? в стек вызовов - чуть позже разберем что это такое.
# Если программа поймала этот обьект исключительной ситуации - то она будет устойчивой к ошибкам,
# и это хорошо. Если не поймала - то выполнение останавливается.

# Место где возникло исключение, сохраняется в аттрибуте __traceback__ обьекта исключения

