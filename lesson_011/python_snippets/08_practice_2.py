# -*- coding: utf-8 -*-

# Решим задачу прошлой практики с помощью функционального подхода
#
# Есть файл calc.txt с записями операций - текстовый калькулятор. Записи вида
#
# 100 + 34
# 23 / 4
#
# то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделенные пробелами.
# Операндны - целые числа. Операции - арифметические, целочисленное деление и остаток от деления.
#
# Нужно вычислить все операции и найти сумму их результата.

ops = {
    '*': lambda x, y: x + y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '//': lambda x, y: x // y,
    '%': lambda x, y: x % y,
}


def calc(line):
    # print(eval(line))  # https://habr.com/post/221937/
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation in ops:
        func = ops[operation]
        value = func(operand_1,  operand_2)
    else:
        raise ValueError('Unknown operation {operation}')
    return value


def get_lines(file_name):
    with open(file_name, 'r') as ff:
        for line in ff:
            if not line:
                continue
            line = line[:-1]
            yield line


total = 0
for line in get_lines(file_name='calc.txt'):
    try:
        total += calc(line)
    except ValueError as exc:
        if 'unpack' in exc.args[0]:
            print(f'Не хватает операндов {exc} в строке {line}')
        else:
            print(f'Не могу преобразовать к целому {exc} в строке {line}')

print(f'Total {total}')

