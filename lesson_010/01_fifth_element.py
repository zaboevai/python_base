# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
input_data = None

try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError as exc:
    print(f'Введено: <{input_data}> - Невозможно преобразовать к числу ({exc}).')
except IndexError as exc:
    print(f'Введено: <{input_data}> - Выход за границы списка ({exc}).')
except Exception:
    print(f'Введено: <{input_data}> - Непредвиденная ошибка.')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




