# -*- coding: utf-8 -*-

#
# 15.04 Работа с табличными данными (CSV)
#

# Очень много данных, которыми обмениваются люди и компьютеры - табличные. Начиная с шумеров.
# Сейчас в офисах один из рабочих инструментов - эксель или его аналоги (OpenOffice, LibreOffice, etc)
# Эти данные можно и нужно обрабатывать с помощью python. Как?

# Процесс работы с табличными данным похож в Питоне на работу со списками.
# И если мы очень захотим, мы сможем создать "таблицу" с помощью списка из списков
import pprint
Indiana_Jones_stash = [['Name', 'year of discovery', 'quantity'],
                       ['Ark of the covenant', '1936', 1],
                       ['Crystal skull', '1957', 1]]
pprint.pprint(Indiana_Jones_stash)


###
# Формат CSV == Comma-Separated Values
# - строки делятся переносом строки
# - ячейки делятся запятыми
# - если ячейка содержит запятую или перенос строки, ячейка обрамяляется кавычками
# - если внутри системных кавычек есть кавычки, они пишутся в виде двойных кавычек

# Формат простой и поддерживается многими системами программами по работе с таблицами.


###
# Библиотека csv

import csv

# csv.reader() - этот метод создат объект, из которого мы сможем построчно извлечь всю информацию из таблицы.

inventory_of_stash = []

with open('external_data/Indiana_stash.csv', 'r', newline='') as csv_file:
    csv_data = csv.reader(csv_file)  # <_csv.reader object at 0x01CCFD30>
    for row in csv_data:
        inventory_of_stash.append(row)

print(f'Вся информация о таблице: {inventory_of_stash}')

# csv.writer() - метод для создания (или дополнения) csv файла

new_artifact_for_stash = ['Sacred Lingam', '1935', '1']

with open('external_data/Indiana_stash.csv', 'a', newline='') as out_csv:
    writer = csv.writer(out_csv)  # <_csv.writer object at 0x03B0AD80>
    writer.writerow(new_artifact_for_stash)

# Классы DictReader и DictWriter:
# Эти два класса позволяют нам использовать особенности Пайтоновских словарей,
# для того, чтобы получить доступ к столбцам наших таблиц, по их заголовкам:
# Зачем? Зачастую нам не нужна вся таблица. Нам нужна какая-то определенная часть информации из неё
# Допустим нам понадобится перечень артефактов из тайника Индианы:

list_of_artifacts = []

with open('external_data/Indiana_stash.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')  # <csv.DictReader object at 0x03B11030>
    for row in reader:
        name_of_item_from_the_stash = row['Name']
        list_of_artifacts.append(name_of_item_from_the_stash)

print(f'В тайнике Индианы Джонса хранятся: {list_of_artifacts}')

# DictWriter соответственно выполняет запись в файл,
# но уже при помощь структуры словарей пайтона

one_more_artifact = {'Name': 'the Golden cross of Coronado', 'year of discovery': '1912', 'quantity': '1'}

with open('external_data/Indiana_stash.csv', "a", newline='') as out_file:
    writer = csv.DictWriter(out_file, delimiter=',', fieldnames=inventory_of_stash[0])
    writer.writerow(one_more_artifact)

# Что же будет, если ключи словаря на запись,
# будут отличны от ключей, заданных аргументом fieldnames?

artifact_with_wrong_keys = {'name': 'the Golden cross of Coronado', 'year_of_discovery': '1912', 'Quantity': '1'}

with open('external_data/Indiana_stash.csv', "a", newline='') as out_file:
    writer = csv.DictWriter(out_file, delimiter=',', fieldnames=inventory_of_stash[0])
    try:
        writer.writerow(artifact_with_wrong_keys)
    except ValueError:
        print(f'В этом случается Пайтон выдает ошибку ValueError с перечнем ключей, в которых была ошибка')


# Тонкости:

# Если при открытии файла не указать параметр newline, то модуль CSV, обрабатывая строки,
# может неверно интерпретировать символы новых строк, расположенных внутри кавычек

# По умолчанию, декодирование происходит в unicode.
# Но! Если файл приходит из вне, могут возникнуть конфликты, приводящие к потере информации.
# Чтобы рещить подобный конфликт, необходимо явно указать тип кодировки с помощью парамтра encoding

with open('external_data/Indiana_stash.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file)  # <_csv.reader object at 0x01CCFD30>
    for row in csv_data:
        print(row)


# Помимо настроек, связанных с открытием файла, есть так же параметры
# связанные непосредственно с чтением и записью CSV-файлов.
# Так, в примерах выше, мы явно указывали тип разделителя для полей (delimiter=',')
# Подобные параметры, определяют правила, по которым будет считана или записана
# информация CSV файла.

# Чтобы не настраивать каждый раз все параметры вручную, они были сгруппированы
# в объекты класса диалект.

print(f'По умолчанию доступны следующие диалекты {csv.list_dialects()}')

# Но настроив все параметры вручную, можно создать и свой собственный диалект.
# подробнее об этом можно прочитать здесь:
# https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters

# Что же делать, если извне вы получаете файл, но заранее не знаете
# какие параметры диалекта в нём использовались?
# Эту проблему решит класс csv.Sniffer()
# Его метод sniff() позволяет по примеру строки
# восстановить параметры используемого диалекта:

with open('external_data/Indiana_stash.csv', 'rb') as csvfile:
    dialect = csv.Sniffer().sniff(str(csvfile.readline()), [',', ';'])
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    print(dialect)  # <class 'csv.Sniffer.sniff.<locals>.dialect'>
    print(reader)  # <_csv.reader object at 0x018CFD30>

# Передав найденные параметры класс reader,
# мы с его помощью сможем корректно прочесть информацию из файла.

# Пример:
# Индиана, собираясь в очередное приключение должен отправить в бухгалтерию
# своего университета данные о закупках инструментов к предстоящей археологической экспедиции.
# За основу он взял стандартный перечень инструментов:

standart_need_list = []

with open('external_data/Tools for archaeological excavations.csv', 'r', newline='') as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        standart_need_list.append(row)

print(f'Стандартный набор инструментов: {standart_need_list}')

# Но в силу специфичности миссии, ему нужно было отредактировать таблицу.
# И отредактировать именно в Пайтоне:

Indiana_need_list = [{'Name:': 'Whip', 'Price:': '100', 'Quantity:': '1'},
                     {'Name:': 'Hat', 'Price:': '200', 'Quantity:': '2'},
                     {'Name:': 'Revolver', 'Price:': '400', 'Quantity:': '1'}]

with open('external_data/Tools for archaeological excavations.csv', 'w', newline='') as out_csv:
    writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=standart_need_list[0])
    writer.writeheader()
    writer.writerows(Indiana_need_list)


# Ещё немного о CSV и Data Science.

# Формат CSV очень популярен в Data Science, тк в нём можно хранить большое количество
# упорядоченных данных, причём порядок будет указывать на тот или иной
# признак объекта.
# Так, если третьий столбец помечен как "Цвет",
# то каждая третья цифра списка будет означать тот или иной цвет объекта.

# Пример:
# В файле houses.csv записаны подробные данные о домах.
# Файл используется в официальном соревновании по прогнозированию стоимости дома с помощью нейронных сетей.

# Для примера возьмём признак, в котором записаны улица домов:
steets_of_houses = []

with open('external_data/houses.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        house_street = row['Street']
        steets_of_houses.append(house_street)

print(f'В итоге мы получим список улиц всех домов из таблицы: {steets_of_houses[:3]}')

# Формат же CSV гораздо более гибкий, чем это может показаться.
# Зачастую в таблицах можно даже хранить изображения.
# Такие таблицы обычно отличаются своим весом, так как в ширину распологается информация о каждом пикселе картинки.
# Так небольшая картинка 28х28, будет занимать в таблице 784 столбца.
# Заголовки же будут соответствовать номеру пикселя в картинке.

# Для работ такого типа, зачастую пользуются очень популярной библиотекой pandas
# С её помощью можно точно выделить нужные столбцы и строки, по именам, или по номерам
# И передать эту информацию дальше, формируя из данных матрицы, которые так любит компьютер.
