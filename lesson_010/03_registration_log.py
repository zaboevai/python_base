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


def check_line_log(line):
    name, email, age = line.split(' ')
    print(line, '1' if name and email and age else '0')
    # TODO В данной проверке нет необходимости, потому если строка не будет
    # TODO содержать всех необходимых данных, то интерпретатор сам возбудит
    # TODO исключение в строке 36
    if name and email and age:
        # TODO Проверки лучше вынесли в отдельные функции
        if name.isalpha():
            if '@' in email and '.' in email:
                if 10 <= int(age) <= 99:
                    return f'{name:<10} {email:<30} {age}\n'
                else:
                    raise ValueError('поле возраст НЕ является числом от 10 до 99')
            else:
                raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')
        else:
            raise NotNameError('поле имени содержит НЕ только буквы')
    else:
        raise ValueError('НЕ присутсвуют все три поля')


with open('registrations.txt', mode='r', encoding='utf8') as file:
    with open('registrations_good.log', mode='w', encoding='utf8') as good_log:
        with open('registrations_bad.log', mode='w', encoding='utf8') as bad_log:
            for file_line in file:
                line_cont += 1
                line = file_line[:-1].strip()
                try:
                    good_line = check_line_log(line)
                    good_log.write(good_line)
                # TODO Обработка всех исключений практически идентична, лучше
                # TODO будет в одном except перехватывать несколько исключений
                except ValueError as exc:
                    if 'unpack' in exc.args[0]:
                        bad_log.write(f'{line_cont:<5} {line:<40} НЕ присутсвуют все три поля\n')
                    else:
                        bad_log.write(f'{line_cont:<5} {line:<40} {exc}\n')
                except NotEmailError as exc:
                    bad_log.write(f'{line_cont:<5} {line:<40} {exc}\n')
                except NotNameError as exc:
                    bad_log.write(f'{line_cont:<5} {line:<40} {exc}\n')
