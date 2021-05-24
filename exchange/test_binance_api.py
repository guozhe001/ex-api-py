from unittest import TestCase

from exchange import binance_api
from util import date_util


class Test(TestCase):
    def test_get_all_tickers(self):
        tickers = binance_api.get_all_tickers()
        for t in tickers:
            print(t)

    def test_get_exchange_info(self):
        exchange_info = binance_api.get_exchange_info()
        # print(symbol)
        print(type(exchange_info))
        for k in exchange_info:
            print(k, type(exchange_info[k]))

        symbols = exchange_info["symbols"]
        for symbol_info in symbols:
            print(type(symbol_info))
            for s_k in symbol_info:
                print(s_k, symbol_info[s_k])
            break

    def test_get_symbol(self):
        symbol = binance_api.get_symbol("MDXUSDT")
        for k in symbol:
            print(k, symbol[k])

    def test_get_kline(self):
        kline = binance_api.get_kline("MDXUSDT", "1m", date_util.to_timestamp("2021-05-24 17:00:00"),
                                      date_util.get_now_timestamp())
        for info in kline:
            info.append(date_util.timestamp_to_str(info[0] / 1000))
            print(info)
