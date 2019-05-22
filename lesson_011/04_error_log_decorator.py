# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


# def log_errors(func):
#     log_name = 'function_errors.log'
#
#     def func_fact(*args, **kwargs):
#         try:
#             res = func(*args, **kwargs)
#             return res
#         except (ZeroDivisionError, ValueError) as exc:
#
#             param = []
#             param.extend([arg for arg in args])
#             param.extend([f'{key}={value}' for key, value in kwargs.items()])
#
#             with open(file=log_name, mode='a', encoding='utf8') as file:
#                 file.write(f'{func.__name__:<15} {param.__str__():<40} {exc.__class__.__name__:<20} {str(exc):<10}\n')
#             raise exc
#
#     return func_fact


# TODO Имена аргументов функции должны отражать их назнчение и иметь
# TODO говорящие название.
def log_errors(fn=None):
    def func_decoration(func):
        # TODO Проще будет у аргумента fn указать значение по умолчанию не
        # TODO None, а 'function_errors.log'. Тогда это условие не нужно будет.
        if fn:
            log_name = fn
        else:
            log_name = 'function_errors.log'

        def logging(*args, **kwargs):
            try:
                # TODO Не нужно сохранять значение во временную переменную,
                # TODO если значение ни как не обрабатывается.
                res = func(*args, **kwargs)
                return res
            except (ZeroDivisionError, ValueError) as exc:

                param = []
                param.extend([arg for arg in args])
                param.extend([f'{key}={value}' for key, value in kwargs.items()])

                with open(file=log_name, mode='a', encoding='utf8') as file:
                    # TODO Длинна строки не должна превышать 120 символов, а в
                    # TODO идеале 79 символов
                    file.write(f'{func.__name__:<15} {param.__str__():<40} {exc.__class__.__name__:<20} {str(exc):<10}\n')
                # TODO В данном случае можно написать просто raise и тогда
                # TODO будет снова выброшено перехваченое исключение
                raise exc
        return logging
    return func_decoration


# Проверить работу на следующих функциях
@log_errors()
def perky(param):
    return param / 0


@log_errors(fn='function_errors2.log')
def perky_with_fn(param):
    return param / 0


@log_errors()
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

try:
    perky(param=42)
except Exception as exc:
    print(exc)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла

try:
    perky_with_fn(param=55)
except Exception as exc:
    print(exc)
