# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

COLOR_WHITE = ImageColor.getrgb('white')
COLOR_BLACK = ImageColor.getrgb('black')
PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FONT = os.path.join(PARENT_DIR, 'font', 'ofont.ru_Franklin Gothic Medium Cond.ttf')

FIO_COORD = (45, 130)
FLY_FROM_COORD = (45, 200)
FLY_TO_COORD = (45, 265)
DATE_COORD = (285, 265)


def prepare_template(draw: ImageDraw):
    draw.rectangle([FIO_COORD, (250, 160)], fill=COLOR_WHITE, width=1)
    draw.rectangle([FLY_FROM_COORD, (250, 230)], fill=COLOR_WHITE, width=1)
    draw.rectangle([FLY_TO_COORD, (350, 295)], fill=COLOR_WHITE, width=1)


def make_ticket(fio=None, from_=None, to_=None, date=None, dest=None):
    # TODO дополнить функцию проверками
    template_path = os.path.join(PARENT_DIR, 'images', 'ticket_template.png')

    img = Image.open(template_path)
    draw = ImageDraw.Draw(im=img)

    prepare_template(draw)

    font = ImageFont.truetype(font=DEFAULT_FONT, size=18, )
    fio = fio.upper()
    from_ = from_.upper()
    to = to_.upper()
    date = date.upper()

    draw.text(xy=FIO_COORD, text=fio, fill=COLOR_BLACK, font=font)
    draw.text(xy=FLY_FROM_COORD, text=from_, fill=COLOR_BLACK, font=font)
    draw.text(xy=FLY_TO_COORD, text=to, fill=COLOR_BLACK, font=font)
    draw.text(xy=DATE_COORD, text=date, fill=COLOR_BLACK, font=font)

    if dest and not os.path.exists(dest):
        try:
            os.mkdir(os.path.join(dest))
            dest_path = os.path.join(dest, 'test1.png')
        except PermissionError:
            print('ОШИБКА: Нет прав на запись!')
            return False

    else:
        dest_path = os.path.join(PARENT_DIR, dest, 'test1.png')

    print(dest_path)
    img.save(dest_path, 'PNG')
    print(f'Создан билет на основе макета в каталоге {dest_path}')
    return True

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Утилита для формирования АВИА билета перевозчика "SKILLBOX AIRLINE".',
                                     add_help=True)

    parser.add_argument('fio', type=str, help='ФИО')
    parser.add_argument('from_', type=str, help='Откуда')
    parser.add_argument('to_', type=str, help='Куда')
    parser.add_argument('date', type=str, help='Дата вылета')
    parser.add_argument('-dst', '--destination', type=str, default='', help='Путь к заполненному файлу (default: '')')
    args = parser.parse_args()
    print(args, args.destination)

    if args:
        make_ticket(args.fio, args.from_, args.to_, args.date, args.destination)

# make_ticket(fio='Забоев Андрей Игоревич', from_='Киров', to_='Сочи', date='04.07')
