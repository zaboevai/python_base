import unittest
from unittest.mock import Mock, patch, ANY

from vk_api.bot_longpoll import VkBotMessageEvent, VkBotEventType

from ..main import Bot


class TestBot(unittest.TestCase):
    RAW_EVENT = {'type': VkBotEventType.MESSAGE_NEW,
                 'object': {'date': 1565551500, 'from_id': 4145622, 'id': 194, 'out': 0, 'peer_id': 4145622,
                            'text': 'test', 'conversation_message_id': 194, 'fwd_messages': [], 'important': False,
                            'random_id': 0, 'attachments': [], 'is_hidden': False},
                 'group_id': 184332451}

    def test_bot_start(self):
        count = 5
        obj = [{'a': 1}]
        events = [obj] * count

        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('main.vk_api.VkApi'), patch('main.VkBotLongPoll', return_value=long_poller_listen_mock):
            bot = Bot('', '')
            bot.on_event = Mock()
            bot.start()

            bot.on_event.assert_called()
            bot.on_event.assert_any_call(obj)
            assert bot.on_event.call_count == count

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)

        send_mock = Mock()

        with patch('main.vk_api.VkApi'), patch('main.VkBotLongPoll'):
            bot = Bot('', '')
            bot.api = Mock()
            bot.api.messages.send = send_mock

            bot.on_event(event)

        send_mock.assert_called_once_with(message=self.RAW_EVENT['object']['text'],
                                          random_id=ANY,
                                          peer_id=self.RAW_EVENT['object']['peer_id'])

# зачет!