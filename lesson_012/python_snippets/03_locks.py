# -*- coding: utf-8 -*-


# Асинхронное программирование порождает несколько проблем.
#
# Одна из них - доступ к совместным данным: если два потока меняют один и тот же обьект,
# то программа становится непредсказуемой. Эта проблема называется состояние гонки (race conditions)
# https://goo.gl/Dz9aJ3
import random
from collections import defaultdict

import threading

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(threading.Thread):

    def __init__(self, name, worms, fish_tank, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.fish_tank = fish_tank

    def run(self):
        for worm in range(self.worms):
            fish = random.choice(FISH)
            if fish is not None:
                self.fish_tank[fish] += 1
                self.catched += 1


# Общий сачок для рыбы
global_fish_tank = defaultdict(int)

humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
fishers = [Fisher(name=name, worms=10000, fish_tank=global_fish_tank) for name in humans]

for fisher in fishers:
    fisher.start()
for fisher in fishers:
    fisher.join()

total_fish_from_fishers = sum(fisher.catched for fisher in fishers)
total_fish_in_tank = sum(global_fish_tank.values())

print(f'Итого рыбаки поймали {total_fish_from_fishers} шт., а с берега увидели {total_fish_in_tank} шт.')

# то есть ИНОГДА возникает случай, когда один поток взял значение total_fish что бы прибавить 1
# и другой поток взял значение total_fish что бы прибавить 1. Пусть total_fish было 42.
# Первый поток прибавил 1 и записывает 43, и второй поток прибавил 1 и записывает 43.
# А должно быть 44 - одна рыбка потерялась...

# Что делать?
# Стараться использовать потокобезопасные атомарные операции.
# Атомарная операция - операция, выполняемая за 1 шаг, без возможности прерывания её другим потоком.
# Вот некоторые потокобезопасные операции:
#     выборка элемента из списка: my_list[xx]
#     модификация списка "на месте" (т.е. с помощью методов): my_list.append(xx)
#     выборка элемента из словаря: my_dict[key]
#     модификация словаря "на месте: my_dict.update(key=value)
#     чтение одного атрибута объекта: my_obj.attr
#     изменение одного атрибута объекта: my_obj.attr = val
#     чтение одной глобальной переменной: my_global
#     изменение одной глобальной переменной: my_global = val
# как мы видели += не атомарная, как и my_global = my_global + val
#
# Не всегда удается обойтись только атомарными операциями и нужно использовать методы синхронизации потоков.
# Они синхронизируют код: потоки замирают и ждут, пока другие потоки работают.
#
# Наверно основной примитив синхронизации называется блокировками - locks.
# Блокировку можно представить как кабинку вокруг кода - войти может только один, а на двери замок.
# Один поток входит в кабинку, закрывает замок (acquire),
# даже если остальным сильно надо в кабинку - они все равно ждут.
# Когда поток сделает все свои дела и выходит из кабинки, то он открывает замок (release)
# И в кабинку может войти следующий поток, случайный из ждущих.


class Fisher(threading.Thread):

    def __init__(self, name, worms, fish_tank, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.fish_tank = fish_tank
        self.fish_tank_lock = lock

    def run(self):
        for worm in range(self.worms):
            fish = random.choice(FISH)
            if fish is not None:
                self.fish_tank_lock.acquire()
                self.fish_tank[fish] += 1
                self.fish_tank_lock.release()
                # with self.fish_tank_lock:
                #     self.fish_tank[fish] += 1
                self.catched += 1


# Общий сачок для рыбы
global_fish_tank = defaultdict(int)

humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
lock = threading.Lock()
fishers = [Fisher(name=name, worms=100000, fish_tank=global_fish_tank, lock=lock) for name in humans]

for fisher in fishers:
    fisher.start()
for fisher in fishers:
    fisher.join()

total_fish_from_fishers = sum(fisher.catched for fisher in fishers)
total_fish_in_tank = sum(global_fish_tank.values())

print(f'Итого рыбаки поймали {total_fish_from_fishers} шт., а с берега увидели {total_fish_in_tank} шт.')

# В момент вызова self.lock.acquire() асинхронные потоки синхонизируются по времени.

# С блокировками нужно обращаться аккуратно - всегда освобождать, даже при падении потока.
# Иначе другие потоки не смогут никогда войти в кабинку нужного кода.

# Что бы блокировки могли быть вложенными, нужно использовать RLock
# это блокировка, которую можно еще раз залочить в этом же потоке - https://goo.gl/TzywJj
lock = threading.RLock()

###
# Другая проблема с блокировками: они могут быть взаимными.
# Один поток заблокировал ресурс A и ему нужен ресурс Б, а другой поток наобарот - заблокировал Б и ждет А.


def func_1(n):
    global a, b
    for i in range(n):
        print(f'{i}: func_1 wait lock_A', flush=True)
        with lock_A:
            print(f'{i}: func_1 take lock_A', flush=True)
            a += 1
            print(f'{i}: func_1 wait lock_B', flush=True)
            with lock_B:
                print(f'{i}: func_1 take lock_B', flush=True)
                b += 1


def func_2(n):
    global a, b
    for i in range(n):
        print(f'{i}: func_2 wait lock_B', flush=True)
        with lock_B:
            print(f'{i}: func_2 take lock_B', flush=True)
            b += 1
            print(f'{i}: func_2 wait lock_A', flush=True)
            with lock_A:
                print(f'{i}: func_2 take lock_A', flush=True)
                a += 1


a = 0
b = 0
lock_A = threading.RLock()
lock_B = threading.RLock()
N = 10

thread_1 = threading.Thread(target=func_1, args=(N,))
thread_2 = threading.Thread(target=func_2, args=(N,))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print(a, b)

# Это называется красиво: deadlock - тупик или безвыходное положение.
# Что делать, что бы избежать deadlock-ов?
#
# Вот рецепты, в порядке убывания значимости:
#  - стараться как можно меньше использовать общие обьекты (глобальные обьекты состояния)
#  - делать как можно меньше вложенных блокировок
#  - внимательно обращаться с существующими блокировками
# Вообще, эти рекомендации относятся ко всему асинхронному программированию,
# вот статья для медитации над этой темой: https://dev.by/news/pochemu-oni-ne-umeyut-pisat-mnogopotochnye-programmy


###
# Есть еще несколько способов синхронизировать потоки:
#
# Семафоры (Semaphore) - https://goo.gl/PZFKTu - очень похожи на Lock, но позволяют выполнять критичный код
# нескольким потокам
#
# Барьер (Barrier) - https://goo.gl/9f1MHk - позволяет нескольким потокам продолжить свое выполнение одновременно.
# Если в потоке есть barrier.wait() то поток приостанавливается, пока все остальные потоки не вызовут barrier.wait()
#
# События (Events) - https://goo.gl/ewCFgh - поток(и) могут ждать пока событие не будет установлено,
# а другой поток может устанавливать или сбрасывать это событие.
#
# Условные переменные (Condition) - https://goo.gl/mVF6rw - позволяют потоку ждать, пока другой поток
# подготовит данные и сообщит об этом
#
# Таймер (Timer) - https://goo.gl/TqZXXY - похож на простой Thread, но начинает выполнение через N секуднд
#
# Хорошая статья про примитивы синхронизации: Fredrik Lundh "Thread Synchronization Mechanisms in Python"
# перевод http://www.quizful.net/post/thread-synchronization-in-python



