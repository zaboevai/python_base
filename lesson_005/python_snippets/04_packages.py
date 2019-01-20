# -*- coding: utf-8 -*-

# Пакеты — способ структурирования пространств имён (namespaces) модулей Python
# за счёт использования имён модулей, разделённых точками („dotted module names“).

# Пакет - это по сути папка файловой системы, в которой есть __init__.py
# Все пайтон модули в папке относятся к пакету

# рассмотрим package_1
from package_1 import module_1
module_1.function1()

from package_1.module_1 import function1
function1()

import package_1.module_1
package_1.module_1.function1()  # тут нужно полное имя модуля

# подпакеты
from package_1.subpackage import module_2
module_2.function2()

from package_1.subpackage.module_2 import function2
function2()

import package_1.subpackage.module_2
package_1.subpackage.module_2.function2()

import package_1
package_1.subpackage.module_2.function2()

from package_1.subpackage import module_2
module_2.function2()


###
# наиболее общеупотребительные способы
from package_1.module_1 import function1
from package_1.subpackage import module_2

###
# Если есть код в __init__.py, то он импортируется напрямую
from package_1 import function3
function3()
# но обычно __init__.py или пустой, или содержит код инициализации пакета

###
# Внутри модулей пакета можно делать т.н. относительные импорты (см package_1.module_3)
from package_1.module_3 import function4
function4()

# см package_1.subpackage.module_4
from package_1.subpackage.module_4 import function5
function5()


###
# Вот пример большой библиотеки - пакет фреймворка Django (немного урезанный, только пакеты)
# .
# ├── apps
# ├── core
# │   ├── cache
# │   │   └── backends
# │   ├── checks
# │   │   ├── compatibility
# │   │   └── security
# │   ├── files
# │   ├── handlers
# │   ├── mail
# │   │   └── backends
# │   ├── management
# │   │   └── commands
# │   ├── serializers
# │   └── servers
# ├── db
# │   ├── backends
# │   │   ├── base
# │   │   ├── dummy
# │   │   ├── mysql
# │   │   ├── oracle
# │   │   ├── postgresql
# │   │   ├── postgresql_psycopg2
# │   │   └── sqlite3
# │   ├── migrations
# │   │   └── operations
# │   └── models
# │       ├── fields
# │       ├── functions
# │       └── sql
# ├── dispatch
# ├── forms
# │   └── extras
# ├── http
# ├── middleware
# ├── template
# │   ├── backends
# │   └── loaders
# ├── templatetags
# ├── test
# ├── urls
# ├── utils
# │   └── translation
# └── views
# ├── decorators
# └── generic

# пример использования
from django.db.models import Manager
from django.urls import reverse