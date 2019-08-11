import logging
import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id

try:
    from config import TOKEN, GROUP_ID
except ImportError:
    exit('DO cp config.txt config.default.txt')


def log_settings(log):
    fh_formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s: %(message)s', datefmt='%m-%d-%Y %H:%M:%S')
    fh = logging.FileHandler(filename='vkBot.log', delay=True)
    fh.setLevel(level=logging.WARNING)
    fh.setFormatter(fh_formatter)

    sh_formatter = logging.Formatter(fmt='%(levelname)s: %(message)s', datefmt='%m-%d-%Y %H:%M:%S')
    sh = logging.StreamHandler()
    sh.setLevel(level=logging.WARNING)
    sh.setFormatter(sh_formatter)

    log.setLevel(logging.DEBUG)
    log.addHandler(fh)
    log.addHandler(sh)


class Bot:
    '''
    Эхо Бот
    '''

    def __init__(self, token, group_id):
        self.log = logging.getLogger('vkBot')
        log_settings(self.log)

        self.token = token
        self.group_id = group_id
        self.vk = vk_api.VkApi(token=token)
        self.longpoll = VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()

    def start(self):
        self.log.info('Бот запущен.')
        for event in self.longpoll.listen():
            try:
                self.on_event(event)
            except Exception as exc:
                self.log.exception(f'ошибка {exc}')

    def on_event(self, event: VkBotEventType):
        '''
        Событие при получении сообщения
        :param event: VkBotMessageEvent
        :return: None
        '''
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.log.info('Бот получил сообщение %s', event.object.text)
            self.api.messages.send(message=event.object.text,
                                   random_id=get_random_id(),
                                   peer_id=event.object.peer_id)
        else:
            self.log.warning('Я ещё не умею работать с данными методами %s', event.type)


if __name__ == '__main__':
    bot = Bot(token=TOKEN, group_id=GROUP_ID)
    bot.start()

# Оставил тудушки в файле requirements - их надо поправить к следующему дз тогда.
# а так зачет!
