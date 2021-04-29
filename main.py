# encoding=utf8

from binance.client import Client

from config import config_util
from constant import constant

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key, secret = config_util.get_api_key_secret(exchange=constant.EXCHANGE_BINANCE)
    print("key={}, secret={}".format(key, secret))
    client = Client(key, secret)
    depth = client.get_order_book(symbol='BNBBTC')
    print(type(depth))
    print(depth)
