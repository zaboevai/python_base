import unittest
from unittest.mock import Mock, patch

import main
from main import Bot


class Test1(unittest.TestCase):

    def test_bot_start(self):
        count = 5
        obj = [{'a': 1}]
        events = [obj] * count

        # session = Mock()
        # vk_api_method = Mock()
        # session.get_api = vk_api_method
        # vk = session.get_api('')

        long_poller_mock = Mock(return_value=events)
        VkLongPoll = Mock()
        long_poller_listen_mock = VkLongPoll
        long_poller_listen_mock.listen = long_poller_mock

        # bot = Bot('', '')
        # bot.on_event = Mock()
        # bot.start()

        # self.assertEquals().

        with patch('main.vk_api.VkApi'):
            with patch('main.VkLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.start()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == 5
