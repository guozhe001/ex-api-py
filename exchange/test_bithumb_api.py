from unittest import TestCase

from exchange import bithumb_api


class Test(TestCase):
    def test_get_min_withdrawal(self):
        print(bithumb_api.get_min_withdrawal("BTC"))
