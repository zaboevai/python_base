from config import TOKEN, GROUP_ID
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.utils import get_random_id


class Bot:

    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id
        self.session = vk_api.VkApi(token=token)
        self.vk = self.session.get_api()

    def start(self):

        try:
            longpoll = VkLongPoll(vk=self.session, wait=5, group_id=GROUP_ID)
        except Exception as exc:
            print(exc)
            return

        for event in longpoll.listen():
            self.on_event(event)

    def on_event(self, event):
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            self.vk.messages.send(user_id=event.user_id,
                                  random_id=get_random_id(),
                                  message='Привет!')


if __name__ == '__main__':
    bot = Bot(token=TOKEN, group_id=GROUP_ID)
    bot.start()
