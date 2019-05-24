# -*- coding: utf-8 -*-

# Кроме блокировок и примитивов синхронизации существует еще один способ обмена данными между потоками.
# Это очереди - Queue - https://docs.python.org/3.6/library/queue.html
# В очередь можно положить элемент и взять его. Queue гарантирует что потоки не помешают друг другу
# - операции очереди атомарные и блокирующие.

import time
from collections import defaultdict

import queue
import random
import threading

FISH = (None, 'плотва', 'окунь', 'лещ')


# Посадим всех рыбаков в лодку, в которой есть садок для улова.
class Fisher(threading.Thread):

    def __init__(self, name, worms, catcher, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catcher = catcher

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}, {worm}: забросили ждем...', flush=True)
            # time.sleep(random.randint(1, 3) / 10)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}, {worm}: сожрали червяка!', flush=True)
            else:
                print(f'{self.name}, {worm}: поймал  {fish} и хочет положить его в садок', flush=True)
                if self.catcher.full():
                    print(f'{self.name}, {worm}: приемщик полон !!!', flush=True)
                # Этот метод у очереди - атомарный и блокирующий
                # Поток приостанавливается, пока нет места в очереди
                self.catcher.put(fish)
                print(f'{self.name}, {worm}: наконец-то отдал {fish} приемщику', flush=True)


class Boat(threading.Thread):

    def __init__(self, worms_per_fisher=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher
        self.catcher = queue.Queue(maxsize=2)
        self.fish_tank = defaultdict(int)

    def add_fisher(self, name):
        fisher = Fisher(name=name, worms=self.worms_per_fisher, catcher=self.catcher)
        self.fishers.append(fisher)

    def run(self):
        print('Лодка вышла в море...', flush=True)
        for fisher in self.fishers:
            fisher.start()
        while True:
            try:
                # Этот метод у очереди - атомарный и блокирующий,
                # Поток приостанавливается, пока нет элементов в очереди
                fish = self.catcher.get(timeout=1)
                print(f'Приемщик принял {fish} и положил в садок', flush=True)
                self.fish_tank[fish] += 1
            except queue.Empty:
                print(f'Приемщику нет рыбы в течении 1 секунды', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break
        for fisher in self.fishers:
            fisher.join()
        print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)


boat = Boat(worms_per_fisher=10)

humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
for name in humans:
    boat.add_fisher(name=name)

boat.start()
boat.join()

print(f'лодка привезла {boat.catch}')

# Мы использовали очередь вида FIFO - first input, first output - первый вошел, первый вышел.
# В модуле queue есть еще два вида очередей:
#   LifoQueue - last input, first output - последний вошел, первый вышел (еще такую очередь называют стеком).
#   PriorityQueue - первым возвращается наименьший элемент, то есть sorted(list(entries))[0]
