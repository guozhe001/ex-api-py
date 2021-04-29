# encoding=utf8
from binance.client import Client

from config import config_util
from constant import constant

key, secret = config_util.get_api_key_secret(exchange=constant.EXCHANGE_BINANCE)
client = Client(key, secret)


def get_all_tickers():
    """
    :return:
     {{'symbol': 'NEBLBNB', 'price': '0.01356000'}}
    """
    tickers = client.get_all_tickers()
    return tickers


def get_order_book(symbol):
    """
    :param symbol: 交易对
    :return:
        {
          "lastUpdateId": 1027024,
          "bids": [
            [
              "4.00000000",     // 价位
              "431.00000000"    // 挂单量
            ]
          ],
          "asks": [
            [
              "4.00000200",
              "12.00000000"
            ]
          ]
        }
    """
    return client.get_order_book(symbol=symbol)
