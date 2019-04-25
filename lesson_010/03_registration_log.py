# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
line_cont = 0


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def is_email(email):
    return '@' in email and '.' in email


def check_age_limit(age):
    return 10 <= int(age) <= 99


def check_line_log(line):
    name, email, age = line.split(' ')

    # TODO Все 3 проверки должны быть вынесены в отдельные функции. Если данные
    # TODO корректны функции ничего не возвращают и просто завершают свою
    # TODO работу, а если данные ошибочны то выбрасывают исключение. Таким
    # TODO образом количество кода сильно сократится и не нужны будут условия.
    if name.isalpha():
        if is_email(email):
            if check_age_limit(age):
                return f'{name:<10} {email:<30} {age}\n'
            else:
                raise ValueError('поле возраст НЕ является числом от 10 до 99')
        else:
            raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')
    else:
        raise NotNameError('поле имени содержит НЕ только буквы')


log_path = 'registrations.txt'
bad_log_path = 'registrations_bad.log'
good_log_path = 'registrations_good.log'

with open(log_path, mode='r', encoding='utf8') as file:
    with open(good_log_path, mode='w', encoding='utf8') as good_log:
        with open(bad_log_path, mode='w', encoding='utf8') as bad_log:
            for file_line in file:
                line_cont += 1
                line = file_line[:-1].strip()
                try:
                    good_line = check_line_log(line)
                # TODO Необходимо перезватывать Exception, а не BaseException
                except BaseException as exc:
                    if 'unpack' in exc.args[0]:
                        bad_log.write(f'{line_cont:<5} {line:<40} НЕ присутсвуют все три поля\n')
                    else:
                        bad_log.write(f'{line_cont:<5} {line:<40} {exc}\n')
                else:
                    good_log.write(good_line)
