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

FONT = 'ofont.ru_Franklin Gothic Medium Cond.ttf'
TEMPLATE_TICKET = 'ticket_template.png'

PARENT_PATH = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FONT_DIR = os.path.join(PARENT_PATH, 'font', FONT)
DEFAULT_TEMPLATE_PATH = os.path.join(PARENT_PATH, 'images', TEMPLATE_TICKET)

COLOR_WHITE = ImageColor.getrgb('white')
COLOR_BLACK = ImageColor.getrgb('black')

FIO_COORD = (45, 130)
FLY_FROM_COORD = (45, 200)
FLY_TO_COORD = (45, 265)
DATE_COORD = (285, 265)


def clear_template(draw: ImageDraw):
    draw.rectangle([FIO_COORD, (250, 160)], fill=COLOR_WHITE, width=1)
    draw.rectangle([FLY_FROM_COORD, (250, 230)], fill=COLOR_WHITE, width=1)
    draw.rectangle([FLY_TO_COORD, (350, 295)], fill=COLOR_WHITE, width=1)


def draw_text(draw, fio, from_, to_, date, ):
    font = ImageFont.truetype(font=DEFAULT_FONT_DIR, size=18, )
    draw.text(xy=FIO_COORD, text=fio, fill=COLOR_BLACK, font=font)
    draw.text(xy=FLY_FROM_COORD, text=from_, fill=COLOR_BLACK, font=font)
    draw.text(xy=FLY_TO_COORD, text=to_, fill=COLOR_BLACK, font=font)
    draw.text(xy=DATE_COORD, text=date, fill=COLOR_BLACK, font=font)


# Здесь тогда тоже поменяем
def make_dir(save_to: str):
    if not os.path.exists(save_to):
        try:
            os.mkdir(save_to)
        except PermissionError:
            print('ОШИБКА: Нет прав на запись!')
            raise PermissionError


def make_ticket(fio=None, from_=None, to_=None, date=None, save_to=None):
    fio, from_, to_, date = [arg.upper() for arg in (fio, from_, to_, date)]
    img = Image.open(DEFAULT_TEMPLATE_PATH)
    draw = ImageDraw.Draw(im=img)

    clear_template(draw)
    draw_text(draw, fio, from_, to_, date, )
    if not save_to:
        save_to = os.path.join(PARENT_PATH, 'result')
    make_dir(save_to)
    ticket_path = os.path.join(save_to, f'{fio}.png')

    img.save(ticket_path, 'PNG')
    print(f'Билет успешно создан в каталоге "{ticket_path}"')


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
    parser.add_argument('-save_to', '--save_to',
                        type=str,
                        default='',
                        help='Куда разместить билет (default: "<current_dir>/result")')
    args = parser.parse_args()

    if args:
        make_ticket(fio=args.fio,
                    from_=args.from_,
                    to_=args.to_,
                    date=args.date,
                    save_to=args.save_to)

# зачет!
