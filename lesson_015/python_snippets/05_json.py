# -*- coding: utf-8 -*-

#
# 15.05 JSON
#

# Данные могут поступать к нам не только в табличном виде, а в некоем "структурированном" виде.
# Бинарные форматы - в каждом конкретном случае нужна своя библа. Текстовые форматы более универсальны,
# они могут читаться и человеком и машиной. Примеры таких форматов - JSON, YML, XML
# В веб приложениях особо популярен JSON, его и рассмотрим.

# JSON (или JavaScript Object Notation) был создан в JavaScript, но несмотря на это
# он является полностью независимым и универсален.
# Как правило любой современный язык программирования поддерживает этот формат в той или иной форме,
# что позволяет использовать JSON для обмена данными между разными яп.

# Формат JSON по своей сути напоминает dict, так как
# зачастую он представляет собой набор пар "ключ:значение":
# {
#   "FirstName":"Dominick"
#   "LastName":"Cobb"
# }
#
# И если формат CSV удобен для хранения больших, но простых массивов данных,
# то JSON удобнее использовать для хранения сложных структур данных.
# Создавать сложные иерархии позволяет тот факт, что в роли "значения",
# могут выступать:
# -- object (аналог словаря - dict в пайтоне)
# -- array (аналог списка - list)
# -- string (str)
# -- number (int,long,float)
# -- true/false (True/False)
# -- null (None)

# Используя object, мы можем добавлять уровни вложенности:
# {
#   "FirstName": "Dominick",
#   "LastName": "Cobb",
#   "Address": {
#       "city": "Los Angeles",
#       "StreetAdress": "S Olive st 617",
#   },
#   "ContactDetails": {
#       "PhoneNumbers": ["+1 212-626-8118", "+1 212-484-4554"],
#       "E-mail": "inception@nolan.genii",
#   }
# }

#   json.dump / json.load
#   json.dumps / json.loads
#   тонкости кодировок и представлений

# Как же Пайтон поддержимает JSON?
# Для работы с JSON существует встроенный модуль:
import json

# Когда речь заходит о работе с JSON,
# вы можете столкнуться со словами
# сериализация/десериализация.
# Процесс сериализации означает трансформацию данных в байты,
# Десериализация соответственно обратный процесс - декодирование данных.
# То есть по сути мы говорим о привычных нам чтении и записи.

# Сериализация (запись):
data = {
   "FirstName": "Dominick",
   "LastName": "Cobb",
   "Adress": {
       "city": "Los Angeles",
       "StreetAdress": "S Olive st 617",
   },
   "ContactDetails": {
       "PhoneNumbers": ["+1 212-626-8118", "+1 212-484-4554"],
       "E-mail": "inception@nolan.genii",
   }
}

# Запись в файл:
with open("external_data/Dom.json", "w") as write_file:
    json.dump(data, write_file)

# Запись в переменную:
json_data = json.dumps(data)
print(f'Словарь будет преобразован в формат JSON в виде строки: {json_data}')  # <class 'str'>
# Данный метод имеет несколько интересных параметров:

# Один из них indent, отвечающий за отсутпы:
json_data_with_indent = json.dumps(data, indent=4)
print(f'Та же строка, но уже с отступами, в удобном виде: {json_data_with_indent}')
with open("external_data/Dom#2.json", "w") as file:
    file.write(json_data)

# Другой sort_keys, который позволяет отсортировать словарь по именам ключей,
# что в некоторых случаях тоже бывает полезно:
json_data_sorted = json.dumps(data, indent=4, sort_keys=True)
print(f'В результате ключи будут отсортированы: {json_data_sorted}')

# Десериализация (чтение):

# Чтение из файла:
with open("external_data/Dom#2.json", "r") as read_file:
    loaded_json_file = json.load(read_file)
print(f'В итоге строка, которую мы загрузили в файл Dom#2, превратилась обратно в словарь: {loaded_json_file}')
print(f'И мы можем получить доступ к нужному полю: {loaded_json_file["FirstName"]}')
print(f'Или к более сложному полю: {loaded_json_file["Adress"]["city"]}')

# Чтение из переменной:
loaded_json_str = json.loads(json_data)
print(f'Строка превращается обратно в словарь: {loaded_json_str}')  # <class 'dict'>

# Пример:
# С открытого внешнего API поступает список,
# хранящий информацию о задачах, назначенных юзерам.
# Нужно обработать список и узнать, сколько в этом наборе уникальных пользователей
# и сколько у каждого пользователя оригинальных задач и сполько из них выполнено.

with open("external_data/json_todos.json", "r") as json_file:
    list_of_tasks = json.load(json_file)
number_of_tasks = len(list_of_tasks)
print(f'Пример записи: {list_of_tasks[0]}')

# Задача 1:
# Определить количесвто уникальных пользователей.

unique_set_of_users = set()
for number in range(number_of_tasks):
    unique_set_of_users.add(list_of_tasks[number]["userId"])
print(f'Количество уникальных пользователей: {len(unique_set_of_users)}')

# Задача 2:
# Опреедлить количество задач и количество выполненных задач для каждого пользователя

users = {}
for task in range(number_of_tasks):
    users[list_of_tasks[task]["userId"]] = {"num": 0, "completed": 0}

for task_number in range(number_of_tasks):
    users[list_of_tasks[task_number]["userId"]]["num"] += 1
    if list_of_tasks[task_number]["completed"] is True:
        users[list_of_tasks[task_number]["userId"]]["completed"] += 1

print(f'У пользователя под номером 1 всего {users[1]["num"]} задач, из них {users[1]["completed"]} уже выполнено')

# Задача 3:
# Записать полученный список задач в файл

with open("external_data/json_todos_formatted.json", "w") as json_file:
    json.dump(users, json_file)


###
# Помимо JSON существует ещё несколько форматов для обмена данными:
# Один из них XML
# ли eXtensible Markup Language, что в переводе значит «расширенный язык разметки»

# Формат XML представляет собой данные, обрамленные тегом, состоящим из открывающих и закрывающих элементов
# <имя> данные </имя>
# Такое объединение само по себе способно быть представленным в поле данных, что позволяет нам строить иерархию.
#
# <имя>
#   <другое имя> данные </другое имя>
# </имя>

# Пример работы с XML:
#
# <data>
#  <name>Petya</name>
#  <age>23</age>
#  <sex>true</sex>
#  <languages>
#   <language name="Python">9</language>
#   <language name="Java">7</language>
#   <language name="C#">8</language>
#  </languages>
#   <pc>
#     <pc_item name="os">Linux</pc_item>
#     <pc_item name="proc">Intel Core i7-8700</pc_item>
#     <pc_item name="ram">64</pc_item>
#     <pc_item name="hard">5000</pc_item>
#   </pc>
# </data>

import xml.etree.ElementTree as ETree

# Первым делом нужно распарсить имеющийся документ
developers_cv = ETree.parse('external_data/demo.xml')
# Найти корень
root_of_developers_cv = developers_cv.getroot()

print(f'Название корневого тэга: {root_of_developers_cv.tag}, а вот текста в нём нет {root_of_developers_cv.text}')

print(f'Следующий элемент, название тэга {root_of_developers_cv[0].tag}, текст внутри: {root_of_developers_cv[0].text}')

# Узнаем какими языками владеет Пётр:

skills = []

for langs in root_of_developers_cv[3]:
    skills.append(langs.attrib['name'])

print(f'Петр владеет следующими яп: {skills}')


###
# Ещё один из схожих форматов - YAML
# Сперва он носил название: Yet Another Markup Language
# И позиционировался как конкурент XML
# Однако позже название изменили на «YAML Ain't Markup Language»
# Так они пытались сказать, что они меньше внимания уделяют разметке, а больше самим данным
# Что и отражается в его структуре, читать которую можно интуитивно:
# -  martin:
#     name: Martin D'vloper
#     job: Developer
#     skills:
#       - python
#       - perl
#       - pascal
# -  tabitha:
#     name: Tabitha Bitumen
#     job: Developer
#     skills:
#       - lisp
#       - fortran
#       - erlang

# pip install pyyaml
import yaml

with open("external_data/yaml_example.yaml", "r") as yaml_file:
    martins_resume_in = yaml.load(yaml_file, Loader=yaml.FullLoader)

print(f'Полученное резюме в формате Yaml мы превратили в словарь Пайтона: {martins_resume_in}')  # <class 'dict'>

martins_resume_out = yaml.dump(martins_resume_in)
# Обратная операция восстановила структуру, превратив словарь в строку, соответствующую формату YAML:
print(martins_resume_out)  # <class 'str'>
