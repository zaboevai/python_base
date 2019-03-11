# -*- coding: utf-8 -*-

# Что делать, если нужно __дополнить__ поведение?
# Дочерний класс делает то же самое, что и родительский, плюс нечто большее


class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class VacuumCleaningRobot(Robot):

    def __init__(self, model):
        super().__init__(model=model)
        self.dust_bug = 0

    def operate(self):
        print('Робот пылесосит пол, заполенность мешка для пыли', self.dust_bug)


roomba = VacuumCleaningRobot(model='roomba M505')
print(roomba)
roomba.operate()


class WarRobot(Robot):

    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        print('Робот охраняет военный обьект c помощью', self.gun)


r2d2 = WarRobot(model='R2D2', gun='пулемет')
print(r2d2)
r2d2.operate()


class SubmarineRobot(WarRobot):

    def operate(self):
        super().operate()
        print('Охрана ведется под водой')


rc_submarine = WarRobot(model='Orbiter', gun='лазер')
print(rc_submarine)
rc_submarine.operate()


