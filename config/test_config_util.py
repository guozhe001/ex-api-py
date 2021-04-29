from unittest import TestCase

import config_util
from constant import constant


class Test(TestCase):
    def test_get_api_key_secret(self):
        key, secret = config_util.get_api_key_secret(constant.EXCHANGE_BINANCE)
        print("key={}, secret={}".format(key, secret))
