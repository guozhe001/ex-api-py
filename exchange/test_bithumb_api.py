from unittest import TestCase

from exchange import bithumb_api


class Test(TestCase):
    def test_get_min_withdrawal(self):
        print(bithumb_api.get_min_withdrawal("BTC"))

    def test_get_asset_status(self):
        status = bithumb_api.get_asset_status("BTC")
        print(status)

    def test_get_ticker(self):
        ticker = bithumb_api.get_ticker("BTC", "KRW")
        print(ticker)
        print(type(ticker))

    def test_print_all_coins(self):
        for coin in bithumb_api.all_coin:
            print(coin)

    def test_get_all_coin_btc_ticker(self):
        for re in bithumb_api.get_all_coin_btc_ticker():
            print(re)
