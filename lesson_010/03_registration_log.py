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

from os import path


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class FileNotFound(Exception):
    pass


class EmailRegistrationLog:

    def __init__(self, path_to_log, path_to_parsed_log, path_to_error_log=None):

        if path_to_log and path.isfile(path_to_log):
            self.path_log = path_to_log
            self.log_file = None
        else:
            raise FileNotFound('Файл лога не укзан !')

        if path_to_parsed_log:
            self.path_to_parsed_log = path_to_parsed_log
            self.parsed_file = None
        else:
            raise FileNotFound('Файл для выгрузки результата не указан !')

        self.path_to_error_log = path_to_error_log
        self.errors_file = None
        self.line_cont = 0

    def check_name(self, name):
        if not name.isalpha():
            raise NotNameError('поле имени содержит НЕ только буквы')

    def is_email(self, email):
        if not '@' in email and '.' in email:
            raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')

    def check_age_limit(self, age):
        if age.isdigit() and not 10 <= int(age) <= 99:
            raise ValueError('поле возраст НЕ является числом от 10 до 99')

    def check_line_log(self, line):
        name, email, age = line.split(' ')
        self.check_name(name)
        self.is_email(email)
        self.check_age_limit(age)
        return f'{name:<10} {email:<30} {age}\n'

    def file_init(self):
        self.log_file = open(self.path_log, mode='r', encoding='utf8')
        self.parsed_file = open(self.path_to_parsed_log, mode='w', encoding='utf8')
        self.errors_file = open(self.path_to_error_log, mode='w', encoding='utf8') if self.path_to_error_log else None

    def file_close(self):
        self.log_file.close()
        self.parsed_file.close()
        self.errors_file.close() if self.errors_file else None

    def parse(self):
        self.file_init()
        for line in self.log_file:
            try:
                self.line_cont += 1
                line = line[:-1].strip()
                good_line = self.check_line_log(line)
                self.parsed_file.write(good_line)
            except Exception as exc:
                if self.path_to_error_log:
                    if 'unpack' in exc.args[0]:
                        self.errors_file.write(f'{self.line_cont:<5} {line:<40} НЕ присутсвуют все три поля\n')
                    else:
                        self.errors_file.write(f'{self.line_cont:<5} {line:<40} {exc} {exc.args}\n')
        self.file_close()


if __name__ == '__main__':

    log_path = 'registrations.txt'
    parsed_log_path = 'registrations_good.log'
    error_log_path = 'registrations_bad.log'

    try:
        log = EmailRegistrationLog(path_to_log=log_path,
                                   path_to_parsed_log=parsed_log_path,
                                   path_to_error_log=error_log_path,
                                   )
        log.parse()
    except FileNotFound as exc:
        print(exc)
