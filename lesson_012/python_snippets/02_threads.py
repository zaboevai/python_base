# -*- coding: utf-8 -*-

# Как создать и запустить поток
import random
import time
from collections import defaultdict
from threading import Thread

FISH = (None, 'плотва', 'окунь', 'лещ')


# Определим функцию, эмулирующую рыбалку
def fishing(name, worms):
    catch = defaultdict(int)
    for worm in range(worms):
        print(f'{name}: Червяк № {worm} - Забросил, ждем...', flush=True)
        _ = 3 ** (random.randint(50, 70) * 10000)
        fish = random.choice(FISH)
        if fish is None:
            print(f'{name}: Тьфу, сожрали червяка...', flush=True)
        else:
            print(f'{name}: Ага, у меня {fish}', flush=True)
            catch[fish] += 1
    print(f'Итого рыбак {name} поймал:')
    for fish, count in catch.items():
        print(f'    {fish} - {count}')


fishing(name='Вася', worms=10)


# А теперь создадим второго рыбака, пошедшего на рыбалку ОДНОВРЕМЕННО с первым
thread = Thread(target=fishing, kwargs=dict(name='Вася', worms=10))
thread.start()

fishing(name='Коля', worms=10)

thread.join()


# При простой передаче функции в поток результат выполнения функции
# можно получить только через изменяемый обьект в параметрах:
def fishing(name, worms, catch):
    for worm in range(worms):
        print(f'{name}: Червяк № {worm} - Забросил, ждем...', flush=True)
        _ = 3 ** (random.randint(50, 70) * 10000)
        fish = random.choice(FISH)
        if fish is None:
            print(f'{name}: Тьфу, сожрали червяка...', flush=True)
        else:
            print(f'{name}: Ага, у меня {fish}', flush=True)
            catch[fish] += 1


vasya_catch = defaultdict(int)
thread = Thread(target=fishing, kwargs=dict(name='Вася', worms=10, catch=vasya_catch))
thread.start()

kolya_catch = defaultdict(int)
fishing(name='Коля', worms=10, catch=kolya_catch)

thread.join()
for name, catch in (('Вася', vasya_catch), ('Вася', kolya_catch)):
    print(f'Итого рыбак {name} поймал:')
    for fish, count in catch.items():
        print(f'    {fish} - {count}')


# Более удобно использовать наследование от класса потока
class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms

    def run(self):
        catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                catch[fish] += 1
        print(f'Итого рыбак {self.name} поймал:')
        for fish, count in catch.items():
            print(f'    {fish} - {count}')


vasya = Fisher(name='Вася', worms=10)
kolya = Fisher(name='Коля', worms=10)

print('.' * 20, 'Они пошли на рыбалку')

vasya.start()
kolya.start()

print('.' * 20, 'Ждем пока они вернутся...')

vasya.join()
kolya.join()

print('.' * 20, 'Итак, они вернулись')


# Если нужен результат выполнения, то просто делаем атрибут класса
class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)

    def run(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.catch[fish] += 1


vasya = Fisher(name='Вася', worms=10)
kolya = Fisher(name='Коля', worms=10)

print('.' * 20, 'Они пошли на рыбалку')

vasya.start()
kolya.start()

print('.' * 20, 'Ждем пока они вернутся...')

vasya.join()
kolya.join()

print('.' * 20, 'Итак, они вернулись')

for fisher in (vasya, kolya):
    print(f'Итого рыбак {fisher.name} поймал:')
    for fish, count in fisher.catch.items():
        print(f'    {fish} - {count}')


# Что будет если в потоке ошибка
class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)

    def run(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            dice = random.randint(1, 5)
            if self.name == 'Коля' and dice == 1:
                raise ValueError(f'{self.name}: Блин, у меня сломалась удочка на {worm} червяке :(')
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.catch[fish] += 1


vasya = Fisher(name='Вася', worms=10)
kolya = Fisher(name='Коля', worms=10)

print('.' * 20, 'Они пошли на рыбалку')

vasya.start()
kolya.start()

print('.' * 20, 'Ждем пока они вернутся...')

vasya.join()
kolya.join()

print('.' * 20, 'Итак, они вернулись')

for fisher in (vasya, kolya):
    print(f'Итого рыбак {fisher.name} поймал:')
    for fish, count in fisher.catch.items():
        print(f'    {fish} - {count}')


# Обрабатывать ошибки нужно в самом потоке
class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)

    def run(self):
        try:
            self._fishing()
        except Exception as exc:
            print(exc)

    def _fishing(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            dice = random.randint(1, 5)
            if self.name == 'Коля' and dice == 1:
                raise ValueError(f'{self.name}: Блин, у меня сломалась удочка на {worm} червяке :(')
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.catch[fish] += 1


vasya = Fisher(name='Вася', worms=10)
kolya = Fisher(name='Коля', worms=10)

print('.' * 20, 'Они пошли на рыбалку')

vasya.start()
kolya.start()

print('.' * 20, 'Ждем пока они вернутся...')

vasya.join()
kolya.join()

print('.' * 20, 'Итак, они вернулись')

for fisher in (vasya, kolya):
    print(f'Итого рыбак {fisher.name} поймал:')
    for fish, count in fisher.catch.items():
        print(f'    {fish} - {count}')


# Вроде все прекрасно, но в пайтоне есть суровый GIL - Global Interpreter Lock - https://goo.gl/MTokAe
# GIL велик и ужасен - это механизм блокировки выполнения потоков, пока один выполняется.
# Что, почему, зачем, Карл?! Зачем стрелять себе в ногу?
#
# Все дело в том, что сам пайтон - процесс в операционной системе. И ОС может приостанавливать выполнение
# самого процесса пайтона. А когда происходит двойное засыпание/просыпание,
# то возникает проблема доступа к одним и тем участкам памяти. Поэтому разработчики CPython,
# (а у нас именно эта реализация) решили сделать GIL.
#
# Поэтому нельзя получить выгоду в производительности программы в т.н. CPU-bounded алгоритмах
# (это те, которым требуется процессорное время и не нужны операции ввода/вывода)

class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)

    def run(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            _ = worm ** 10000  # фиксируем время ожидания поклевки
            fish = random.choice(FISH)
            if fish is not None:
                self.catch[fish] += 1


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 6)
        print(f'Функция {func.__name__} работала {elapsed} секунд(ы)',)
        return result
    return surrogate


@time_track
def run_in_one_thread(fishers):
    for fisher in fishers:
        fisher.run()


@time_track
def run_in_threads(fishers):
    for fisher in fishers:
        fisher.start()
    for fisher in fishers:
        fisher.join()


humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
fishers = [Fisher(name=name, worms=100) for name in humans]

run_in_one_thread(fishers)
run_in_threads(fishers)


# Хорошая новость в том, что пайтон отпускает GIL перед системными вызовами. Чтение из файла, к примеру,
# может занимать длительное время и совершенно не требует GIL — можно дать шанс другим потокам поработать.
# ...
# Профит! там где есть операции ввода/ввывода: чтение с диска, обменд данными по сети, етс.
# Хорошая новость: любая программа должна обмениваться данными с внешним миром :)

class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)

    def run(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            time.sleep(0.01)  # TODO тут вызов системной функции
            fish = random.choice(FISH)
            if fish is not None:
                self.catch[fish] += 1


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 6)
        print(f'Функция {func.__name__} работала {elapsed} секунд(ы)',)
        return result
    return surrogate


@time_track
def run_in_one_thread(fishers):
    for fisher in fishers:
        fisher.run()


@time_track
def run_in_threads(fishers):
    for fisher in fishers:
        fisher.start()
    for fisher in fishers:
        fisher.join()


humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
fishers = [Fisher(name=name, worms=100) for name in humans]

run_in_one_thread(fishers)
run_in_threads(fishers)


# Про обьяснение механизма GIL очень рекомендую посмотреть видео с Moscow Python Meetup:
# Григорий Петров. "GIL в Python: зачем он нужен и как с этим жить"
# http://www.moscowpython.ru/meetup/14/gil-and-python-why/

###
# Извне завершить поток невозможно штатными средствами пайтона.
# И это правильно, вот две основные проблемы с "убийством" потока:
#   - поток может активно работать с данными в этот момент и принудительное завершениие разрушит их целостность.
#   - поток может породить другие потоки - их тоже завершать?
# Что делать? Можно добавить признак выхода:

class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)
        # будем проверять в цикле - а не пора ли нам заканчивать?
        self.need_stop = False

    def run(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.catch[fish] += 1
            if self.need_stop:
                print(f'{self.name}: Ой, жена ужинать зовет! Сматываем удочки...', flush=True)
                break


vasya = Fisher(name='Вася', worms=100)
vasya.start()
time.sleep(1)
if vasya.is_alive():  # кстати с помощью этого метода можно проверить выполняется ли еще поток?
    vasya.need_stop = True
vasya.join()  # ожидание завершения обязательно - поток может некоторое время финализировать работу

# Подводя итог, нужно сказать, что в мультипоточном программированиии наши линейный код
# перестают быть линейным (СИНХРОННЫМ). Если ранее мы были уверены в последовательности выполнения кода,
# то при использовании потоков (процессов) код может выполняться АСИНХРОННО: нельзя гарантировать
# что за этим блоком кода будет выполняться вот этот.
# Представьте себе спагетти, которые мешают вилкой: где и когда соприкоснуться макаронины никто не знает...
