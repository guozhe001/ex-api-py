# encoding=utf8

from config import config_util
from constant import constant

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key, secret = config_util.get_api_key_secret(exchange=constant.EXCHANGE_BINANCE)
    print("key={}, secret={}".format(key, secret))
