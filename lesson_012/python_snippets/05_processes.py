# -*- coding: utf-8 -*-

# Многопроцессное программирование.
#
# Очень похоже на многопточное, но порождает процессы операционной системы.
# Это позволяет использовать все ядра всех процессоров (GIL действует только внутри одного процесса).
# Но как всегда - есть ньюансы...
#
# Основной - то, что порождается новый процесс в операционной системе, со своей ОТДЕЛЬНОЙ памятью,
# И изменения обьектов в памяти одного процесса никак не отражатеся в памяти другого.
# Потоки же имеют доступ ко всем обьектам в памяти одного процесса, именно поэтому мы могли
# в разных потоках изменять один и тот же обьект (используя блокировки, конечно же).
# Что делать? Передавать данные с помощью специальных механизмов (Pipe, Queue)
#
# Второй ньюанс - как порождаются процессы. В linux/mac os это происходит с помощью т.н. форка (fork)
# в момент порождения нового процесса ПОЛНОСТЬЮ копируется состяние памяти процесса-родителя.
# То есть все текущие значения переменных копируются в процесс-потомок, и дальше уже живут независимо.
# В windows механизм другой (windows == боль) - тут используется spawn. При этом методе запускается
# новый интерпретатор, с чистой памятью и процесс-потомок наследует только параметры запуска процеса.
# Ну и spawn, та-дам!, медленнее.
#
# Давайте попробуем.
import os
import random
from collections import defaultdict
from multiprocessing import Process, Pipe, Queue
from queue import Empty

FISH = (None, 'плотва', 'окунь', 'лещ')


def fishing(name, worms):
    print(f'{name} parent process:', os.getppid())
    print(f'{name} process id:', os.getpid())
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


if __name__ == '__main__':
    # Для windows это условие обязательно

    # Второй рыбак у нас будет ловить в отдельном процессе
    proc = Process(target=fishing, kwargs=dict(name='Вася', worms=10))
    proc.start()

    fishing(name='Коля', worms=10)

    proc.join()


# Лучше на классах
class Fisher(Process):

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


if __name__ == '__main__':
    vasya = Fisher(name='Вася', worms=10)
    kolya = Fisher(name='Коля', worms=10)

    print('.' * 20, 'Они пошли на рыбалку')

    vasya.start()
    kolya.start()
    # Обратите внимание на загрузку процессоров

    # _ = 3 ** (random.randint(50, 70) * 10000)
    print('.' * 20, 'Ждем пока они вернутся...')

    vasya.join()
    kolya.join()

    print('.' * 20, 'Итак, они вернулись')

# Видно что multiprocessing очень сильно похож на threading по методам.
# Это сделано намеренно, что бы было легче портировать программы.


# А теперь посмотрим на различия
class Fisher(Process):

    def __init__(self, name, worms, fish_tank, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.fish_tank = fish_tank

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            # _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is not None:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.fish_tank[fish] += 1
                self.catched += 1


global_fish_tank = defaultdict(int)

if __name__ == '__main__':

    humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
    fishers = [Fisher(name=name, worms=1000, fish_tank=global_fish_tank) for name in humans]

    for fisher in fishers:
        fisher.start()
    for fisher in fishers:
        fisher.join()

    total_fish_from_fishers = sum(fisher.catched for fisher in fishers)
    total_fish_in_tank = sum(v for _, v in global_fish_tank.items())

    print(f'Итого рыбаки поймали {total_fish_from_fishers} шт., а с берега увидели {total_fish_in_tank} шт.')


# То есть родительский процесс вообще не видит, что происходит в дочерних...
# Что делать? надо обмениваться информацией, Ватсон!
# Делается это с помощью класса Pipe (труба). С его помощью можно передавать обьект от процесса к процессу.


class Fisher(Process):

    def __init__(self, name, worms, conn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.conn = conn

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is not None:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.catched += 1
        print(f'{self.name}: Всего поймал {self.catched}', flush=True)
        # будем передавать только общее количество
        self.conn.send([self.name, self.catched])
        self.conn.close()


if __name__ == '__main__':

    humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
    fishers, pipes = [], []
    for name in humans:
        parent_conn, child_conn = Pipe()
        fisher = Fisher(name=name, worms=100, conn=child_conn)
        fishers.append(fisher)
        pipes.append(parent_conn)

    for fisher in fishers:
        fisher.start()
    total_fish = 0
    for conn in pipes:
        name, fish_count = conn.recv()
        print('.' * 30, f'на берегу увидели: {name} поймал {fish_count}')
        total_fish += fish_count
    for fisher in fishers:
        fisher.join()

    print(f'Итого рыбаки поймали {total_fish} шт.')
# Через Pipe передается только один обьект, если в трубу закинуть новый обьект, старый исчезнет
# Если нужно передать несколько обьектов, то мы уже знаем решение - Queue


class Fisher(Process):

    def __init__(self, name, worms, fish_receiver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.fish_receiver = fish_receiver

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}, {worm}: забросили ждем...', flush=True)
            # time.sleep(random.randint(1, 3) / 10)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}, {worm}: сожрали червяка!', flush=True)
            else:
                print(f'{self.name}, {worm}: поймал  {fish} и хочет положить его в садок', flush=True)
                if self.fish_receiver.full():
                    print(f'{self.name}, {worm}: садок полон !!!', flush=True)
                # Этот метод у очереди - атомарный и блокирующий
                # Поток приостанавливается, пока нет места в очереди
                self.fish_receiver.put(fish)
                print(f'{self.name}, {worm}: наконец-то положил {fish} в садок', flush=True)


class Boat(Process):

    def __init__(self, worms_per_fisher, humans, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher
        self.fish_receiver = Queue(maxsize=2)
        self.fish_tank = defaultdict(int)
        self.humans = humans

    def run(self):
        print('Лодка вышла в море...', flush=True)
        for name in self.humans:
            fisher = Fisher(name=name, worms=self.worms_per_fisher, fish_receiver=self.fish_receiver)
            self.fishers.append(fisher)
        for fisher in self.fishers:
            fisher.start()
        while True:
            try:
                # Этот метод у очереди - атомарный и блокирующий,
                # Поток приостанавливается, пока нет элементов в очереди
                fish = self.fish_receiver.get(timeout=1)
                print(f'Садок принял {fish}', flush=True)
                self.fish_tank[fish] += 1
            except Empty:
                print(f'В садке пусто в течении 1 секунды', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break
        for fisher in self.fishers:
            fisher.join()
        print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)


if __name__ == '__main__':
    # Нельзя создать процессы рыбаков в главном процессе, а запустить их в процессе лодки - разная память.
    # Защита от дурака - нельзя создать процесс в этом процессе, а запустить в другом
    boat = Boat(worms_per_fisher=10, humans=['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ])
    boat.start()
    boat.join()

# Так же в multiprocessing есть обьекты синхронизации - RLock, Barrier, Condition, Event, Semaphore.
# Это практически клоны своих тезок из threading.
