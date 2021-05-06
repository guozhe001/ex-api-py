# encoding=utf8

from exchange import binance_api

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    book = binance_api.get_order_book("ETHBTC")
    print(book)
