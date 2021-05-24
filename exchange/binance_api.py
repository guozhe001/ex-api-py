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


def get_exchange_info():
    return client.get_exchange_info()


def get_symbol(symbol):
    return client.get_symbol_info(symbol)


def get_kline(symbol, interval, start_time, end_time):
    """
    根据交易对获取k线数据
    :param symbol:
    :param interval:
    :param start_time:
    :param end_time:
    :return:
    """
    return client.get_klines(symbol=symbol, interval=interval, startTime=start_time, endTime=end_time)
