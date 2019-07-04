# -*- coding: utf-8 -*-


# Зачастую в проектах необходимо бывает использовать не только разные версии библиотек,
# но и разные версии пайтона. Пример: есть задача сделать сайт, у заказчика на сервере
# стоит версия 3.5.2 и обновлять он её не хочет.
# Поэтому разработчику надо уметь работать с несколькими версиями интерпретатора
#
# Хорошая новость в том, что пайтон можно устанавливать в отдельные директории.
#
# Под windows это делается так: находите нужную версию тут https://www.python.org/downloads/windows/
# (пусть это будет 3.6.1 для примера), скачиваете инсталлятор и через Custom указываете директорию
# C:\Python361 - важно что бы она была уникальная. Ну и добавлять в PATH не надо.
#
# Под linux и macos есть такой замечательный проект - pyenv - https://github.com/pyenv/pyenv
# это набор утилит, который позволяет установить любую версию автоматически.
#
# Для linux - открываем консоль и делаем по инструкции (https://github.com/pyenv/pyenv):
#   git clone https://github.com/pyenv/pyenv.git ~/.pyenv
# клонируется в папку .pyenv в домашней директории
#   $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
#   $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
#   $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
# я заменил bash_profile на bashrc - особенности Linux Mint
# и установим все пакеты ОС, необходимые для сборки пайтона (https://github.com/pyenv/pyenv/wiki)
#   $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev
#   $ sudo apt-get install -y libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev
#   $ sudo apt-get install -y libxmlsec1-dev libffi-dev
# далее перегружаем консоль и вводим команды pyenv
#   $ pyenv versions
#   $ pyenv install 3.6.1
# pyenv скачивает исходники и компилит нужную версию пайтона. Располагаться она будет в
#   $ ls -al ~/.pyenv/versions
#
# Для macos сначала нужно установить Homebrew - https://brew.sh/index_ru
# Это "Недостающий менеджер пакетов для macOS", как написано в описании :)
#   $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# Через него можно установить и python3, но только последней версии.
# Но мы установим pyenv
#   $ brew install pyenv
# Далее вводим команды pyenv
#   $ pyenv versions
#   $ pyenv install 3.6.1
# pyenv скачивает исходники и компилит нужную версию пайтона. Располагаться она будет в
#   $ ls -al ~/.venv/versions
#
# Теперь, независимо от ОС, можно использовать разные версии пайтона в PyCharm.
# В PyCharm смотрим появлась ли новая версия, если нет - добавляем руками.
# Ну и впоследствии можно создавать виртуальное окружение на основе установленной версии пайтона.
#
# Теперь вы готовы к любым проектам :)
