from unittest import TestCase

from exchange import binance_api


class Test(TestCase):
    def test_get_all_tickers(self):
        tickers = binance_api.get_all_tickers()
        for t in tickers:
            print(t)
