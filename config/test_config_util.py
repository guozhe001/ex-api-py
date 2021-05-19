from unittest import TestCase

import config_util
from constant import constant


class Test(TestCase):
    def test_get_api_key_secret(self):
        key, secret = config_util.get_api_key_secret(constant.EXCHANGE_BINANCE)
        print("key={}, secret={}".format(key, secret))

    def test_list_sections(self):
        sections = config_util.list_sections()
        for section in sections:
            print(section)

    def test_list_all(self):
        list_all = config_util.list_all(constant.CONFIG_WANTED)
        print(type(list_all))
        for item in list_all:
            print(list_all[item])
