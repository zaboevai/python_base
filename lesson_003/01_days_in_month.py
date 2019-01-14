# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

user_input = input("Введите, пожалуйста, номер месяца: ")
if user_input.isdigit():
    # TODO Если пользователь введет букву вся программа сразу сломается, это не хорошо
    month = int(user_input)

    if 1 <= month <= 12:
        # TODO Для того, чтобы не писать такое огромное количество условий
        # TODO можно воспользоваться словарем дня хранения информации о том сколько днгей в месяце
        if month == 1:
            date_count = 31
            date_count
        elif month == 2:
            date_count = 28
        elif month == 3:
            date_count = 31
        elif month == 4:
            date_count = 30
        elif month == 5:
            date_count = 31
        elif month == 6:
            date_count = 30
        elif month == 7:
            date_count = 31
        elif month == 8:
            date_count = 31
        elif month == 9:
            date_count = 30
        elif month == 10:
            date_count = 31
        elif month == 11:
            date_count = 30
        elif month == 12:
            date_count = 31

        print('Вы ввели', month)
        print('Кол-во дней в месяце:', date_count)

    else:
        print('Месяца с таким номер не существует.')
else:
    print('Необходимо ввести число.')
